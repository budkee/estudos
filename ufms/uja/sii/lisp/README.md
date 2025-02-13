# Lisp on Docker

Você pode criar um **Dockerfile** para configurar um ambiente de desenvolvimento com **SBCL** e **Quicklisp**. Aqui está um passo a passo para criar e executar um contêiner Docker rodando **Lisp**:

## Lisp on Container

### 📌 1. Criar o `Dockerfile`
Crie um arquivo chamado `Dockerfile` com o seguinte conteúdo:

```dockerfile
# Usar imagem base do SBCL
FROM debian:latest

# Atualizar pacotes e instalar dependências
RUN apt-get update && apt-get install -y \
    sbcl \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Baixar e instalar Quicklisp
RUN curl -o /tmp/ql.lisp http://beta.quicklisp.org/quicklisp.lisp && \
    sbcl --no-sysinit --no-userinit --load /tmp/ql.lisp \
         --eval '(quicklisp-quickstart:install :path "~/.quicklisp")' \
         --eval '(ql:add-to-init-file)' \
         --quit && \
    rm /tmp/ql.lisp

# Instalar Quicklisp-Slime-Helper
RUN sbcl --eval '(ql:quickload :quicklisp-slime-helper)' --quit

# Definir o diretório de trabalho
WORKDIR /scripts

# Comando padrão: iniciar um REPL do SBCL
CMD ["sbcl"]
```

---

### 📌 2. Criar e Executar o Contêiner

Agora, no mesmo diretório do `Dockerfile`, execute:

1. **Construir a imagem Docker:**
   ```sh
   docker build -t sbcl-lisp .
   ```

2. **Rodar um contêiner interativo com o Lisp REPL:**
   ```sh
   docker run -it --rm sbcl-lisp
   ```

Isso abrirá um **REPL do SBCL** dentro do contêiner.

---

### 📌 3. Executar um Script Lisp pelo Contêiner

Se quiser rodar um **script Lisp** (por exemplo, `script.lisp`) dentro do contêiner:

1. **Crie um arquivo** `script.lisp` com algum código, por exemplo:
   ```lisp
   (format t "Hello, Lisp in Docker!~%")
   ```

2. **Execute dentro do contêiner:**
   ```sh
   docker run --rm -v "$(pwd)/script.lisp:/scripts/script.lisp" sbcl-lisp sbcl --script /scripts/script.lisp
   ```

Isso monta o arquivo no contêiner e o executa.

## Lisp on Docker Compose

Se você quiser montar um volume para a pasta `scripts/` usando **Docker Compose**, pode fazer o seguinte:

---

### 📌 1. Estrutura do Projeto  

```
/lisp
│── docker-compose.yml
│── Dockerfile
└── scripts/
    ├── script.lisp
    ├── outro_script.lisp
```

- A pasta `scripts/` contém os arquivos Lisp que você quer acessar dentro do contêiner.

---

### 📌 2. Criar o `Dockerfile`  

Se você ainda não criou o `Dockerfile`, aqui está um modelo que configura **SBCL + Quicklisp**:

```dockerfile
# Usar imagem base do SBCL
FROM debian:latest

# Instalar dependências
RUN apt-get update && apt-get install -y \
    sbcl \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Baixar e instalar Quicklisp
RUN curl -o /tmp/ql.lisp http://beta.quicklisp.org/quicklisp.lisp && \
    sbcl --no-sysinit --no-userinit --load /tmp/ql.lisp \
         --eval '(quicklisp-quickstart:install :path "~/.quicklisp")' \
         --eval '(ql:add-to-init-file)' \
         --quit && \
    rm /tmp/ql.lisp

# Instalar Quicklisp-Slime-Helper
RUN sbcl --eval '(ql:quickload :quicklisp-slime-helper)' --quit

# Definir diretório de trabalho
WORKDIR /scripts

# Comando padrão: iniciar um REPL do SBCL
CMD ["sbcl"]
```

---

### 📌 3. Criar o `compose.yml`  

Agora, crie um arquivo `compose.yml` na raiz do projeto:

```yaml
services:
  lisp:
    build: .
    volumes:
      - ./scripts:/scripts
    working_dir: /scripts
    command: ["sbcl"]
```

Esse arquivo:
- **Constrói a imagem** usando o `Dockerfile`.
- **Monta a pasta `scripts/`** do host dentro do contêiner no diretório `/lisp`.
- **Define o diretório de trabalho** como `/lisp`, então qualquer arquivo Lisp estará acessível dentro do contêiner.
- **Inicia o SBCL** automaticamente.

---

### 📌 4. Executar o Contêiner  

1️⃣ **Construir e iniciar o contêiner:**  
```sh
docker compose up -d
```
Isso cria o contêiner e o mantém rodando em segundo plano.

2️⃣ **Acessar o SBCL dentro do contêiner:**  
```sh
docker compose exec sii sbcl
```

Agora você pode interagir com o **REPL do SBCL** e acessar os arquivos Lisp na pasta montada.

3️⃣ **Rodar um script Lisp dentro do contêiner:**  
Se houver um arquivo `scripts/script.lisp`, execute:  
```sh
docker compose exec sii sbcl --script "basededatos.lisp"
```

ou

```sh
docker compose exec sii sbcl --noinform --load basededatos.lisp
```

| Modo | Sai do SBCL? | Para quê usar? |
| --- | --------- | ---- |
| --script | ✅ Sim | Executar e sair automaticamente |
| --noinform --load | ❌ Não | Carregar código e continuar no REPL | 

4️⃣ **Acessar um container gerenciado pelo Compose**
```sh
docker compose exec sii sbcl
```

5️⃣ **Executar um script dentro do `sbcl`**
```sbcl
(load "./test.lisp")
```

**Parar e remover os contêineres:**  
```sh
docker compose down
```

