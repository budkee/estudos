-- DATABASES

CREATE DATABASE db_data;
CREATE DATABASE db_newsletter;

-- -- Verifica e cria o banco de dados db_django se não existir
-- DO $$ BEGIN
--     IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'db_django') THEN
--         CREATE DATABASE db_django;
--     END IF;
-- END $$;

-- -- Verifica e cria o banco de dados db_users se não existir
-- DO $$ BEGIN
--     IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'db_users') THEN
--         CREATE DATABASE db_users;
--     END IF;
-- END $$;

-- -- Verifica e cria o banco de dados db_weather se não existir
-- DO $$ BEGIN
--     IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'db_weather') THEN
--         CREATE DATABASE db_weather;
--     END IF;
-- END $$;


-- -- Tabela 'users'
-- CREATE TABLE users (
--     id SERIAL PRIMARY KEY,
--     email VARCHAR(254) UNIQUE NOT NULL,
--     frequency VARCHAR(10) NOT NULL
-- );

-- -- Tabela 'localizacao'
-- CREATE TABLE localizacao (
--     id SERIAL PRIMARY KEY,
--     nome VARCHAR(255) NOT NULL,
--     latitude DOUBLE PRECISION NOT NULL,
--     longitude DOUBLE PRECISION NOT NULL
-- );

-- -- Tabela 'condicoes_climaticas'
-- CREATE TABLE condicoes_climaticas (
--     id SERIAL PRIMARY KEY,
--     localizacao_id INTEGER REFERENCES localizacao(id) ON DELETE CASCADE,
--     data_hora TIMESTAMP WITHOUT TIME ZONE NOT NULL,
--     descricao_weather VARCHAR(255) NOT NULL,
--     temperatura_atual DOUBLE PRECISION NOT NULL,
--     temperatura_max DOUBLE PRECISION NOT NULL,
--     temperatura_min DOUBLE PRECISION NOT NULL,
--     umidade DOUBLE PRECISION NOT NULL,
--     velocidade_vento DOUBLE PRECISION NOT NULL,
--     direcao_vento DOUBLE PRECISION NOT NULL,
--     rajada_vento DOUBLE PRECISION
-- );

-- -- Inserir dados de teste na tabela users
-- INSERT INTO users (email, frequency) VALUES
-- ('kae.budke@gmail.com', 'weekly'),
-- ('kae.budke@ufms.br', 'biweekly');
