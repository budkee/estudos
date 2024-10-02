-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Tempo de geração: 24/04/2024 às 15:49
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
-- Banco de dados: `sistema_eleitoral`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `Candidato`
--

CREATE TABLE `Candidato` (
  `rg` varchar(11) NOT NULL,
  `nome` varchar(36) NOT NULL,
  `cargo` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `partido` int NOT NULL COMMENT 'fk_candidato_partido'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Candidato`
--

INSERT INTO `Candidato` (`rg`, `nome`, `cargo`, `partido`) VALUES
('9999994', 'Manuela', 'Deputado Estadual', 6),
('9999995', 'Pedro', 'Deputado Federal', 5),
('9999996', 'Jorge', 'Vereador', 4),
('9999997', 'Christina', 'Deputado Estadual', 3),
('9999998', 'Moisés', 'Deputado Federal', 2),
('9999999', 'Romeo', 'Vereador', 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Eleitor`
--

CREATE TABLE `Eleitor` (
  `rg` varchar(11) NOT NULL,
  `titulo_eleitor` varchar(12) NOT NULL,
  `nome` varchar(36) NOT NULL,
  `data_nasc` varchar(10) NOT NULL,
  `numero_secao` int NOT NULL COMMENT 'id_secao',
  `numero_zona` int NOT NULL COMMENT 'id_zona',
  `numero_localidade` int NOT NULL COMMENT 'id_localidade',
  `voto` varchar(11) NOT NULL COMMENT 'id_candidato'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Eleitor`
--

INSERT INTO `Eleitor` (`rg`, `titulo_eleitor`, `nome`, `data_nasc`, `numero_secao`, `numero_zona`, `numero_localidade`, `voto`) VALUES
('111111111', '112223231234', 'Rosemary da Silva', '13/05/2000', 1, 1, 333, '9999994'),
('111111112', '112223231232', 'Pedro Augusto dos Santos', '13/03/2001', 1, 1, 333, '9999994'),
('111111113', '112223231233', 'Matilde Medeiras', '12/05/2000', 5, 111, 334, '9999995'),
('111111114', '112223231231', 'Vitória Rodrigues', '14/03/2001', 2, 111, 333, '9999999'),
('111111115', '112223231235', 'Murilo Fraga', '12/01/2000', 3, 111, 333, '9999996'),
('111111116', '112223231236', 'Alexandre Santana', '11/10/2000', 4, 1, 333, '9999997');

-- --------------------------------------------------------

--
-- Estrutura para tabela `Localidade`
--

CREATE TABLE `Localidade` (
  `id` int NOT NULL COMMENT 'id do objeto',
  `nome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Localidade`
--

INSERT INTO `Localidade` (`id`, `nome`) VALUES
(333, 'Campo Grande'),
(334, 'Paranaíba'),
(335, 'Rio Verde de Mato Grosso'),
(336, 'Ponta Porã'),
(337, 'Dourados'),
(338, 'São Gabriel do Oeste');

-- --------------------------------------------------------

--
-- Estrutura para tabela `Partido`
--

CREATE TABLE `Partido` (
  `id` int NOT NULL,
  `nome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Partido`
--

INSERT INTO `Partido` (`id`, `nome`) VALUES
(1, 'Partido Cor de Rosa'),
(2, 'Arco-íris'),
(3, 'Verde'),
(4, 'Partido Vermelho'),
(5, 'Branco'),
(6, 'Roxo');

-- --------------------------------------------------------

--
-- Estrutura para tabela `Seção`
--

CREATE TABLE `Seção` (
  `id` int NOT NULL,
  `nome` varchar(36) NOT NULL,
  `zona` int NOT NULL COMMENT 'id_zona'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Seção`
--

INSERT INTO `Seção` (`id`, `nome`, `zona`) VALUES
(1, 'A', 1),
(2, 'B', 1),
(3, 'C', 1),
(4, 'A', 11),
(5, 'B', 11),
(6, 'C', 11);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Zona Eleitoral`
--

CREATE TABLE `Zona Eleitoral` (
  `id` int NOT NULL COMMENT 'id objeto',
  `localidade` int NOT NULL COMMENT 'id_localidade',
  `nome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `Zona Eleitoral`
--

INSERT INTO `Zona Eleitoral` (`id`, `localidade`, `nome`) VALUES
(1, 333, 'Zona Leste'),
(11, 333, 'Zona Oeste'),
(111, 333, 'Zona Norte'),
(1111, 333, 'Zona Sul');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `Candidato`
--
ALTER TABLE `Candidato`
  ADD PRIMARY KEY (`rg`),
  ADD KEY `fk_candidato_partido` (`partido`);

--
-- Índices de tabela `Eleitor`
--
ALTER TABLE `Eleitor`
  ADD PRIMARY KEY (`rg`,`titulo_eleitor`),
  ADD KEY `fk_eleitor_localidade` (`numero_localidade`),
  ADD KEY `fk_eleitor_secao` (`numero_secao`),
  ADD KEY `fk_eleitor_zona` (`numero_zona`),
  ADD KEY `fk_voto_candidato` (`voto`);

--
-- Índices de tabela `Localidade`
--
ALTER TABLE `Localidade`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `Partido`
--
ALTER TABLE `Partido`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `Seção`
--
ALTER TABLE `Seção`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_secao_zona` (`zona`);

--
-- Índices de tabela `Zona Eleitoral`
--
ALTER TABLE `Zona Eleitoral`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD KEY `fk_zona_localidade` (`localidade`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `Localidade`
--
ALTER TABLE `Localidade`
  MODIFY `id` int NOT NULL AUTO_INCREMENT COMMENT 'id do objeto', AUTO_INCREMENT=339;

--
-- AUTO_INCREMENT de tabela `Partido`
--
ALTER TABLE `Partido`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `Seção`
--
ALTER TABLE `Seção`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `Zona Eleitoral`
--
ALTER TABLE `Zona Eleitoral`
  MODIFY `id` int NOT NULL AUTO_INCREMENT COMMENT 'id objeto', AUTO_INCREMENT=1112;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `Candidato`
--
ALTER TABLE `Candidato`
  ADD CONSTRAINT `fk_candidato_partido` FOREIGN KEY (`partido`) REFERENCES `Partido` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Restrições para tabelas `Eleitor`
--
ALTER TABLE `Eleitor`
  ADD CONSTRAINT `fk_eleitor_localidade` FOREIGN KEY (`numero_localidade`) REFERENCES `Localidade` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_eleitor_secao` FOREIGN KEY (`numero_secao`) REFERENCES `Seção` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_eleitor_zona` FOREIGN KEY (`numero_zona`) REFERENCES `Zona Eleitoral` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_voto_candidato` FOREIGN KEY (`voto`) REFERENCES `Candidato` (`rg`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Restrições para tabelas `Seção`
--
ALTER TABLE `Seção`
  ADD CONSTRAINT `fk_secao_zona` FOREIGN KEY (`zona`) REFERENCES `Zona Eleitoral` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Restrições para tabelas `Zona Eleitoral`
--
ALTER TABLE `Zona Eleitoral`
  ADD CONSTRAINT `fk_zona_localidade` FOREIGN KEY (`localidade`) REFERENCES `Localidade` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
