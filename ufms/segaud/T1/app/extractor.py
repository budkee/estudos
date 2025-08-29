#!/usr/bin/env python3
"""
extractor.py
Extrai textos de regiões conhecidas da ROM usando uma tabela .tbl.

Você precisa fornecer:
  - ROM
  - Tabela .tbl
  - Um arquivo JSON com as regiões de texto a extrair (ex.: ranges.json)

Formato de ranges.json:
[
  {
    "name": "intro_message",
    "start": "0x123456",   # início (hex string ou inteiro)
    "end":   "0x123ABC",   # fim exclusivo (hex string ou inteiro)
    "terminator": "00"     # opcional: byte (ou múltiplos) de término em hex (sem 0x)
  }
]

Saída:
  - Um CSV com colunas: name,offset_hex,offset_dec,length,raw_hex,text
Uso:
  python extractor.py ROM.sfc sample_snes.tbl ranges.json output.csv
"""
from __future__ import annotations
import argparse, json, csv, os, sys
from typing import List, Dict, Any
from table_utils import load_tbl, greedy_decode

"""
Faz o parse de um valor hexadecimal ou decimal, por meio da conversão de tipos.
"""
def parse_hex_or_int(x: Any) -> int:

    # Se já for um inteiro, retorna como está
    if isinstance(x, int):
        return x
    # Se for uma string, tenta converter
    s = str(x).strip()
    if s.lower().startswith("0x"):
        return int(s, 16)
    return int(s, 16) if all(c in "0123456789abcdefABCDEF" for c in s) else int(s)

def main():

    # Setup dos argumentos
    p = argparse.ArgumentParser(description="Extrai textos de regiões da ROM usando tabela.")
    p.add_argument("rom")
    p.add_argument("table")
    p.add_argument("ranges_json")
    p.add_argument("out_csv")

    # Pega os argumentos
    args = p.parse_args()

    if not os.path.exists(args.rom): 
        print("ROM não encontrada.", file=sys.stderr); sys.exit(1)
    if not os.path.exists(args.table): 
        print("Tabela não encontrada.", file=sys.stderr); sys.exit(1)
    if not os.path.exists(args.ranges_json): 
        print("JSON de ranges não encontrado.", file=sys.stderr); sys.exit(1)

    enc_map, dec_map = load_tbl(args.table)

    with open(args.rom, "rb") as f:
        rom = f.read()

    # Carrega as regiões a partir do JSON
    ranges = json.load(open(args.ranges_json, "r", encoding="utf-8"))
    rows = []
    for r in ranges:
        name = r.get("name", "segment")
        start = parse_hex_or_int(r["start"])
        end = parse_hex_or_int(r["end"])
        term_hex = r.get("terminator")
        terminator = bytes.fromhex(term_hex) if term_hex else None

        if start < 0 or end > len(rom) or start >= end:
            print(f"Aviso: intervalo inválido para {name}.", file=sys.stderr)
            continue

        i = start
        while i < end:
            # leitura até terminador ou fim de bloco
            j = i
            if terminator:
                tlen = len(terminator)
                while j+tlen <= end and rom[j:j+tlen] != terminator:
                    j += 1
                # se encontrou terminador, exclui-o
                text_bytes = rom[i:j]
                next_pos = j + tlen if j+tlen <= end else end
            else:
                text_bytes = rom[i:end]
                next_pos = end

            if not text_bytes:
                i = next_pos
                continue

            text = greedy_decode(text_bytes, enc_map)
            raw_hex = " ".join(f"{b:02X}" for b in text_bytes)

            rows.append({
                "name": name,
                "offset_hex": f"0x{i:08X}",
                "offset_dec": i,
                "length": len(text_bytes),
                "raw_hex": raw_hex,
                "text": text
            })
            i = next_pos

    with open(args.out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["name","offset_hex","offset_dec","length","raw_hex","text"])
        w.writeheader()
        w.writerows(rows)
    print(f"Extração concluída. {len(rows)} entradas salvas em {args.out_csv}")

if __name__ == "__main__":
    main()
