#!/usr/bin/env python3
"""
finder.py
Recebe uma string e retorna offset(s) e bytes em hexadecimal no arquivo ROM,
usando uma tabela (.tbl) de mapeamento (hex <-> caracteres).

Uso:
    python finder.py SMario.sfc "Welcome" --table tabelas/mario_dialogo_raw.tbl

Dicas:
- Se não fornecer --table, será usado ASCII direto (1 byte por char).
"""
import argparse, os, sys
from table_utils import load_tbl, greedy_encode

def encode_query(query: str, table: str|None) -> bytes:
    
    if table:
        # Carrega a tabela de mapeamento
        enc_map, dec_map = load_tbl(table)
        # Codifica a query usando a tabela
        return greedy_encode(query, dec_map)
    else:
        return query.encode("ascii", errors="replace")

def main():
    
    # Setup dos argumentos
    p = argparse.ArgumentParser(description="Busca sequência (via tabela) e mostra offsets + hex.")
    p.add_argument("rom", help="Caminho da ROM (ex.: SMario.sfc)")
    p.add_argument("query", help="Texto a buscar")
    p.add_argument("--table", "-t", help="Tabela .tbl para mapear caracteres")

    # Pega os argumentos
    args = p.parse_args()

    if not os.path.exists(args.rom):
        print(f"Erro: arquivo não encontrado: {args.rom}", file=sys.stderr)
        sys.exit(1)
    
    # Converte o texto em bytes usando a tabela, se fornecida
    needle = encode_query(args.query, args.table)
    if not needle:
        print("Nada para buscar (query vazia).", file=sys.stderr)
        sys.exit(2)

    with open(args.rom, "rb") as f:
        data = f.read()

    # Busca a sequência no arquivo
    i = 0
    found = 0
    n = len(needle)
    while True:
        # Busca a próxima ocorrência da sequência
        pos = data.find(needle, i)
        
        if pos == -1:
            break
        # Extrai o pedaço correspondente da ROM, a partir do offset
        chunk = data[pos:pos+n]
        # Mostra o offset (decimal e hex) e os bytes em hexadecimal
        hex_str = " ".join(f"{b:02X}" for b in chunk)
        print({"offset": f"{pos} (0x{pos:08X})", "hexadecimal": hex_str})

        # Avança a busca a partir do próximo byte
        i = pos + 1
        found += 1
    
    if not found:
        print("Nenhuma ocorrência encontrada.")

if __name__ == "__main__":
    main()
