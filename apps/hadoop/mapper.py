#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) < 7:
        continue
    ip = parts[0]
    url_match = re.search(r'\"(?:GET|POST) (.*?) HTTP', line)
    url = url_match.group(1) if url_match else "-"
    print(f"{ip}\t1")
    print(f"{url}\t1")
