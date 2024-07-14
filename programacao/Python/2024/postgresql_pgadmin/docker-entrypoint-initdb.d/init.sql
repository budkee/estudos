-- Criar a tabela de usuários (users)
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT NOT NULL
);

-- Inserir dados de teste na tabela users
INSERT INTO users (name, email, age) VALUES
('Alice Smith', 'alice.smith@example.com', 30),
('Bob Johnson', 'bob.johnson@example.com', 25),
('Charlie Brown', 'charlie.brown@example.com', 35);
