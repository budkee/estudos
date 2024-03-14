# Python

Python é uma linguagem de programação amplamente utilizada e popular devido à sua simplicidade e legibilidade de código. É uma ótima escolha para iniciantes que desejam aprender a programar.

Existem muitos recursos online disponíveis para ajudar a aprender Python e praticar suas habilidades. Alguns dos principais sites para prática são:

- [**Codecademy**](www.codecademy.com): Oferece cursos interativos de Python, desde o básico até tópicos mais avançados, com exercícios práticos para testar seus conhecimentos.

- [**HackerRank**](www.hackerrank.com): Plataforma focada em desafios de programação, oferecendo uma ampla variedade de problemas em Python para você resolver e melhorar suas habilidades.

- [**Exercism**](www.exercism.io): Oferece uma abordagem mais prática para aprender Python, fornecendo uma série de exercícios para resolver, além de feedback e discussões com a comunidade.

- [**LeetCode**](leetcode.com): Similar ao HackerRank, o LeetCode também oferece uma variedade de desafios de programação em Python para você praticar.

## Desenvolvimento de Aplicações com um Servidor

Além de aprender Python em sites de prática, você também pode explorar o desenvolvimento de aplicações usando um servidor. Aqui estão algumas opções populares:

- [**Django**](www.djangoproject.com): Um framework poderoso e completo para desenvolvimento web em Python. Com o Django, você pode criar aplicações web robustas e escaláveis.

- [**Flask**](flask.pocoo.org): Um microframework leve e flexível para desenvolvimento web em Python. É mais simples que o Django, mas ainda permite criar aplicativos web eficientes.

- [**Bottle**](bottlepy.org): Outro microframework para desenvolvimento web em Python, com um foco em simplicidade e facilidade de uso.

Essas são apenas algumas opções disponíveis para desenvolvimento com Python. Cada uma tem suas características e recursos específicos, portanto, escolha a que melhor se adapte às suas necessidades e preferências.

## Guia Rápido para Programar Utilizando um Ambiente Virtual

Este guia tem como objetivo fornecer uma visão geral dos passos necessários para programar utilizando um ambiente virtual. Um ambiente virtual é uma maneira de isolar e gerenciar as dependências do seu projeto, permitindo que você mantenha diferentes versões de bibliotecas e evite conflitos entre elas. Ele é especialmente útil quando você está trabalhando em vários projetos simultaneamente.

### Pré-requisitos
- Python instalado no seu computador

### Passos

1. **Instalar o pacote `virtualenv`**: Abra o terminal e execute o seguinte comando para instalar o pacote `virtualenv`:

   ```
   $ pip install virtualenv
   ```

2. **Criar um novo ambiente virtual**: No terminal, navegue até a pasta raiz do seu projeto e execute o seguinte comando para criar um novo ambiente virtual:

   ```
   $ virtualenv nome_do_ambiente_virtual
   ```

3. **Ativar o ambiente virtual**: No terminal, execute o seguinte comando para ativar o ambiente virtual:

   - No Windows:

     ```
     $ nome_do_ambiente_virtual\Scripts\activate
     ```

   - No macOS ou Linux:

     ```
     $ source nome_do_ambiente_virtual/bin/activate
     ```

4. **Instalar as dependências do projeto**: Com o ambiente virtual ativado, você pode instalar todas as dependências do seu projeto utilizando o gerenciador de pacotes `pip`. Execute o seguinte comando para instalar as dependências listadas em um arquivo `requirements.txt`:

   ```
   $ pip install -r requirements.txt
   ```

5. **Desativar o ambiente virtual**: Quando você terminar de trabalhar no projeto, você pode desativar o ambiente virtual executando o seguinte comando no terminal:

   ```
   $ deactivate
   ```

Agora você pode programar utilizando o ambiente virtual isolado, garantindo que todas as bibliotecas e dependências estejam corretamente gerenciadas. Certifique-se de ativar o ambiente virtual sempre que estiver trabalhando no projeto e atualizar as dependências conforme necessário.


## Links e Referências

- [Documentação | Python Org](https://docs.python.org/pt-br/3/)
- [Roadmap | Dev Python](https://roadmap.sh/python)
- [Documentação | Requests](https://requests.readthedocs.io/en/latest/user/install/)
