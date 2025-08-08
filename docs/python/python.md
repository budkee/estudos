# Snippets | Python

## Sumário

- [Prática](#prática)
- [Links e referências]()

## Prática

### Passo a Passo para Instalar Python via CLI

---

### **MacOS**

1. **Abra o Terminal**  
   Pressione `Command + Space`, digite `Terminal` e pressione `Enter`.

2. **Instale o Homebrew (se ainda não tiver)**

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Atualize o Homebrew**

   ```bash
   brew update
   ```

4. **Instale o Python**

   ```bash
   brew install python
   ```

5. **Verifique a Instalação**  
   Após a instalação, verifique a versão instalada:
   ```bash
   python3 --version
   pip3 --version
   ```

---

### **Linux (Ubuntu/Debian)**

1. **Abra o Terminal**  
   Use o atalho `Ctrl + Alt + T`.

2. **Atualize os Repositórios**

   ```bash
   sudo apt update && sudo apt upgrade
   ```

3. **Instale Dependências Necessárias**

   ```bash
   sudo apt install -y software-properties-common
   ```

4. **Adicione o Repositório PPA do Python (opcional para versões recentes)**

   ```bash
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt update
   ```

5. **Instale o Python**  
   Substitua `3.x` pela versão desejada:

   ```bash
   sudo apt install -y python3 python3-pip
   ```

6. **Verifique a Instalação**
   ```bash
   python3 --version
   pip3 --version
   ```

---

### **Windows**

1. **Abra o PowerShell como Administrador**  
   Pressione `Win + X` e selecione **Windows PowerShell (Admin)**.

2. **Baixe o Instalador do Python**  
   Use o comando abaixo para baixar a versão mais recente:

   ```bash
   Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe -OutFile python-installer.exe
   ```

   Substitua a versão no link (`3.12.2`) pela desejada.

3. **Instale o Python**  
   Execute o instalador:

   ```bash
   Start-Process .\python-installer.exe -Wait
   ```

   Durante a instalação:

   - Marque a opção **"Add Python to PATH"**.
   - Escolha a instalação personalizada e habilite **"Install for all users"**.

4. **Verifique a Instalação**  
   Após concluir, verifique se o Python foi instalado corretamente:
   ```bash
   python --version
   pip --version
   ```

---

### **Dicas Gerais**

- **Gerenciador de Versões**  
  Considere usar um gerenciador de versões para Python:

  - **Mac/Linux**: [pyenv](https://github.com/pyenv/pyenv)
    ```bash
    curl https://pyenv.run | bash
    ```
  - **Windows**: [pyenv-win](https://github.com/pyenv-win/pyenv-win)

- **Configurar Ambientes Virtuais**  
  Sempre use ambientes virtuais para isolar dependências:

  ```bash
  python3 -m venv myenv
  source myenv/bin/activate  # Mac/Linux
  myenv\Scripts\activate     # Windows
  ```

- **Atualizar pip**  
   Atualize o `pip` para a versão mais recente:
  ```bash
  python3 -m pip install --upgrade pip
  ```

Pronto! Python estará configurado e pronto para uso.

## Links e Referências

- [Command Reference](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-exec)