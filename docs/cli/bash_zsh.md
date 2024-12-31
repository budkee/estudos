# Guia sobre manipulação de arquivos no Linux** focado em permissões, meios de execução, e conceitos essenciais para automação com scripts shell.

Este guia trata sobre manipulação de arquivos no Linux focado em **permissões**, **meios de execução**, e conceitos essenciais para **automação com scripts shell**.

## 1. **Permissões de Arquivo no Linux**

### 1.1 Tipos de Permissões
Cada arquivo ou diretório no Linux tem três tipos principais de permissões:
- **Leitura (r)**: Permite ler o conteúdo do arquivo ou listar o conteúdo do diretório.
- **Escrita (w)**: Permite modificar o arquivo ou adicionar/excluir arquivos dentro de um diretório.
- **Execução (x)**: Permite executar um arquivo (útil para scripts) ou acessar um diretório.

Essas permissões são atribuídas a três categorias:
1. **Dono (user)**: O proprietário do arquivo.
2. **Grupo (group)**: Um grupo de usuários que possuem permissões para o arquivo.
3. **Outros (others)**: Todos os outros usuários.

### 1.2 Exibindo Permissões de Arquivos
Use o comando `ls -l` para exibir as permissões de arquivos e diretórios:

```bash
ls -l
```

Saída de exemplo:

```bash
-rwxr-xr--
```

- O primeiro caractere define o tipo (ex: `-` para arquivo comum, `d` para diretório).
- Os próximos três caracteres definem as permissões para o dono, o grupo e os outros, respectivamente.

### 1.3 Modificando Permissões: `chmod`
Use o comando `chmod` para alterar permissões.

#### Modificar Permissões com Notação Simbólica
Exemplo: Dando permissão de execução ao dono:
```bash
chmod u+x script.sh
```
- `u`: Dono (user)
- `g`: Grupo (group)
- `o`: Outros (others)
- `+x`: Adicionar permissão de execução.

#### Modificar Permissões com Notação Numérica
Cada permissão é representada por um valor numérico:
- `4`: Leitura (r)
- `2`: Escrita (w)
- `1`: Execução (x)

Para definir permissões, você soma os números. Exemplo: Para definir permissão de leitura, escrita e execução para o dono, leitura e execução para o grupo, e nenhuma permissão para outros:

```bash
chmod 750 script.sh
```
Isso equivale a:
- Dono: `rwx` (7 = 4+2+1)
- Grupo: `r-x` (5 = 4+1)
- Outros: `---` (0)

## 2. **Gerenciamento de Propriedade com `chown` e `chgrp`**

### 2.1 Alterando o Dono: `chown`
Use o comando `chown` para alterar o dono de um arquivo.

Exemplo: Alterar o dono do arquivo para o usuário `username`:
```bash
chown username arquivo.txt
```

### 2.2 Alterando o Grupo: `chgrp`
Use o comando `chgrp` para alterar o grupo de um arquivo.

Exemplo: Alterar o grupo do arquivo para o grupo `groupname`:
```bash
chgrp groupname arquivo.txt
```

### 2.3 Alterar Dono e Grupo ao Mesmo Tempo:
```bash
chown username:groupname arquivo.txt
```

## 3. **Execução de Scripts Shell**

### 3.1 Criando e Executando um Script Shell

#### Passo 1: Criar um arquivo de script
Use um editor de texto como `nano`, `vim` ou `gedit` para criar um script:

```bash
nano script.sh
```

#### Passo 2: Escrever o script
Todo script shell começa com a "shebang", que especifica qual interpretador usar:

```bash
#!/bin/bash
echo "Hello, world!"
```

#### Passo 3: Tornar o script executável
Para executar o script, ele deve ter permissão de execução:

```bash
chmod +x script.sh
```

#### Passo 4: Executar o script
Execute o script usando:

```bash
./script.sh
```

### 3.2 Executando Scripts sem Permissão de Execução
Você pode executar scripts sem dar permissão de execução, chamando o interpretador diretamente:

```bash
bash script.sh
```

### 3.3 Execução de Scripts na Inicialização
Para executar um script automaticamente na inicialização do sistema, você pode adicionar seu caminho ao arquivo `crontab` com o agendamento correto.

Exemplo para rodar um script no boot:
```bash
@reboot /caminho/do/script.sh
```

Para editar o `crontab`:
```bash
crontab -e
```

## 4. **Redirecionamento de Entrada/Saída**

### 4.1 Redirecionando Saída para Arquivo
Use o símbolo `>` para redirecionar a saída de um comando para um arquivo (sobrescrevendo o arquivo):
```bash
echo "texto" > arquivo.txt
```

Use `>>` para adicionar ao conteúdo existente sem sobrescrever:
```bash
echo "novo texto" >> arquivo.txt
```

### 4.2 Redirecionando Erros para Arquivo
Para redirecionar a saída de erro (stderr), use `2>`:
```bash
comando_invalido 2> erros.txt
```

### 4.3 Redirecionando Entrada
Você pode usar `<` para redirecionar a entrada de um arquivo:
```bash
cat < arquivo.txt
```

### 4.4 Redirecionamento de Saída e Erros Simultaneamente
Para redirecionar tanto a saída padrão (stdout) quanto erros (stderr):
```bash
comando > saida.txt 2>&1
```

## 5. **Automatizando Tarefas com `cron`**

O `cron` permite agendar scripts para execução periódica. Para adicionar uma tarefa cron, use o comando:

```bash
crontab -e
```

Adicione uma linha com a seguinte sintaxe:
```
* * * * * /caminho/do/script.sh
```

Cada asterisco representa um parâmetro:
- **Minuto** (0-59)
- **Hora** (0-23)
- **Dia do mês** (1-31)
- **Mês** (1-12)
- **Dia da semana** (0-6, Domingo é 0)

Por exemplo, para executar o script todos os dias às 3h da manhã:
```bash
0 3 * * * /caminho/do/script.sh
```

## 6. **Verificando e Matando Processos**

### 6.1 Verificando Processos em Execução: `ps`
Use `ps` para listar os processos em execução:

```bash
ps aux
```

### 6.2 Matando Processos: `kill`
Use `kill` seguido do PID (Process ID) para encerrar um processo:

```bash
kill 1234
```

Para forçar o encerramento:
```bash
kill -9 1234
```
