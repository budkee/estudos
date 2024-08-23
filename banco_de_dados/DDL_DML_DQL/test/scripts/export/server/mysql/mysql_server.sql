-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql_server:3306
-- Tempo de geração: 28/04/2024 às 22:18
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
-- Banco de dados: `amigo_secreto_kaeu`
--
CREATE DATABASE IF NOT EXISTS `amigo_secreto_kaeu` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `amigo_secreto_kaeu`;

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
--
-- Banco de dados: `amigo_secreto_kaeu_der`
--
CREATE DATABASE IF NOT EXISTS `amigo_secreto_kaeu_der` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `amigo_secreto_kaeu_der`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `avaliacao_sugestao`
--

CREATE TABLE `avaliacao_sugestao` (
  `descricao` varchar(240) NOT NULL,
  `avaliador` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `lista_presente`
--

CREATE TABLE `lista_presente` (
  `descricao` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `mensagem`
--

CREATE TABLE `mensagem` (
  `id` int NOT NULL,
  `msg` varchar(240) NOT NULL,
  `eh_aviso` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `participante`
--

CREATE TABLE `participante` (
  `codinome` varchar(14) NOT NULL,
  `eh_patrocinador` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `sorteio`
--

CREATE TABLE `sorteio` (
  `id_sorteio` int NOT NULL,
  `data` date NOT NULL,
  `codinome_participante` varchar(14) NOT NULL,
  `codinome_ami_secreto` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `avaliacao_sugestao`
--
ALTER TABLE `avaliacao_sugestao`
  ADD PRIMARY KEY (`descricao`);

--
-- Índices de tabela `lista_presente`
--
ALTER TABLE `lista_presente`
  ADD PRIMARY KEY (`descricao`);

--
-- Índices de tabela `mensagem`
--
ALTER TABLE `mensagem`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `participante`
--
ALTER TABLE `participante`
  ADD PRIMARY KEY (`codinome`);

--
-- Índices de tabela `sorteio`
--
ALTER TABLE `sorteio`
  ADD PRIMARY KEY (`id_sorteio`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `mensagem`
--
ALTER TABLE `mensagem`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `sorteio`
--
ALTER TABLE `sorteio`
  MODIFY `id_sorteio` int NOT NULL AUTO_INCREMENT;
--
-- Banco de dados: `amigo_secreto_kaeu_md`
--
CREATE DATABASE IF NOT EXISTS `amigo_secreto_kaeu_md` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `amigo_secreto_kaeu_md`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `avalia_sugestao`
--

CREATE TABLE `avalia_sugestao` (
  `id` int NOT NULL,
  `avaliador` varchar(14) NOT NULL,
  `msg` varchar(240) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `lista_presente`
--

CREATE TABLE `lista_presente` (
  `participante` varchar(14) NOT NULL,
  `presente` varchar(36) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `mensagem`
--

CREATE TABLE `mensagem` (
  `id` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `msg` varchar(240) NOT NULL,
  `remetente` varchar(14) NOT NULL COMMENT 'fk_usuario',
  `destinatario` varchar(14) NOT NULL COMMENT 'fk_usuario'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `participante`
--

CREATE TABLE `participante` (
  `codinome` varchar(14) NOT NULL,
  `presentes` varchar(240) DEFAULT NULL,
  `departamento` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `patrocinador`
--

CREATE TABLE `patrocinador` (
  `empresa` varchar(14) NOT NULL,
  `msg_transmissao` varchar(240) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `sorteio`
--

CREATE TABLE `sorteio` (
  `id` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `participante` varchar(14) NOT NULL,
  `ami_secreto` varchar(14) NOT NULL,
  `presente_ami` varchar(36) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

CREATE TABLE `usuario` (
  `cpf` varchar(14) NOT NULL,
  `codinome` varchar(14) NOT NULL,
  `nome` varchar(36) NOT NULL,
  `eh_patrocinador` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `avalia_sugestao`
--
ALTER TABLE `avalia_sugestao`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `avaliador` (`avaliador`);

--
-- Índices de tabela `lista_presente`
--
ALTER TABLE `lista_presente`
  ADD PRIMARY KEY (`participante`),
  ADD UNIQUE KEY `presente` (`presente`);

--
-- Índices de tabela `mensagem`
--
ALTER TABLE `mensagem`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `remetente` (`remetente`),
  ADD UNIQUE KEY `destinatario` (`destinatario`);

--
-- Índices de tabela `participante`
--
ALTER TABLE `participante`
  ADD PRIMARY KEY (`codinome`),
  ADD UNIQUE KEY `presentes` (`presentes`);

--
-- Índices de tabela `patrocinador`
--
ALTER TABLE `patrocinador`
  ADD PRIMARY KEY (`empresa`);

--
-- Índices de tabela `sorteio`
--
ALTER TABLE `sorteio`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `participante` (`participante`),
  ADD UNIQUE KEY `ami_secreto` (`ami_secreto`);
ALTER TABLE `sorteio` ADD FULLTEXT KEY `presente_ami` (`presente_ami`);

--
-- Índices de tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`cpf`),
  ADD UNIQUE KEY `codinome` (`codinome`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `avalia_sugestao`
--
ALTER TABLE `avalia_sugestao`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `avalia_sugestao`
--
ALTER TABLE `avalia_sugestao`
  ADD CONSTRAINT `avaliador_participante` FOREIGN KEY (`avaliador`) REFERENCES `participante` (`codinome`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Restrições para tabelas `lista_presente`
--
ALTER TABLE `lista_presente`
  ADD CONSTRAINT `participante` FOREIGN KEY (`participante`) REFERENCES `participante` (`codinome`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `presentes_participante` FOREIGN KEY (`presente`) REFERENCES `participante` (`presentes`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Restrições para tabelas `mensagem`
--
ALTER TABLE `mensagem`
  ADD CONSTRAINT `usuario_destino` FOREIGN KEY (`destinatario`) REFERENCES `usuario` (`codinome`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `usuario_recebe` FOREIGN KEY (`remetente`) REFERENCES `usuario` (`codinome`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Restrições para tabelas `sorteio`
--
ALTER TABLE `sorteio`
  ADD CONSTRAINT `ami_secreto` FOREIGN KEY (`ami_secreto`) REFERENCES `participante` (`codinome`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Restrições para tabelas `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_participante` FOREIGN KEY (`codinome`) REFERENCES `participante` (`codinome`) ON DELETE RESTRICT ON UPDATE RESTRICT;
--
-- Banco de dados: `comercio_ext`
--
CREATE DATABASE IF NOT EXISTS `comercio_ext` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `comercio_ext`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `BLOCO`
--

CREATE TABLE `BLOCO` (
  `IdBloco` int NOT NULL,
  `NomeBloco` varchar(15) DEFAULT NULL,
  `Anofund` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `BLOCO_PAIS`
--

CREATE TABLE `BLOCO_PAIS` (
  `Sigla` varchar(15) NOT NULL,
  `IdBloco` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `EXP`
--

CREATE TABLE `EXP` (
  `Pais` varchar(15) NOT NULL,
  `CodProd` int NOT NULL,
  `Ano` int NOT NULL,
  `Quant` int DEFAULT NULL,
  `Valor` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `HISTVALOR`
--

CREATE TABLE `HISTVALOR` (
  `idProduto` int NOT NULL,
  `Data` date NOT NULL,
  `Valor` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `IDIOMA`
--

CREATE TABLE `IDIOMA` (
  `Sigla` varchar(15) NOT NULL,
  `Idioma` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `IMP`
--

CREATE TABLE `IMP` (
  `Pais` varchar(15) NOT NULL,
  `CodProd` int NOT NULL,
  `Ano` int NOT NULL,
  `Quant` int DEFAULT NULL,
  `Valor` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `PAIS`
--

CREATE TABLE `PAIS` (
  `Sigla` varchar(15) NOT NULL,
  `SiglaNet` varchar(15) DEFAULT NULL,
  `Nome` varchar(15) DEFAULT NULL,
  `Area` varchar(15) DEFAULT NULL,
  `Pop` int DEFAULT NULL,
  `Continente` varchar(15) DEFAULT NULL,
  `BRIC` varchar(15) DEFAULT NULL,
  `NomeIngles` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `PIB`
--

CREATE TABLE `PIB` (
  `Sigla` varchar(15) NOT NULL,
  `Ano` int NOT NULL,
  `Valor` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `PRODUTO`
--

CREATE TABLE `PRODUTO` (
  `CodProd` int NOT NULL,
  `NomeProd` varchar(15) DEFAULT NULL,
  `Unidade` int DEFAULT NULL,
  `DescrProduto` varchar(15) DEFAULT NULL,
  `TipoProd` varchar(15) DEFAULT NULL,
  `Class` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `BLOCO`
--
ALTER TABLE `BLOCO`
  ADD PRIMARY KEY (`IdBloco`);

--
-- Índices de tabela `BLOCO_PAIS`
--
ALTER TABLE `BLOCO_PAIS`
  ADD PRIMARY KEY (`Sigla`,`IdBloco`),
  ADD KEY `IdBloco` (`IdBloco`);

--
-- Índices de tabela `EXP`
--
ALTER TABLE `EXP`
  ADD PRIMARY KEY (`Pais`,`CodProd`,`Ano`),
  ADD KEY `CodProd` (`CodProd`);

--
-- Índices de tabela `HISTVALOR`
--
ALTER TABLE `HISTVALOR`
  ADD PRIMARY KEY (`idProduto`,`Data`);

--
-- Índices de tabela `IDIOMA`
--
ALTER TABLE `IDIOMA`
  ADD PRIMARY KEY (`Sigla`,`Idioma`);

--
-- Índices de tabela `IMP`
--
ALTER TABLE `IMP`
  ADD PRIMARY KEY (`Pais`,`CodProd`,`Ano`),
  ADD KEY `CodProd` (`CodProd`);

--
-- Índices de tabela `PAIS`
--
ALTER TABLE `PAIS`
  ADD PRIMARY KEY (`Sigla`);

--
-- Índices de tabela `PIB`
--
ALTER TABLE `PIB`
  ADD PRIMARY KEY (`Sigla`,`Ano`);

--
-- Índices de tabela `PRODUTO`
--
ALTER TABLE `PRODUTO`
  ADD PRIMARY KEY (`CodProd`);

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `BLOCO_PAIS`
--
ALTER TABLE `BLOCO_PAIS`
  ADD CONSTRAINT `BLOCO_PAIS_ibfk_1` FOREIGN KEY (`IdBloco`) REFERENCES `BLOCO` (`IdBloco`),
  ADD CONSTRAINT `BLOCO_PAIS_ibfk_2` FOREIGN KEY (`Sigla`) REFERENCES `PAIS` (`Sigla`);

--
-- Restrições para tabelas `EXP`
--
ALTER TABLE `EXP`
  ADD CONSTRAINT `EXP_ibfk_1` FOREIGN KEY (`CodProd`) REFERENCES `PRODUTO` (`CodProd`);

--
-- Restrições para tabelas `HISTVALOR`
--
ALTER TABLE `HISTVALOR`
  ADD CONSTRAINT `HISTVALOR_ibfk_1` FOREIGN KEY (`idProduto`) REFERENCES `PRODUTO` (`CodProd`);

--
-- Restrições para tabelas `IDIOMA`
--
ALTER TABLE `IDIOMA`
  ADD CONSTRAINT `IDIOMA_ibfk_1` FOREIGN KEY (`Sigla`) REFERENCES `PAIS` (`Sigla`);

--
-- Restrições para tabelas `IMP`
--
ALTER TABLE `IMP`
  ADD CONSTRAINT `IMP_ibfk_1` FOREIGN KEY (`CodProd`) REFERENCES `PRODUTO` (`CodProd`);

--
-- Restrições para tabelas `PIB`
--
ALTER TABLE `PIB`
  ADD CONSTRAINT `PIB_ibfk_1` FOREIGN KEY (`Sigla`) REFERENCES `PAIS` (`Sigla`);
--
-- Banco de dados: `notown_kaeu_der`
--
CREATE DATABASE IF NOT EXISTS `notown_kaeu_der` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `notown_kaeu_der`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `album`
--

CREATE TABLE `album` (
  `id` int NOT NULL,
  `titulo` varchar(36) NOT NULL,
  `data` date DEFAULT NULL,
  `formato` char(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'CD' COMMENT 'CD ou MC',
  `produtor` varchar(14) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `album`
--

INSERT INTO `album` (`id`, `titulo`, `data`, `formato`, `produtor`) VALUES
(1, 'Vaca atolada', '2023-02-28', 'CD', NULL),
(2, 'Três pratos de trigo', '2022-04-28', 'CD', NULL),
(3, 'Para três tigres tristes', '2022-05-28', 'CD', NULL);

-- --------------------------------------------------------

--
-- Estrutura para tabela `endereco`
--

CREATE TABLE `endereco` (
  `telefone` varchar(14) NOT NULL,
  `cep` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `logradouro` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `endereco`
--

INSERT INTO `endereco` (`telefone`, `cep`, `logradouro`) VALUES
('(67) 3328-2231', '55.442-283', 'Rua Roxa'),
('(67) 3328-2233', '33.442-283', 'Rua Amarela'),
('(67) 3328-2441', '55.442-222', 'Rua Branca');

-- --------------------------------------------------------

--
-- Estrutura para tabela `instrumento`
--

CREATE TABLE `instrumento` (
  `id` int NOT NULL,
  `tom` char(3) NOT NULL,
  `nome` varchar(36) NOT NULL,
  `emprestado` tinyint(1) NOT NULL DEFAULT '0',
  `musico_emprestimo` varchar(14) DEFAULT NULL COMMENT 'fk_musico'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `instrumento`
--

INSERT INTO `instrumento` (`id`, `tom`, `nome`, `emprestado`, `musico_emprestimo`) VALUES
(1, 'B', 'Flauta Doce', 0, NULL),
(2, 'E', 'Guitarra', 0, NULL),
(3, 'E', 'Violão', 0, NULL);

-- --------------------------------------------------------

--
-- Estrutura para tabela `musica`
--

CREATE TABLE `musica` (
  `id` int NOT NULL,
  `titulo` varchar(36) NOT NULL,
  `interprete` varchar(14) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'fk_musico',
  `album` int DEFAULT NULL COMMENT 'fk_album'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `musica`
--

INSERT INTO `musica` (`id`, `titulo`, `interprete`, `album`) VALUES
(1, 'Deus Dará', '033.333.231-22', 1),
(2, 'Dalila', '033.333.231-32', 2),
(3, 'Girassol', '033.333.881-22', 3);

-- --------------------------------------------------------

--
-- Estrutura para tabela `musico`
--

CREATE TABLE `musico` (
  `cpf` varchar(14) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '999.999.999-99',
  `nome` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `telefone` varchar(14) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'fk_endereco'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `musico`
--

INSERT INTO `musico` (`cpf`, `nome`, `telefone`) VALUES
('033.333.231-22', 'Pedro', '(67) 3328-2231'),
('033.333.231-32', 'Jão', '(67) 3328-2233'),
('033.333.881-22', 'Costa', '(67) 3328-2441');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `album`
--
ALTER TABLE `album`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `produtor` (`produtor`);

--
-- Índices de tabela `endereco`
--
ALTER TABLE `endereco`
  ADD PRIMARY KEY (`telefone`),
  ADD UNIQUE KEY `telefone` (`telefone`);

--
-- Índices de tabela `instrumento`
--
ALTER TABLE `instrumento`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `musico_emprestimo` (`musico_emprestimo`);

--
-- Índices de tabela `musica`
--
ALTER TABLE `musica`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `album` (`album`),
  ADD UNIQUE KEY `autor` (`interprete`);

--
-- Índices de tabela `musico`
--
ALTER TABLE `musico`
  ADD PRIMARY KEY (`cpf`),
  ADD UNIQUE KEY `telefone` (`telefone`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `musica`
--
ALTER TABLE `musica`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `album`
--
ALTER TABLE `album`
  ADD CONSTRAINT `musico_produtor` FOREIGN KEY (`produtor`) REFERENCES `musico` (`cpf`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Restrições para tabelas `instrumento`
--
ALTER TABLE `instrumento`
  ADD CONSTRAINT `emprestimo_musico` FOREIGN KEY (`musico_emprestimo`) REFERENCES `musico` (`cpf`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Restrições para tabelas `musica`
--
ALTER TABLE `musica`
  ADD CONSTRAINT `album_musica` FOREIGN KEY (`album`) REFERENCES `album` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `musico_autor` FOREIGN KEY (`interprete`) REFERENCES `musico` (`cpf`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Restrições para tabelas `musico`
--
ALTER TABLE `musico`
  ADD CONSTRAINT `telefone_musico` FOREIGN KEY (`telefone`) REFERENCES `endereco` (`telefone`) ON DELETE CASCADE ON UPDATE CASCADE;
--
-- Banco de dados: `notown_kaeu_exp`
--
CREATE DATABASE IF NOT EXISTS `notown_kaeu_exp` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `notown_kaeu_exp`;

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
--
-- Banco de dados: `notown_marcio_der`
--
CREATE DATABASE IF NOT EXISTS `notown_marcio_der` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `notown_marcio_der`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `album`
--

CREATE TABLE `album` (
  `id` int NOT NULL,
  `titulo` varchar(36) NOT NULL,
  `formato` char(5) NOT NULL COMMENT 'CD ou MC',
  `data` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `album`
--

INSERT INTO `album` (`id`, `titulo`, `formato`, `data`) VALUES
(1, 'A Cor que nunca acaba', 'CD', '2024-04-21'),
(2, 'Olhos de cigana', 'MC', '2024-03-22'),
(3, 'Cabelo colorido', 'MC', '2024-03-22');

-- --------------------------------------------------------

--
-- Estrutura para tabela `endereco`
--

CREATE TABLE `endereco` (
  `telefone` varchar(14) NOT NULL,
  `cep` varchar(10) NOT NULL,
  `logradouro` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `endereco`
--

INSERT INTO `endereco` (`telefone`, `cep`, `logradouro`) VALUES
('(65) 3344-3432', '79.933-822', 'Rua Roxa'),
('(67) 3233-3322', '79.933-828', 'Rua Amarela'),
('(67) 3433-3222', '79.933-823', 'Rua Branca');

-- --------------------------------------------------------

--
-- Estrutura para tabela `instrumento`
--

CREATE TABLE `instrumento` (
  `tom` varchar(3) NOT NULL,
  `nome` varchar(36) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `instrumento`
--

INSERT INTO `instrumento` (`tom`, `nome`) VALUES
('C', 'Gaita'),
('C', 'Sanfona'),
('E', 'Guitarra');

-- --------------------------------------------------------

--
-- Estrutura para tabela `musica`
--

CREATE TABLE `musica` (
  `id` int NOT NULL,
  `titulo` varchar(36) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `musica`
--

INSERT INTO `musica` (`id`, `titulo`) VALUES
(1, 'Tudo que ela quer'),
(2, 'Girassol'),
(3, 'Flamingo');

-- --------------------------------------------------------

--
-- Estrutura para tabela `musico`
--

CREATE TABLE `musico` (
  `cpf` varchar(14) NOT NULL,
  `nome` varchar(36) NOT NULL,
  `telefone` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `musico`
--

INSERT INTO `musico` (`cpf`, `nome`, `telefone`) VALUES
('999.837.376-37', 'Jonas', '(72) 922433283'),
('999.837.377-37', 'Tomas', '(65) 922833283'),
('999.837.377-38', 'Kauã', '(67) 922833283');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `album`
--
ALTER TABLE `album`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `endereco`
--
ALTER TABLE `endereco`
  ADD PRIMARY KEY (`telefone`);

--
-- Índices de tabela `instrumento`
--
ALTER TABLE `instrumento`
  ADD PRIMARY KEY (`tom`,`nome`);

--
-- Índices de tabela `musica`
--
ALTER TABLE `musica`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `musico`
--
ALTER TABLE `musico`
  ADD PRIMARY KEY (`cpf`),
  ADD UNIQUE KEY `nome` (`nome`);
--
-- Banco de dados: `notown_marcio_exp`
--
CREATE DATABASE IF NOT EXISTS `notown_marcio_exp` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `notown_marcio_exp`;

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
  MODIFY `endereco_id` int NOT NULL AUTO_INCREMENT;

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
