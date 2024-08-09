-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Tempo de geração: 01/05/2024 às 00:56
-- Versão do servidor: 8.3.0
-- Versão do PHP: 8.2.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `mao_de_obra_ltda`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `cliente`
--

CREATE TABLE `cliente` (
  `num` int NOT NULL,
  `nome` varchar(36) NOT NULL,
  `endereco` varchar(50) NOT NULL,
  `telefone` varchar(18) NOT NULL,
  `data_cadastro` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `cliente`
--

INSERT INTO `cliente` (`num`, `nome`, `endereco`, `telefone`, `data_cadastro`) VALUES
(1, 'Seu Jorge', 'Rua purpurina, 555', '(67) 992272777', '2024-03-04'),
(2, 'Pablo Vittar', 'Rua roxa, 666', '(67) 992272555', '2024-03-04'),
(3, 'Lúcia de Fátima', 'Rua rosa, 777', '(67) 992272733', '2024-03-18'),
(4, 'Pablo Escobar', 'Rua azul, 444', '(67) 992272788', '2024-03-08'),
(5, 'Gloria Grover', 'Rua branca, 883', '(67) 992272799', '2024-03-19');

-- --------------------------------------------------------

--
-- Estrutura para tabela `colaborador`
--

CREATE TABLE `colaborador` (
  `num` int NOT NULL,
  `nome` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `endereco` varchar(36) NOT NULL,
  `data_cadastro` date NOT NULL,
  `num_setor` int NOT NULL,
  `servicos_aptidoes` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `telefone` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `escolaridade` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `linguas` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `colaborador`
--

INSERT INTO `colaborador` (`num`, `nome`, `endereco`, `data_cadastro`, `num_setor`, `servicos_aptidoes`, `telefone`, `escolaridade`, `linguas`) VALUES
(1, 'Paulo Coelho', 'Rua amarela, 883', '2024-02-09', 1, 'asdsarr adasdasd', '(67) 992272700', 'Ensino Fundamental', 'Português'),
(2, 'Paulo Joaquim dos Santos', 'Rua roxa, 883', '2024-02-01', 2, 'asdsdsd asrera', '(67) 992272729', 'Ensino Médio', 'Português e Espanhol'),
(3, 'João Joaquim dos Santos', 'Rua rosa, 883', '2024-02-04', 4, 'asdas aasdsdas', '(67) 992272721', 'Ensino Superior', 'Português, Inglês e Espanhol'),
(4, 'Paulo dos Santos', 'Rua azul, 883', '2024-02-07', 3, 'asd warefdcasd asds', '(67) 992272723', 'Ensino Médio', 'Português e Inglês '),
(5, 'Joaquina dos Santos', 'Rua purpurina, 883', '2024-02-07', 3, 'asd warefdcasd asdswdadsadasda', '(67) 992272003', 'Ensino Médio', 'Português e Inglês ');

-- --------------------------------------------------------

--
-- Estrutura para tabela `equipe_trab`
--

CREATE TABLE `equipe_trab` (
  `num_serv` int NOT NULL,
  `num_colab` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `equipe_trab`
--

INSERT INTO `equipe_trab` (`num_serv`, `num_colab`) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 5),
(2, 3),
(2, 4),
(2, 5),
(3, 2),
(4, 2);

-- --------------------------------------------------------

--
-- Estrutura para tabela `servico`
--

CREATE TABLE `servico` (
  `id` int NOT NULL,
  `descricao` varchar(250) NOT NULL,
  `data_recepcao` date NOT NULL,
  `data_inicio_serv` date NOT NULL,
  `num_equipe_trab` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `servico`
--

INSERT INTO `servico` (`id`, `descricao`, `data_recepcao`, `data_inicio_serv`, `num_equipe_trab`) VALUES
(1, 'carpintaria', '2024-04-01', '2024-04-08', 1),
(2, 'trabalho agricola', '2024-03-29', '2024-04-01', 2),
(3, 'limpeza/higiene', '2024-04-01', '2024-04-02', 3),
(4, 'soldador', '2024-04-01', '2024-04-02', 4),
(5, 'carpintaria', '2024-03-04', '2024-04-09', 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `setor_atividade`
--

CREATE TABLE `setor_atividade` (
  `num` int NOT NULL,
  `nome` varchar(36) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `setor_atividade`
--

INSERT INTO `setor_atividade` (`num`, `nome`) VALUES
(1, 'trabalhos agricolas'),
(2, 'limpeza/higiene'),
(3, 'carpintaria'),
(4, 'soldador');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`num`);

--
-- Índices de tabela `colaborador`
--
ALTER TABLE `colaborador`
  ADD PRIMARY KEY (`num`),
  ADD KEY `num_setor` (`num_setor`) USING BTREE;

--
-- Índices de tabela `equipe_trab`
--
ALTER TABLE `equipe_trab`
  ADD PRIMARY KEY (`num_serv`,`num_colab`),
  ADD KEY `num_serv` (`num_serv`),
  ADD KEY `num_colab` (`num_colab`);

--
-- Índices de tabela `servico`
--
ALTER TABLE `servico`
  ADD PRIMARY KEY (`id`),
  ADD KEY `num_equipe_trab` (`num_equipe_trab`) USING BTREE;

--
-- Índices de tabela `setor_atividade`
--
ALTER TABLE `setor_atividade`
  ADD PRIMARY KEY (`num`);

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `colaborador`
--
ALTER TABLE `colaborador`
  ADD CONSTRAINT `num_setor` FOREIGN KEY (`num_setor`) REFERENCES `setor_atividade` (`num`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Restrições para tabelas `equipe_trab`
--
ALTER TABLE `equipe_trab`
  ADD CONSTRAINT `num_colab` FOREIGN KEY (`num_colab`) REFERENCES `colaborador` (`num`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `num_serv` FOREIGN KEY (`num_serv`) REFERENCES `servico` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Restrições para tabelas `servico`
--
ALTER TABLE `servico`
  ADD CONSTRAINT `num_equipe` FOREIGN KEY (`num_equipe_trab`) REFERENCES `equipe_trab` (`num_serv`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
