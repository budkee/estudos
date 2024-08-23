# Coleta de dados da API Web do Spotify

## Sobre

A API Web do Spotify permite a criação de aplicativos que podem interagir com o serviço de streaming do Spotify, fornecendo as seguintes atividades:

- Recuperação de metadados de conteúdo
- Captura de recomendações
- Criação e gerenciamento de playlists
- Controle da reprodução

O objetivo deste projeto é realizar a comunicação com a API, coletar 100 tuplas do Spotify e armazenar os dados no banco de dados PostgreSQL (>=12). Para atingir este objetivo, é necessário (i) realizar o diagrama entidade relacionamento e mapeamento relacional dos 12 endpoints existentes na documentação. Em seguida, (ii) o código da aplicação deverá solicitar da API 100 tuplas de pelo menos uma das endpoints 

## Entregas

- [Diagrama Entidade Relacionamento | PDF]()
- [DUMP do Banco de Dados | dump.sql]()
- [Código de Coleta | load_spotify.sql]()
- [Apresentação da Aplicação | 10 min | Restrito]()

## Brincando com a API 

Para conhecer um pouco mais sobre como funciona a interface e brincar um pouco fazendo algumas requisições, podemos fazê-lo utilizando [[1]](https://developer.spotify.com/documentation/web-api/tutorials/getting-started) `cURL`, realizando os  testes pela Linha de Comando (CLI), ou [[2]](https://www.postman.com/) através do Postman que proporciona um ambiente de testes com uma interface amigável para visualização de respostas das requisições.

### Passo a passo com o Postman

1. Com a conta criada no Spotify, entre na [área para Desenvolvedores](https://developer.spotify.com/), clique no seu usuário no canto superior direito e selecione `Dashboard`.

2. Crie um novo aplicativo e preencha o formulário de modo sucinto para que eles liberem o ID do Cliente da sua Aplicação. Um exemplo de preenchimento pode ser: 
    - App name: Brincando com a API
    - App description: Testando a API
    - Website: http://localhost:3000
    - Redirect URIs: http://localhost:3000
    - APIs used: `Web API`
Deixe os campos `Bundle IDs` e `Android Packages` em branco.

3. Com o aplicativo criado e o ID em mãos, podemos solicitar um novo token de acesso por meio do Postman. Para isso, [crie uma conta no Postman](https://identity.getpostman.com/login) e crie um novo `Blank Workspace`, dando um nome para o espaço de trabalho - aqui será `Brincando com a API` - e selecione o tipo de exposição que você deseja a esse espaço (`Personal`, `Team` ou `Public`) - nesse caso eu coloquei como [público](https://www.postman.com/docking-module-cosmologist-39725675/workspace/brincando-com-a-api/overview), porém é recomendado colocar como `Personal` ou em `Team`.

4. No espaço de trabalho, selecione `New HTTP Request`. Por padrão o Postman te apresenta o `GET` em verde seguido de um input para a URL, porém, como queremos solicitar o token de acesso ao spotify, vamos selecionar o `POST` e adicionar a URL `https://accounts.spotify.com/api/token`. Além disso, temos que passar alguns parâmetros e uma configuração no cabeçalho da requisição. Em `Params`, a partir da segunda linha da chave `Key` e valor `Value`, complete com os seguintes dados: 
    
    - grant_type: client_credentials
    - client_id: <seu_client_id>
    - client_secret: <seu_client_secret>

Em `Headers`, preencha com:

    - Content-Type: application/x-www-form-urlencoded

5. Salve a requisição em uma nova coleção, caso já não tenha criado, para facilitar futuras solicitações de tokens. Clique em enviar `Send` e a resposta deverá retornar um arquivo em `json` com este formato, porém com uma string de token diferente:

    {
        "access_token": "BQDBKJ5eo5jxbtpWjVOj7ryS84khybFpP_lTqzV7uV-T_m0cTfwvdn5BnBSKPxKgEb11",
        "token_type": "Bearer",
        "expires_in": 3600
    }

O token será válido por apenas 1 hora.

6. Agora com o token em mãos, podemos solicitar dados dos endpoints de interesse. Vamos consumir a endpoint que nos retorna alguns dos álbuns de Kali Uchis, Puro Suco e Anitta. Para isso devemos ter em mãos (i) a URL de acesso global para pegar diversos álbuns `https://api.spotify.com/v1/albums` e (ii) o id dos álbuns dos artistas, retirado a partir do link de compartilhamento do álbum:

    - [Red Moon In Venus | Kali Uchis](https://open.spotify.com/intl-pt/album/5OZ44LaqZbpP3m9B3oT8br?si=9DnVTClvR26v_rigMCeUUA): `5OZ44LaqZbpP3m9B3oT8br`
    - [Cacau | Puro Suco](https://open.spotify.com/intl-pt/album/7hLXr1YD7DGY8c1A5zWPmo?si=v69nb2IIRbG7MU22g64OhA): `7hLXr1YD7DGY8c1A5zWPmo`
    - [Funk Generation | Anitta](https://open.spotify.com/intl-pt/album/6z6VObudfoxrvGNC5MtiTY?si=IzpPOCceStWpmC9HQiSdLQ): `6z6VObudfoxrvGNC5MtiTY`

7. De volta ao Postman, crie uma nova requisição `New HTTP Request`, mas dessa vez para `GET`. Cole o endpoint (https://api.spotify.com/v1/albums) no input da URL e siga para aba de parâmetros. Nesta, adicione as chaves `ids` e `market` com os valores `5OZ44LaqZbpP3m9B3oT8br,7hLXr1YD7DGY8c1A5zWPmo,6z6VObudfoxrvGNC5MtiTY` e `BR`, respectivamente. Na aba de autorização `Authorization`, selecione o tipo `Type` como `Bearer Token` e cole o token de acesso do passo 5. Salve na coleção do Spotify e envie a requisição. 

## Links e Referências

- [Descrição do trabalho de Laboratório de Banco de Dados](TR___TRABALHO_PRÁTICO_LBD_2024.pdf)
- [Documentação da API Web | Spotify Developer](https://developer.spotify.com/documentation/web-api)