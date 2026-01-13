# Git

O Git é uma ferramenta de versionamento de código onde é possível você realizar as alterações no seu código e salvá-las logo após o fechamento de um dia de trabalho, por exemplo. Uma cena que constantemente vemos em algumas máquinas de usuários que permeiam que escrevem com o Word instalado localmente é a seguinte:

![arquivo_final-arquivo_final(1)-arquivo_final(2)]()

Após enviar uma versão ao revisor, o usuário realiza as alterações e salva o arquivo novamente para enviar. Entre os problemas de manter esse sistema, nota-se (i) um alto consumo da memória do hospedeiro, (ii) ...

Com poucos comandos você pode verificar como está o status do seu repositório - *git status* -, adicionar o estado dos arquivos alterados ao longo do tempo - *git add .* e enviar essas novas alterações no servidor(?) - *git commit -m "Sobre as alterações do dia"*.

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
