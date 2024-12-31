### Tutorial de Iniciantes sobre Jekyll e Gems

#### O que é o Jekyll?

O **Jekyll** é um gerador de sites estáticos escrito em Ruby que permite criar sites rápidos, seguros e fáceis de manter. Ele converte templates Markdown ou Liquid em páginas HTML estáticas, o que é ideal para blogs, portfólios e até landing pages. Por ser um sistema de site estático, não depende de um banco de dados, tornando o processo mais simples e com menos manutenção.

#### O que são Gems no contexto do Jekyll?

**Gems** são bibliotecas ou pacotes reutilizáveis no ambiente Ruby. No contexto do Jekyll, elas servem para adicionar funcionalidades ao site, como plugins, temas e integrações com outras ferramentas. O Jekyll, em si, é distribuído como uma Gem, e você pode usar outras Gems para estender suas capacidades.

#### Como instalar o Jekyll?

Para começar a usar o Jekyll, você precisa de Ruby instalado no seu sistema.

1. **Instalar Ruby** (se ainda não tiver):
   - No Linux (Ubuntu):
     ```bash
     sudo apt-get install ruby-full build-essential zlib1g-dev
     ```
   - No macOS:
     ```bash
     brew install ruby
     ```
   - No Windows, pode-se usar o [RubyInstaller](https://rubyinstaller.org/).

2. **Configurar seu ambiente**:
   Adicione as seguintes linhas ao seu arquivo `.bashrc` ou `.zshrc` (no Linux/macOS):
   ```bash
   export GEM_HOME="$HOME/gems"
   export PATH="$HOME/gems/bin:$PATH"
   ```

3. **Instalar o Jekyll e Bundler**:
   O Bundler é uma ferramenta que ajuda a gerenciar dependências Ruby (Gems).
   ```bash
   gem install jekyll bundler
   ```

#### Criando seu primeiro site com Jekyll

Agora que o Jekyll está instalado, você pode criar seu primeiro site:

1. **Gerar o site**:
   ```bash
   jekyll new nome-do-seu-site
   ```

2. **Entrar no diretório do site**:
   ```bash
   cd nome-do-seu-site
   ```

3. **Executar o servidor local**:
   ```bash
   bundle exec jekyll serve
   ```

O comando acima iniciará um servidor local, e o site estará disponível em `http://localhost:4000`.

#### Estrutura do projeto Jekyll

Ao criar um novo site com o Jekyll, ele gera uma estrutura de diretórios similar à seguinte:

- **_config.yml**: O arquivo de configuração principal. Aqui você define o título do site, informações do autor, plugins e configurações de tema.
- **_posts/**: Diretório onde os posts do blog são armazenados. Cada arquivo deve ser nomeado no formato `YYYY-MM-DD-titulo-do-post.md`.
- **_layouts/**: Arquivos de layout que definem a estrutura do site. Por exemplo, pode ter um layout para o blog e outro para as páginas estáticas.
- **_includes/**: Trechos de código que podem ser reutilizados em diferentes partes do site.
- **_sass/**: Estilos CSS usando Sass.
- **assets/**: Imagens, arquivos JavaScript, e outros recursos estáticos.

#### Usando Gems no Jekyll

Você pode estender o Jekyll com plugins, que são Gems específicas. Por exemplo, se você quiser adicionar suporte a SEO, pode usar a Gem `jekyll-seo-tag`.

1. **Adicione a Gem ao Gemfile**:
   No arquivo `Gemfile`, você pode adicionar Gems como:
   ```ruby
   gem "jekyll-seo-tag"
   ```

2. **Instale a Gem**:
   Após adicionar a Gem ao Gemfile, execute o comando:
   ```bash
   bundle install
   ```

3. **Ativar o plugin no _config.yml**:
   No arquivo `_config.yml`, adicione o plugin à lista:
   ```yaml
   plugins:
     - jekyll-seo-tag
   ```

Agora, o plugin `jekyll-seo-tag` está ativo e adicionará tags SEO às suas páginas automaticamente.

#### Temas do Jekyll

Os temas são outra forma de Gems no Jekyll. Eles permitem que você aplique um design predefinido ao seu site com pouca customização.

1. **Instalar um tema**:
   Encontre um tema Jekyll no [Jekyll Themes](https://jekyllthemes.io/) ou [GitHub Pages Themes](https://pages.github.com/themes/).
   
   No `Gemfile`, adicione o tema:
   ```ruby
   gem "minima", "~> 2.5"
   ```

2. **Aplicar o tema**:
   No arquivo `_config.yml`, defina o tema:
   ```yaml
   theme: minima
   ```

3. **Instalar o tema**:
   Execute o comando:
   ```bash
   bundle install
   ```

Agora, seu site Jekyll usará o tema que você escolheu.

#### Publicando o site

Uma vez que o site esteja pronto, você pode publicá-lo em várias plataformas. O GitHub Pages, por exemplo, é uma escolha popular por ser gratuito e fácil de integrar com o Jekyll.

1. **Subir para o GitHub Pages**:
   1. Crie um repositório no GitHub.
   2. Faça o push do código do seu site para esse repositório.
   3. No GitHub, vá em "Configurações" e habilite o GitHub Pages na aba "Pages", escolhendo o branch correto para publicar.

#### Conclusão

O Jekyll é uma excelente ferramenta para criar sites rápidos e simples, sem a complexidade de um CMS tradicional. Usando Gems, você pode estender as funcionalidades do Jekyll de acordo com suas necessidades, seja com temas, plugins de SEO, ou outras integrações.

#### Referências

- [Documentação Oficial do Jekyll](https://jekyllrb.com/)
- [Ruby Gems - Página Oficial](https://rubygems.org/)
- [Jekyll SEO Tag Plugin](https://github.com/jekyll/jekyll-seo-tag)
- [GitHub Pages com Jekyll](https://pages.github.com/)