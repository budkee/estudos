# Guia Básico do Bash

## Introdução ao Bash

O Bash (Bourne Again Shell) é um dos interpretadores de comandos mais populares em sistemas Unix e Linux. Ele permite a execução de comandos, scripts e automação de tarefas.

### Comandos Básicos

- `ls`: Lista arquivos e diretórios.
- `cd`: Navega entre diretórios.
- `pwd`: Exibe o diretório atual.
- `mkdir`: Cria um novo diretório.
- `rm`: Remove arquivos ou diretórios.
- `cp`: Copia arquivos ou diretórios.
- `mv`: Move ou renomeia arquivos/diretórios.

### Variáveis

```bash
# Definir uma variável
NOME="Mundo"
echo "Olá, $NOME"
```

### Estruturas de Controle

```bash
# Condicional
if [ -f arquivo.txt ]; then
    echo "O arquivo existe."
fi

# Loop
for i in {1..5}; do
    echo "Número $i"
done
```

---

## Diferença entre Bash e Zsh

Embora o Bash e o Zsh sejam shells populares, eles possuem diferenças importantes:

| Característica         | Bash                          | Zsh                          |
|------------------------|-------------------------------|------------------------------|
| Popularidade           | Mais amplamente utilizado.    | Menos comum, mas crescente.  |
| Autocompletar          | Básico.                       | Mais avançado e personalizável. |
| Plugins e Temas        | Suporte limitado.             | Suporte nativo com Oh-My-Zsh. |
| Configuração           | `.bashrc`, `.bash_profile`.   | `.zshrc`.                    |
| Recursos Extras        | Menos recursos embutidos.     | Recursos como globbing avançado. |

---

## Bash-it

O Bash-it é uma coleção de scripts, aliases e funções que ajudam a personalizar e melhorar o uso do Bash. Ele também suporta temas para personalizar o prompt.

### Instalação

1. Clone o repositório:
     ```bash
     git clone --depth=1 https://github.com/Bash-it/bash-it.git ~/.bash_it
     ```
2. Execute o script de instalação:
     ```bash
     ~/.bash_it/install.sh
     ```

### Ativando Temas

Após instalar o Bash-it, você pode ativar temas para personalizar o prompt. Edite o arquivo `~/.bashrc` e defina o tema:
```bash
export BASH_IT_THEME='bobby'
```

### Lista de Temas

Confira a lista completa de temas no [site oficial do Bash-it](https://bash-it.readthedocs.io/en/latest/themes-list/#list-of-themes).

---

## Conclusão

O Bash é uma ferramenta poderosa para desenvolvedores e administradores de sistemas. Com o Bash-it, você pode personalizar sua experiência e torná-la mais produtiva. Explore os temas e plugins para adaptar o shell às suas necessidades.
