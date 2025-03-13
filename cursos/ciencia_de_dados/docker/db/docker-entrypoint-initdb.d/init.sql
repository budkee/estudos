-- Verificar se o usuário 'postgres' existe, se não, criar
DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT
      FROM   pg_catalog.pg_roles
      WHERE  rolname = 'postgres') THEN

      CREATE ROLE postgres LOGIN SUPERUSER INHERIT CREATEDB CREATEROLE NOREPLICATION;
   END IF;
END
$$;

-- Conectar ao banco de dados teste_financas
\c teste_financas

-- Criar a tabela Crédito
-- CREATE TABLE credito (
--     id SERIAL PRIMARY KEY,
--     data_hora TIMESTAMP NOT NULL,
--     email VARCHAR(255) NOT NULL,
--     whatsapp VARCHAR(20),
--     nome VARCHAR(100) NOT NULL,
--     cpf VARCHAR(11) NOT NULL,
--     valor DECIMAL(10, 2) NOT NULL,
--     parcelas INT NOT NULL,
--     renda DECIMAL(10, 2) NOT NULL,
--     score INT NOT NULL,
--     status VARCHAR(20) NOT NULL
-- );

-- Conectar ao banco de dados prioriza_cg
-- \c prioriza_cg

-- -- Criar a tabela Respostas
-- CREATE TABLE Respostas (
--     id SERIAL PRIMARY KEY,
--     data_hora TIMESTAMP NOT NULL,
--     email VARCHAR(255) NOT NULL,
--     whatsapp VARCHAR(20),
--     bairro VARCHAR(100) NOT NULL,
--     participacao_efetiva_populacao BOOLEAN NOT NULL,
--     areas_sociais TEXT NOT NULL,
--     maiores_problemas TEXT NOT NULL,
--     maiores_prioridades_4_anos TEXT NOT NULL,
--     maiores_problemas_por_area_social TEXT NOT NULL,
--     sugestoes_melhoria_social TEXT NOT NULL,
--     pontos_progresso_bem_estar TEXT NOT NULL,
--     possiveis_contribuicoes TEXT NOT NULL,
--     acoes_em_4_anos TEXT NOT NULL
-- );
