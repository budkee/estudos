#!/bin/bash

while IFS= read -r pacote; do
    pip uninstall -y "$pacote"
done < requirements.txt
