# Como configurar suas chaves SSH

### **1. Verificar se você já possui uma chave SSH na sua máquina**

Abra o terminal e execute:  

```bash
ls ~/.ssh/id_*
```

Se aparecerem arquivos como `id_rsa` ou `id_ed25519`, significa que já existem chaves SSH criadas. Caso contrário, siga para o próximo passo.

---

### **2. Gerar uma nova chave SSH (se necessário)**  

Execute o comando:  

```bash
ssh-keygen -t ed25519 -C "seu_email@exemplo.com"
```

- **`-t ed25519`**: Especifica o tipo de chave (Ed25519 é mais seguro e moderno). Para compatibilidade com sistemas mais antigos, você pode usar `rsa` com `-t rsa -b 4096`.
- **`-C`**: Adiciona um comentário à chave, geralmente seu e-mail.  

Durante o processo:

1. Será solicitado um nome para o arquivo. Pressione **Enter** para aceitar o padrão (`~/.ssh/id_ed25519`).
2. Insira uma senha para proteger a chave ou pressione **Enter** para não usar senha.

---

### **3. Verificar a chave pública**

Após gerar a chave, visualize o conteúdo da chave pública:  

```bash
cat ~/.ssh/id_ed25519.pub
```

(Ou substitua `id_ed25519.pub` pelo nome do arquivo especificado na criação da chave.)  

Copie o conteúdo exibido (ele começa com algo como `ssh-ed25519`).

---

### **4. Configurar a chave pública no servidor remoto**

1. Acesse o servidor com sua senha atual:  

   ```bash
   ssh usuario@ip_do_servidor
   ```

2. No servidor, crie ou edite o arquivo `~/.ssh/authorized_keys`:  

   ```bash
   mkdir -p ~/.ssh
   nano ~/.ssh/authorized_keys
   ```

3. Cole a chave pública copiada anteriormente no arquivo e salve.

4. Ajuste as permissões:  

   ```bash
   chmod 700 ~/.ssh
   chmod 600 ~/.ssh/authorized_keys
   ```

---

### **5. Testar a conexão SSH**

Agora, desconecte-se do servidor e teste a conexão novamente:  

```bash
ssh usuario@ip_do_servidor
```

Se configurado corretamente, você não precisará mais da senha para acessar o servidor.

---

### **6. Configuração opcional: Arquivo de configuração SSH**

Para facilitar o acesso, configure o arquivo `~/.ssh/config` na sua máquina local:  

```bash
nano ~/.ssh/config
```

Adicione as informações do servidor:  

```
Host meu_servidor
    HostName ip_do_servidor
    User usuario
    IdentityFile ~/.ssh/id_ed25519
```

Agora, você pode conectar-se ao servidor apenas com:  

```bash
ssh meu_servidor
```

---

### **7. Segurança adicional**

- **Proteja sua chave privada**: Certifique-se de que somente você tenha acesso a ela:  

  ```bash
  chmod 600 ~/.ssh/id_ed25519
  ```

- **Use uma senha para a chave**: Isso aumenta a segurança em caso de comprometimento do seu dispositivo.

