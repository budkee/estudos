#!/bin/bash

# Configurando gateway e rede dinâmica (DHCP) para interface eth0 de um sistema Linux
nmcli con mod "eth0" ipv4.method auto
# nmcli con modify "eth0" ipv4.addresses 192.168.200.0/24
nmcli con modify "eth0" ipv4.gateway 192.168.200.1
nmcli con modify "eth0" ipv4.dns "9.9.9.9 1.1.1.1"
nmcli con up "eth0"
# ou
reboot

# Verificando a assinatura | Tor Browser
gpg --auto-key-locate nodefault,wkd --locate-keys torbrowser@torproject.org
gpg --output ./tor.keyring --export 0xEF6E286DDA85EA2A4BA7DE684E2C6E8793298290
gpgv --keyring ./tor.keyring ~/Downloads/tor-browser-linux-x86_64-13.0.1.tar.xz.asc ~/Downloads/tor-browser-linux-x86_64-13.0.1.tar.xz
