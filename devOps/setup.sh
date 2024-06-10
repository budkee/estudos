#! usr/bin/sh

# Crie um usuário 'budkee'
adduser budkee

# Defina a senha do usuário 'budkee' como 'siriusb'
echo "budkee:siriusb" | chpasswd

# Atribua permissões de admin ao usuário
usermod -aG sudo budkee

# Faça login com ele
su - budkee
