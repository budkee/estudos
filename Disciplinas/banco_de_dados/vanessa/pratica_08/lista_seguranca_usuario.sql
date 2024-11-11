--1. Conectar-se ao PostgreSQL com o usuário postgres. Abra o terminal e faça login no PostgreSQL usando o comando abaixo:
docker ps
docker exec -it <container_id_or_name> /bin/bash
psql -h localhost -p 5432 -d postgres -U postgres

--[POSTGRES] 
--Criar um banco de dados chamado aulabd
CREATE DATABASE aulabd;

--[POSTGRES] 
--Liste todos os bancos de dados para confirmar a criação:
\l

--[POSTGRES] 
-- Conectar-se ao banco de dados aulabd
\c aulabd

--[POSTGRES] 
--Crie a tabela catalogo com as colunas id, nome, local, preco, e responsavel:
CREATE TABLE public.catalogo (
    id INTEGER PRIMARY KEY, 
    nome VARCHAR(255), 
    local VARCHAR(255), 
    preco NUMERIC(10,2) DEFAULT 0.00, 
    responsavel VARCHAR(255) DEFAULT 'sessao_usuario'
);

--[POSTGRES] 
--2. Criar o usuário/papel usuarioaluno. Crie um papel bdaluno com login, senha, e permissões para criar bancos de dados e papéis:
-- RESPOSTA AQUI **************
CREATE USER usuarioaluno WITH PASSWORD 'passada';
CREATE ROLE bdaluno WITH LOGIN PASSWORD 'tode' CREATEDB CREATEROLE;
GRANT bdaluno TO usuarioaluno;

--[POSTGRES] 
--	Verifique os papéis e suas permissões:
\du

--[USUARIOALUNO]
psql -h localhost -p 5432 -d postgres -U usuarioaluno

--[USUARIOALUNO]
--	Realize uma consulta na tabela catalogo para verificar o acesso:
SELECT * FROM catalogo;

--[POSTGRES] 
-- Conceder a permissao de select a tabela catalogo ao bdaluno
-- RESPOSTA AQUI **************
GRANT SELECT ON TABLE catalogo TO bdaluno;

--[USUARIOALUNO]
--Insira uma nova linha na tabela catalogo:
INSERT INTO catalogo (id, nome, local) VALUES (1, 'nome1', 'local1');
INSERT INTO catalogo (id, nome, local) VALUES (2, 'nome2', 'local2');

--[POSTGRES] 
-- Conceder a permissao de insert a tabela catalogo ao bdaluno
-- RESPOSTA AQUI **************
GRANT INSERT ON TABLE catalogo TO bdaluno;

--[POSTGRES] 
--Revogue todos os privilégios de usuarioaluno na tabela catalogo:
-- RESPOSTA AQUI **************
REVOKE ALL PRIVILEGES ON catalogo FROM usuarioaluno;

--[POSTGRES] 
--Remova o usuário usuarioaluno do sistema:
-- RESPOSTA AQUI **************
DROP USER usuarioaluno;