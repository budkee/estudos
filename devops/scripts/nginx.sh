#!/bin/bash

# Instala o Nginx
apt update
apt install -y nginx

# Inicia o Nginx
systemctl start nginx
systemctl enable nginx

# Configura o firewall para permitir tráfego HTTP e HTTPS
sudo ufw allow 'Nginx Full'
sudo ufw reload

# Cria um arquivo de configuração de exemplo
sudo cat <<EOL > /etc/nginx/sites-available/pluto
server {
    listen 80;
    server_name pluto.com;

    location / {
        root /var/www/pluto;
        index index.html;
    }
}
EOL

# Cria o diretório do site
mkdir -p /var/www/exemplo
echo "<h1>Bem-vindo ao Nginx!</h1>" > /var/www/exemplo/index.html

# Habilita a configuração do site
ln -s /etc/nginx/sites-available/exemplo /etc/nginx/sites-enabled/

# Testa a configuração do Nginx
nginx -t

# Reinicia o Nginx
systemctl restart nginx