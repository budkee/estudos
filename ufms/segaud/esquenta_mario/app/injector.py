#!/usr/bin/env python3
"""
injector.py
Lê um CSV (gerado/adaptado do extractor) com textos possivelmente editados e injeta na ROM.

Restrições:
- Não ultrapassar o tamanho original de cada entrada, a não ser que você use --truncate para cortar.
- Preenchimento com --pad-byte (default 00) se o texto novo for menor.
- Usa a mesma tabela .tbl da extração para codificar o texto.

Uso:
  python injector.py ROM.sfc sample_snes.tbl edited.csv ROM_patched.sfc
  python injector.py ROM.sfc sample_snes.tbl edited.csv ROM_patched.sfc --truncate --pad-byte FF
"""
from __future__ import annotations
import argparse, csv, os, sys
from table_utils import load_tbl, greedy_encode

def main():
    p = argparse.ArgumentParser(description="Injeta textos editados na ROM usando tabela.")
    p.add_argument("rom_in")
    p.add_argument("table")
    p.add_argument("csv_in")
    p.add_argument("rom_out")
    p.add_argument("--truncate", action="store_true", help="Se novo texto for maior, corta para caber.")
    p.add_argument("--pad-byte", default="00", help="Byte de preenchimento (hex) quando novo texto for menor (default 00).")
    args = p.parse_args()

    if not os.path.exists(args.rom_in): print("ROM de entrada não encontrada.", file=sys.stderr); sys.exit(1)
    if not os.path.exists(args.table): print("Tabela não encontrada.", file=sys.stderr); sys.exit(1)
    if not os.path.exists(args.csv_in): print("CSV não encontrado.", file=sys.stderr); sys.exit(1)

    enc_map, dec_map = load_tbl(args.table)
    
    try:
        pad = bytes.fromhex(args.pad_byte)
    except ValueError:
        print("Valor inválido para --pad-byte. Use hex, ex.: 00 ou FF", file=sys.stderr); sys.exit(2)
    if len(pad) != 1:
        print("--pad-byte deve ser 1 byte.", file=sys.stderr); sys.exit(2)

    rom = bytearray(open(args.rom_in, "rb").read())

    # Leitura CSV
    with open(args.csv_in, "r", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        required = {"offset_dec", "length", "text"}
        if not required.issubset(rdr.fieldnames or []):
            print("CSV deve conter colunas: offset_dec,length,text", file=sys.stderr); sys.exit(2)

        count = 0
        for row in rdr:
            try:
                offset = int(row["offset_dec"])
                orig_len = int(row["length"])
            except ValueError:
                print(f"Linha inválida (offset/length): {row}", file=sys.stderr)
                continue
            new_text = row["text"]
            new_bytes = greedy_encode(new_text, dec_map)
            seg = new_bytes

            if len(new_bytes) > orig_len:
                if args.truncate:
                    seg = new_bytes[:orig_len]
                    
                else:
                    print(f"Erro: novo texto maior que o espaço ({len(new_bytes)} > {orig_len}) em offset {offset}. Use --truncate ou reduza o texto.", file=sys.stderr)
                    sys.exit(3)
            elif len(new_bytes) < orig_len:
                seg = new_bytes + pad * (orig_len - len(new_bytes))

            # aplicar
            rom[offset:offset+orig_len] = seg
            count += 1

    with open(args.rom_out, "wb") as f:
        f.write(rom)
    print(f"Injeção concluída. {count} entradas aplicadas em {args.rom_out}")

if __name__ == "__main__":
    main()
