-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql_server
-- Tempo de geração: 29/03/2024 às 05:30
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
-- Banco de dados: `notown_records`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `album`
--

CREATE TABLE `album` (
  `id_album` int NOT NULL,
  `titulo` varchar(30) NOT NULL,
  `data_direitos_autorais` date NOT NULL,
  `formato` varchar(15) NOT NULL,
  `produtor` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `eh_utilizado`
--

CREATE TABLE `eh_utilizado` (
  `instrumento` int NOT NULL,
  `musica` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `endereco`
--

CREATE TABLE `endereco` (
  `num_telefone` varchar(16) NOT NULL,
  `endereco` varchar(50) NOT NULL,
  `cpf_musico` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `instrumento`
--

CREATE TABLE `instrumento` (
  `id_instrumento` int NOT NULL,
  `tom_musical` varchar(5) NOT NULL,
  `nome` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `musica`
--

CREATE TABLE `musica` (
  `id_musica` int NOT NULL,
  `album` int NOT NULL,
  `titulo` varchar(30) NOT NULL,
  `autor` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `musico`
--

CREATE TABLE `musico` (
  `cpf` varchar(14) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `endereco` varchar(50) NOT NULL,
  `telefone` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `album`
--
ALTER TABLE `album`
  ADD PRIMARY KEY (`id_album`),
  ADD KEY `album_produtor_fk` (`produtor`);

--
-- Índices de tabela `eh_utilizado`
--
ALTER TABLE `eh_utilizado`
  ADD PRIMARY KEY (`instrumento`,`musica`),
  ADD KEY `musica_instrumento_fk` (`musica`);

--
-- Índices de tabela `endereco`
--
ALTER TABLE `endereco`
  ADD PRIMARY KEY (`endereco`) USING BTREE;

--
-- Índices de tabela `instrumento`
--
ALTER TABLE `instrumento`
  ADD PRIMARY KEY (`id_instrumento`);

--
-- Índices de tabela `musica`
--
ALTER TABLE `musica`
  ADD PRIMARY KEY (`id_musica`),
  ADD KEY `musica_album_fk` (`album`),
  ADD KEY `musica_autor_fk` (`autor`);

--
-- Índices de tabela `musico`
--
ALTER TABLE `musico`
  ADD PRIMARY KEY (`cpf`),
  ADD KEY `musico_endereco_fk` (`endereco`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `album`
--
ALTER TABLE `album`
  MODIFY `id_album` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `instrumento`
--
ALTER TABLE `instrumento`
  MODIFY `id_instrumento` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `musica`
--
ALTER TABLE `musica`
  MODIFY `id_musica` int NOT NULL AUTO_INCREMENT;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `album`
--
ALTER TABLE `album`
  ADD CONSTRAINT `album_produtor_fk` FOREIGN KEY (`produtor`) REFERENCES `musico` (`cpf`) ON UPDATE RESTRICT;

--
-- Restrições para tabelas `eh_utilizado`
--
ALTER TABLE `eh_utilizado`
  ADD CONSTRAINT `instrumento_musica_fk` FOREIGN KEY (`instrumento`) REFERENCES `instrumento` (`id_instrumento`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `musica_instrumento_fk` FOREIGN KEY (`musica`) REFERENCES `musica` (`id_musica`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Restrições para tabelas `musica`
--
ALTER TABLE `musica`
  ADD CONSTRAINT `musica_album_fk` FOREIGN KEY (`album`) REFERENCES `album` (`id_album`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `musica_autor_fk` FOREIGN KEY (`autor`) REFERENCES `musico` (`cpf`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Restrições para tabelas `musico`
--
ALTER TABLE `musico`
  ADD CONSTRAINT `musico_endereco_fk` FOREIGN KEY (`endereco`) REFERENCES `endereco` (`endereco`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
