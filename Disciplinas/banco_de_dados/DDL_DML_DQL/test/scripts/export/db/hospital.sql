-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql_server
-- Tempo de geração: 25/03/2024 às 20:03
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
-- Banco de dados: `hospital`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `consulta`
--

CREATE TABLE `consulta` (
  `id` int NOT NULL,
  `data` date NOT NULL,
  `tipo` varchar(256) NOT NULL,
  `resultado` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `medico`
--

CREATE TABLE `medico` (
  `crm` int NOT NULL,
  `telefone` int NOT NULL,
  `especializacao` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `paciente`
--

CREATE TABLE `paciente` (
  `cpf` int NOT NULL,
  `rg` int NOT NULL,
  `endereco` varchar(128) NOT NULL,
  `telefones` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `telefones`
--

CREATE TABLE `telefones` (
  `telefone` int NOT NULL,
  `cpf_paciente` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `consulta`
--
ALTER TABLE `consulta`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `medico`
--
ALTER TABLE `medico`
  ADD PRIMARY KEY (`crm`);

--
-- Índices de tabela `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`cpf`);

--
-- Índices de tabela `telefones`
--
ALTER TABLE `telefones`
  ADD KEY `cpf_paciente_fk` (`telefone`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `consulta`
--
ALTER TABLE `consulta`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `consulta`
--
ALTER TABLE `consulta`
  ADD CONSTRAINT `consulta_medico_fk` FOREIGN KEY (`id`) REFERENCES `medico` (`crm`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `consulta_paciente_fk` FOREIGN KEY (`id`) REFERENCES `paciente` (`cpf`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Restrições para tabelas `paciente`
--
ALTER TABLE `paciente`
  ADD CONSTRAINT `medico_responsavel_fk` FOREIGN KEY (`cpf`) REFERENCES `medico` (`crm`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Restrições para tabelas `telefones`
--
ALTER TABLE `telefones`
  ADD CONSTRAINT `cpf_paciente_fk` FOREIGN KEY (`telefone`) REFERENCES `paciente` (`cpf`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
