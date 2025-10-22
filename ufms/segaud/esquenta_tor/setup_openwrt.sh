#!/bin/bash

# ====================== Baixando a imagem do OpenWRT ======================
# Baixando a imagem do OpenWRT para ARM
wget https://downloads.openwrt.org/releases/24.10.3/targets/armsr/armv8/openwrt-24.10.3-armsr-armv8-generic-ext4-combined-efi.img.gz
# Baixando o hash sha256 e a assinatura
wget https://downloads.openwrt.org/releases/24.10.3/targets/armsr/armv8/sha256sums
wget https://downloads.openwrt.org/releases/24.10.3/targets/armsr/armv8/sha256sums.asc

# Verificando o hash sha256
# sha256sum openwrt-24.10.3-armsr-armv8-generic-ext4-combined-efi.img.gz

# Colocando o hash baixado em um arquivo
sha256sum openwrt-24.10.3-armsr-armv8-generic-ext4-combined-efi.img.gz >> sha256sums2

# Comparando com o hash oficial
gpg --with-fingerprint --verify sha256sums.asc sha256sums
# sha256sum -c --ignore-missing sha256sums
# sha256sum -c sha256sums 2>&1 | grep openwrt-24.10.3-armsr-armv8-generic-ext4-combined-efi.img.gz

# Importando a chave pública
gpg --keyserver keys.openpgp.org --recv-keys 0x1D53D1877742E911
# Verificando a assinatura
gpg --verify sha256sums.asc sha256sums

# ====================== Preparando a imagem para o VirtualBox ======================
# descomprimindo o arquivo, se necessário
gunzip openwrt-24.10.3-armsr-armv8-generic-ext4-combined-efi.img.gz

# conversão
VBoxManage convertfromraw openwrt-24.10.3-armsr-armv8-generic-ext4-combined-efi.img openwrt-arm.vdi --format VDI
#ou
# sudo apt install qemu-utils
qemu-img convert -f raw -O vdi openwrt-24.10.3-armsr-armv8-generic-ext4-combined-efi.img openwrt-arm.vdi

# ====================== Ajustes do Host para permeabilidade da VM no VirtualBox ======================
# Mudando o ip da ponte do virtualBox
sudo ifconfig bridge101 inet 192.168.200.3 netmask 255.255.255.0