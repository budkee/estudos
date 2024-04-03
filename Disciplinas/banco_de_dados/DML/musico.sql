-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql_server:3306
-- Tempo de geração: 03/04/2024 às 00:05
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
('12332198789', 'Jefferson', '77667266365', 1),
('87888987878', 'João Carreiro', '12232312232', 2),;
('13834833432', 'Capataz', '99585839584', 3),;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `musico`
--
ALTER TABLE `musico`
  ADD PRIMARY KEY (`cpf`),
  ADD KEY `endereco_id` (`endereco_id`);

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `musico`
--
ALTER TABLE `musico`
  ADD CONSTRAINT `musico_ibfk_1` FOREIGN KEY (`endereco_id`) REFERENCES `endereco` (`endereco_id`) ON DELETE RESTRICT ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
