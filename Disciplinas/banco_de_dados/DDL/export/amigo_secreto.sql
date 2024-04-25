-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql_server
-- Tempo de geração: 29/03/2024 às 04:43
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
-- Banco de dados: `amigo_secreto`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `avaliacao_sugestao`
--

CREATE TABLE `avaliacao_sugestao` (
  `id_avaliacao_sugestao` int NOT NULL,
  `id_participante_avaliador` int NOT NULL,
  `avaliacao_sugestao` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `destinatario`
--

CREATE TABLE `destinatario` (
  `id_destinatario` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `mensagem`
--

CREATE TABLE `mensagem` (
  `id_mensagem` int NOT NULL,
  `data_hora_envio` date NOT NULL,
  `conteudo_mensagem` varchar(240) NOT NULL,
  `remetente` int NOT NULL,
  `destinatario` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `notificacao`
--

CREATE TABLE `notificacao` (
  `id_notificacao` int NOT NULL,
  `id_remetente` int NOT NULL,
  `id_destinatario` int NOT NULL,
  `id_sorteio` int NOT NULL,
  `id_mensagem` int NOT NULL,
  `id_patrocinador` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `participante`
--

CREATE TABLE `participante` (
  `id_participante` int NOT NULL,
  `nome` varchar(50) NOT NULL,
  `codinome` varchar(25) NOT NULL,
  `ramal` int NOT NULL,
  `sugestao_presente` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `patrocinador`
--

CREATE TABLE `patrocinador` (
  `id_patrocinador` int NOT NULL,
  `aviso_geral` varchar(240) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `remetente`
--

CREATE TABLE `remetente` (
  `id_remetente` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `resultado`
--

CREATE TABLE `resultado` (
  `id_resultado` int NOT NULL,
  `id_sorteio` int NOT NULL,
  `id_participante` int NOT NULL,
  `id_amigo_secreto` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `sorteio`
--

CREATE TABLE `sorteio` (
  `id_sorteio` int NOT NULL,
  `data_hora` date NOT NULL,
  `resultado` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `avaliacao_sugestao`
--
ALTER TABLE `avaliacao_sugestao`
  ADD PRIMARY KEY (`id_avaliacao_sugestao`),
  ADD KEY `participante_avaliador_fk` (`id_participante_avaliador`);

--
-- Índices de tabela `destinatario`
--
ALTER TABLE `destinatario`
  ADD PRIMARY KEY (`id_destinatario`);

--
-- Índices de tabela `mensagem`
--
ALTER TABLE `mensagem`
  ADD PRIMARY KEY (`id_mensagem`),
  ADD KEY `mensagem_remetente_fk` (`remetente`),
  ADD KEY `mensagem_destinatario_fk` (`destinatario`);

--
-- Índices de tabela `notificacao`
--
ALTER TABLE `notificacao`
  ADD PRIMARY KEY (`id_notificacao`) USING BTREE,
  ADD KEY `notificacao_sorteio_fk` (`id_sorteio`),
  ADD KEY `notificacao_patrocinador_fk` (`id_patrocinador`);

--
-- Índices de tabela `participante`
--
ALTER TABLE `participante`
  ADD PRIMARY KEY (`id_participante`);

--
-- Índices de tabela `patrocinador`
--
ALTER TABLE `patrocinador`
  ADD PRIMARY KEY (`id_patrocinador`);

--
-- Índices de tabela `remetente`
--
ALTER TABLE `remetente`
  ADD PRIMARY KEY (`id_remetente`);

--
-- Índices de tabela `resultado`
--
ALTER TABLE `resultado`
  ADD PRIMARY KEY (`id_resultado`) USING BTREE;

--
-- Índices de tabela `sorteio`
--
ALTER TABLE `sorteio`
  ADD PRIMARY KEY (`id_sorteio`),
  ADD KEY `sorteio_resultado_fk` (`resultado`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `avaliacao_sugestao`
--
ALTER TABLE `avaliacao_sugestao`
  MODIFY `id_avaliacao_sugestao` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `mensagem`
--
ALTER TABLE `mensagem`
  MODIFY `id_mensagem` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `participante`
--
ALTER TABLE `participante`
  MODIFY `id_participante` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `patrocinador`
--
ALTER TABLE `patrocinador`
  MODIFY `id_patrocinador` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `sorteio`
--
ALTER TABLE `sorteio`
  MODIFY `id_sorteio` int NOT NULL AUTO_INCREMENT;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `avaliacao_sugestao`
--
ALTER TABLE `avaliacao_sugestao`
  ADD CONSTRAINT `participante_avaliador_fk` FOREIGN KEY (`id_participante_avaliador`) REFERENCES `participante` (`id_participante`) ON UPDATE RESTRICT;

--
-- Restrições para tabelas `mensagem`
--
ALTER TABLE `mensagem`
  ADD CONSTRAINT `mensagem_destinatario_fk` FOREIGN KEY (`destinatario`) REFERENCES `destinatario` (`id_destinatario`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `mensagem_remetente_fk` FOREIGN KEY (`remetente`) REFERENCES `remetente` (`id_remetente`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Restrições para tabelas `notificacao`
--
ALTER TABLE `notificacao`
  ADD CONSTRAINT `notificacao_patrocinador_fk` FOREIGN KEY (`id_patrocinador`) REFERENCES `patrocinador` (`id_patrocinador`) ON UPDATE RESTRICT;

--
-- Restrições para tabelas `sorteio`
--
ALTER TABLE `sorteio`
  ADD CONSTRAINT `sorteio_resultado_fk` FOREIGN KEY (`resultado`) REFERENCES `sorteio` (`id_sorteio`) ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
