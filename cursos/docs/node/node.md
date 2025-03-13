## Passo a Passo para Instalar o Node.js via CLI

### **MacOS**

1. **Abra o Terminal**  
   Pressione `Command + Space`, digite `Terminal` e pressione `Enter`.

2. **Instale o Homebrew (se ainda não tiver)**  

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Instale o Node.js usando o Homebrew**  

   ```bash
   brew install node
   ```
        ==> Caveats
        node@22 is keg-only, which means it was not symlinked into /opt/homebrew,
        because this is an alternate version of another formula.

        If you need to have node@22 first in your PATH, run:
        echo 'export PATH="/opt/homebrew/opt/node@22/bin:$PATH"' >> /Users/kaebudke/.zshrc

        For compilers to find node@22 you may need to set:
        export LDFLAGS="-L/opt/homebrew/opt/node@22/lib"
        export CPPFLAGS="-I/opt/homebrew/opt/node@22/include"

4. **Verifique a Instalação**  

   ```bash
   node -v
   npm -v
   ```

   O comando retornará as versões instaladas do Node.js e do NPM.

---

### **Linux (Ubuntu/Debian)**

1. **Abra o Terminal**  
   Use o atalho `Ctrl + Alt + T`.

2. **Atualize os Repositórios**  

   ```bash
   sudo apt update && sudo apt upgrade
   ```

3. **Instale o Node.js pelo Repositório Oficial**  
   Adicione o repositório do Node.js:  

   ```bash
   curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   ```

   Substitua `18.x` pela versão desejada (por exemplo, `20.x`).

4. **Instale o Node.js**  

   ```bash
   sudo apt install -y nodejs
   ```

5. **Verifique a Instalação**  

   ```bash
   node -v
   npm -v
   ```

---

### **Windows**

1. **Abra o PowerShell como Administrador**  
   Pressione `Win + X` e selecione **Windows PowerShell (Admin)**.

2. **Baixe o Instalador do Node.js**  
   Use o comando:

   ```bash
   Invoke-WebRequest -Uri https://nodejs.org/dist/v18.18.2/node-v18.18.2-x64.msi -OutFile nodejs.msi
   ```

   Substitua a versão no link pelo número desejado (exemplo: `20.x`).

3. **Instale o Node.js**  
   Execute o arquivo baixado:  

   ```bash
   Start-Process .\nodejs.msi -Wait
   ```

4. **Adicione ao PATH (se necessário)**  

   ```bash
   $env:Path += ";C:\Program Files\nodejs"
   ```

5. **Verifique a Instalação**  

   ```bash
   node -v
   npm -v
   ```

---

### Dicas para Uso no VSCode

1. **Configuração do Terminal**  
   Abra o terminal integrado no VSCode com `Ctrl + ```.  
   Certifique-se de que está no ambiente correto (Bash, PowerShell ou Zsh).

2. **Depuração (Debugging)**  
   Crie um arquivo `launch.json`:  

   ```json
   {
       "version": "0.2.0",
       "configurations": [
           {
               "type": "node",
               "request": "launch",
               "name": "Launch Program",
               "program": "${workspaceFolder}/index.js"
           }
       ]
   }
   ```

4. [**ESLint e Prettier**](./lint_prettier.md)
   - Instale as extensões ESLint e Prettier no VSCode.
   - Configure um arquivo `.eslintrc` para manter seu código padronizado.

5. **Scripts NPM no VSCode**  
   Use o menu lateral "NPM Scripts" para executar comandos `npm run` diretamente.

6. **Dica de Performance**  
   Use a opção **"Node.js: Use Inspect"** no VSCode para monitorar o uso de memória e gargalos no código.
