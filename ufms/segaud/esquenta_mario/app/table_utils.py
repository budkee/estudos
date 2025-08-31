"""
table_utils.py
Auxiliares para carregar e usar tabelas de texto SNES personalizadas (.tbl).
"""
from __future__ import annotations 
from typing import Dict, List, Tuple

def load_tbl(path: str) -> Tuple[Dict[bytes, str], Dict[str, bytes]]:
    
    # Tabela de codificação
    enc: Dict[bytes, str] = {}
    dec: Dict[str, bytes] = {}
    
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(";") or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            left, right = line.split("=", 1)
            left = left.strip()
            right = right.strip()
            
            # left pode ser multibyte: "AB CD EF"
            try:
                b = bytes(int(x, 16) for x in left.split())
            except ValueError:
                continue
            enc[b] = right
            # O lado direito pode ser um token multi-caractere como "<END>" ou caracteres normais
            dec[right] = b

    # retornamos ambos os mapas e também a lista de chaves ordenadas para decodificação mais rápida
    return enc, dec

def greedy_decode(data: bytes, enc_map: Dict[bytes, str]) -> str:
    # chaves ordenadas por tamanho decrescente para o maior encaixe possível
    ordered = sorted(enc_map.keys(), key=len, reverse=True)
    out: List[str] = []
    i = 0
    n = len(data)
    while i < n:
        matched = False
        for k in ordered:
            if data.startswith(k, i):
                out.append(enc_map[k])
                i += len(k)
                matched = True
                break
        if not matched:
            # fallback: mostra byte desconhecido como <HH>
            out.append(f"<{data[i]:02X}>")
            i += 1
    return "".join(out)

def greedy_encode(text: str, dec_map: Dict[str, bytes]) -> bytes:
    # Tentamos encaixar tokens no texto.
    # Tokens são envoltos como <END> ou <0A>. Para caracteres únicos, apenas use o caractere.
    out = bytearray()
    i = 0
    n = len(text)
    while i < n:
        if text[i] == "<":
            j = text.find(">", i + 1)
            if j != -1:
                token = text[i:j+1]
                if token in dec_map:
                    out.extend(dec_map[token])
                    i = j + 1
                    continue
                # se o token parece ser hexadecimal tipo <0A>
                inner = token[1:-1]
                if all(c in "0123456789ABCDEFabcdef" for c in inner) and len(inner) in (2,4):
                    # permite 1 ou 2 bytes como <0A> ou <0A0B>
                    bs = bytes.fromhex(inner)
                    out.extend(bs)
                    i = j + 1
                    continue
        ch = text[i]
        if ch in dec_map:
            out.extend(dec_map[ch])
        else:
            # fallback: escreve o código ASCII do caractere se 0-255, senão usa 0x3F
            code = ord(ch)
            out.append(code if 0 <= code <= 255 else 0x3F)
        i += 1
    return bytes(out)
    return bytes(out)
