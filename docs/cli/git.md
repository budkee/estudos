# Git

Muito se fala dessa palavra Git, mas você sabe o que ela é e faz de fato? Hoje a gente vai falar um pouco mais sobre.

## O que é?

O Git é uma ferramenta de versionamento de código onde é possível você realizar as alterações no seu código e salvá-las logo após o fechamento de um dia de trabalho, por exemplo. Com poucos comandos você pode verificar como está o status do seu repositório - *git status* -, adicionar o estado dos arquivos alterados ao longo do tempo - *git add .* e enviar essas novas alterações no servidor(?) - *git commit -m "Sobre as alterações do dia"*.

## Adicionando uma URL remota em um repositório local

Muitas vezes você pode se deparar com a situação de ter desenvolvido seu código local mas não sabe como pode subir em um repositório remoto. No git podemos tentar fazer o seguinte:

```bash
git remote add origin <url-remota>
```

Entretanto, se você já esta dentro de um repositório você pode encontrar o seguinte retorno:

```bash
error: remote origin already exists.
```

Para esse tipo de situação, devemos alterar com o seguinte comando:

```bash
git remote set-url origin https://novo-repositorio.git
```

## Outras leituras

- [Git Flow](git_flow.md)
- [GitHub e GitHub Actions](actions_github.md)
- [Cheatsheet | Git by Heroku](./pdf/SF_git_cheatsheet.pdf)
