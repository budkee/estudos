-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql_server:3306
-- Tempo de geração: 03/04/2024 às 01:46
-- Versão do servidor: 8.3.0
-- Versão do PHP: 8.2.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `default_schema`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `album`
--

CREATE TABLE `album` (
  `id` int NOT NULL,
  `titulo` varchar(256) NOT NULL,
  `data` date NOT NULL,
  `formato` varchar(16) NOT NULL,
  `produtor_cpf` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `album_musica`
--

CREATE TABLE `album_musica` (
  `album_id` int NOT NULL,
  `musica_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `endereco`
--

CREATE TABLE `endereco` (
  `endereco_id` int NOT NULL,
  `telefone` varchar(32) NOT NULL,
  `cep` varchar(8) NOT NULL,
  `logradouro` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `endereco`
--

INSERT INTO `endereco` (`endereco_id`, `telefone`, `cep`, `logradouro`) VALUES
(1, '2123326767', '1828836', 'Rua alecrim dourado'),
(2, '2123326767', '21233267', '2123326767');

-- --------------------------------------------------------

--
-- Estrutura para tabela `instrumento`
--

CREATE TABLE `instrumento` (
  `nome` varchar(256) NOT NULL,
  `tom` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `interpreta`
--

CREATE TABLE `interpreta` (
  `musico_cpf` varchar(14) NOT NULL,
  `musica_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `musica`
--

CREATE TABLE `musica` (
  `musica_id` int NOT NULL,
  `titulo` varchar(256) NOT NULL,
  `autor_cpf` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `musica_instrumento`
--

CREATE TABLE `musica_instrumento` (
  `instrumento_nome` varchar(256) NOT NULL,
  `instrumento_tom` varchar(8) NOT NULL,
  `musica_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `musico`
--

CREATE TABLE `musico` (
  `cpf` varchar(14) NOT NULL,
  `nome` varchar(256) NOT NULL,
  `telefone` varchar(32) NOT NULL,
  `endereco_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `musico`
--

INSERT INTO `musico` (`cpf`, `nome`, `telefone`, `endereco_id`) VALUES
('12332198780', '2123326768', '77667266365', 1),
('12332198789', 'Jefferson', '77667266365', 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `participa_musica`
--

CREATE TABLE `participa_musica` (
  `musico_cpf` varchar(14) NOT NULL,
  `musica_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `toca`
--

CREATE TABLE `toca` (
  `instrumento_nome` varchar(256) NOT NULL,
  `instrumento_tom` varchar(8) NOT NULL,
  `musico_cpf` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `album`
--
ALTER TABLE `album`
  ADD PRIMARY KEY (`id`),
  ADD KEY `produtor_cpf` (`produtor_cpf`);

--
-- Índices de tabela `album_musica`
--
ALTER TABLE `album_musica`
  ADD KEY `album_id` (`album_id`),
  ADD KEY `musica_id` (`musica_id`);

--
-- Índices de tabela `endereco`
--
ALTER TABLE `endereco`
  ADD PRIMARY KEY (`endereco_id`);

--
-- Índices de tabela `instrumento`
--
ALTER TABLE `instrumento`
  ADD PRIMARY KEY (`nome`,`tom`);

--
-- Índices de tabela `interpreta`
--
ALTER TABLE `interpreta`
  ADD KEY `musica_id` (`musica_id`),
  ADD KEY `musico_cpf` (`musico_cpf`);

--
-- Índices de tabela `musica`
--
ALTER TABLE `musica`
  ADD PRIMARY KEY (`musica_id`),
  ADD KEY `autor_cpf` (`autor_cpf`);

--
-- Índices de tabela `musica_instrumento`
--
ALTER TABLE `musica_instrumento`
  ADD KEY `musica_id` (`musica_id`),
  ADD KEY `instrumento_nome` (`instrumento_nome`,`instrumento_tom`);

--
-- Índices de tabela `musico`
--
ALTER TABLE `musico`
  ADD PRIMARY KEY (`cpf`),
  ADD KEY `endereco_id` (`endereco_id`);

--
-- Índices de tabela `participa_musica`
--
ALTER TABLE `participa_musica`
  ADD KEY `musica_id` (`musica_id`),
  ADD KEY `musico_cpf` (`musico_cpf`);

--
-- Índices de tabela `toca`
--
ALTER TABLE `toca`
  ADD KEY `musico_cpf` (`musico_cpf`),
  ADD KEY `instrumento_nome` (`instrumento_nome`,`instrumento_tom`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `album`
--
ALTER TABLE `album`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `endereco`
--
ALTER TABLE `endereco`
  MODIFY `endereco_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `musica`
--
ALTER TABLE `musica`
  MODIFY `musica_id` int NOT NULL AUTO_INCREMENT;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `album`
--
ALTER TABLE `album`
  ADD CONSTRAINT `album_ibfk_1` FOREIGN KEY (`produtor_cpf`) REFERENCES `musico` (`cpf`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Restrições para tabelas `album_musica`
--
ALTER TABLE `album_musica`
  ADD CONSTRAINT `album_musica_ibfk_1` FOREIGN KEY (`album_id`) REFERENCES `album` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `album_musica_ibfk_2` FOREIGN KEY (`musica_id`) REFERENCES `musica` (`musica_id`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Restrições para tabelas `interpreta`
--
ALTER TABLE `interpreta`
  ADD CONSTRAINT `interpreta_ibfk_1` FOREIGN KEY (`musica_id`) REFERENCES `musica` (`musica_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `interpreta_ibfk_2` FOREIGN KEY (`musico_cpf`) REFERENCES `musico` (`cpf`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Restrições para tabelas `musica`
--
ALTER TABLE `musica`
  ADD CONSTRAINT `musica_ibfk_1` FOREIGN KEY (`autor_cpf`) REFERENCES `musico` (`cpf`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Restrições para tabelas `musica_instrumento`
--
ALTER TABLE `musica_instrumento`
  ADD CONSTRAINT `musica_instrumento_ibfk_1` FOREIGN KEY (`musica_id`) REFERENCES `musica` (`musica_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `musica_instrumento_ibfk_2` FOREIGN KEY (`instrumento_nome`,`instrumento_tom`) REFERENCES `instrumento` (`nome`, `tom`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Restrições para tabelas `musico`
--
ALTER TABLE `musico`
  ADD CONSTRAINT `musico_ibfk_1` FOREIGN KEY (`endereco_id`) REFERENCES `endereco` (`endereco_id`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Restrições para tabelas `participa_musica`
--
ALTER TABLE `participa_musica`
  ADD CONSTRAINT `participa_musica_ibfk_1` FOREIGN KEY (`musica_id`) REFERENCES `musica` (`musica_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `participa_musica_ibfk_2` FOREIGN KEY (`musico_cpf`) REFERENCES `musico` (`cpf`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Restrições para tabelas `toca`
--
ALTER TABLE `toca`
  ADD CONSTRAINT `toca_ibfk_1` FOREIGN KEY (`musico_cpf`) REFERENCES `musico` (`cpf`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `toca_ibfk_2` FOREIGN KEY (`instrumento_nome`,`instrumento_tom`) REFERENCES `instrumento` (`nome`, `tom`) ON DELETE RESTRICT ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
