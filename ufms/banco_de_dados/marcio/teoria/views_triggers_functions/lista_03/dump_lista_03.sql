--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.2 (Debian 16.2-1.pgdg120+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: vendas; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA vendas;


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: ex_cliente; Type: TABLE; Schema: vendas; Owner: -
--

CREATE TABLE vendas.ex_cliente (
    codcliente integer NOT NULL,
    nome character varying(60),
    datanascimento date,
    cpf character varying(11)
);


--
-- Name: ex_itempedido; Type: TABLE; Schema: vendas; Owner: -
--

CREATE TABLE vendas.ex_itempedido (
    codpedido integer NOT NULL,
    numeroitem integer NOT NULL,
    valorunitario numeric(10,2),
    quantidade integer,
    codproduto integer
);


--
-- Name: ex_pedido; Type: TABLE; Schema: vendas; Owner: -
--

CREATE TABLE vendas.ex_pedido (
    codpedido integer NOT NULL,
    codcliente integer,
    datapedido date,
    nf character varying(12),
    valortotal numeric(10,2)
);


--
-- Name: ex_produto; Type: TABLE; Schema: vendas; Owner: -
--

CREATE TABLE vendas.ex_produto (
    codproduto integer NOT NULL,
    descricao character varying(100)
);


--
-- Data for Name: ex_cliente; Type: TABLE DATA; Schema: vendas; Owner: -
--

INSERT INTO vendas.ex_cliente VALUES (1, 'Sylvio Barbon', '1984-12-05', '12315541212');
INSERT INTO vendas.ex_cliente VALUES (2, 'Antonio Carlos da Silva', '1970-11-01', '12313345512');
INSERT INTO vendas.ex_cliente VALUES (3, 'Thiago Ribeiro', '1964-11-15', '12315544411');
INSERT INTO vendas.ex_cliente VALUES (4, 'Carlos Eduardo', '1924-10-25', '42515541212');
INSERT INTO vendas.ex_cliente VALUES (5, 'Maria Cristina Goes', '1981-11-03', '67715541212');
INSERT INTO vendas.ex_cliente VALUES (6, 'Ruan Manoel Fanjo', '1983-12-06', '32415541212');
INSERT INTO vendas.ex_cliente VALUES (7, 'Patrícia Marques', '1944-02-01', '77715541212');


--
-- Data for Name: ex_itempedido; Type: TABLE DATA; Schema: vendas; Owner: -
--

INSERT INTO vendas.ex_itempedido VALUES (1, 1, 10.90, 1, 1);
INSERT INTO vendas.ex_itempedido VALUES (1, 2, 389.10, 1, 3);
INSERT INTO vendas.ex_itempedido VALUES (2, 1, 10.90, 1, 1);
INSERT INTO vendas.ex_itempedido VALUES (3, 1, 10.90, 1, 1);
INSERT INTO vendas.ex_itempedido VALUES (4, 1, 10.90, 1, 1);
INSERT INTO vendas.ex_itempedido VALUES (4, 2, 15.90, 2, 2);
INSERT INTO vendas.ex_itempedido VALUES (4, 3, 25.50, 1, 4);
INSERT INTO vendas.ex_itempedido VALUES (4, 4, 100.90, 1, 5);
INSERT INTO vendas.ex_itempedido VALUES (5, 1, 100.90, 1, 5);
INSERT INTO vendas.ex_itempedido VALUES (6, 1, 25.50, 2, 4);


--
-- Data for Name: ex_pedido; Type: TABLE DATA; Schema: vendas; Owner: -
--

INSERT INTO vendas.ex_pedido VALUES (1, 1, '2024-04-01', '00001', 400.00);
INSERT INTO vendas.ex_pedido VALUES (2, 2, '2024-04-01', '00002', 10.90);
INSERT INTO vendas.ex_pedido VALUES (3, 2, '2024-04-01', '00003', 21.80);
INSERT INTO vendas.ex_pedido VALUES (4, 3, '2024-05-01', '00004', 169.10);
INSERT INTO vendas.ex_pedido VALUES (5, 4, '2024-05-01', '00005', 100.90);
INSERT INTO vendas.ex_pedido VALUES (6, 6, '2024-05-02', '00006', 51.35);


--
-- Data for Name: ex_produto; Type: TABLE DATA; Schema: vendas; Owner: -
--

INSERT INTO vendas.ex_produto VALUES (1, 'Mouse');
INSERT INTO vendas.ex_produto VALUES (2, 'Teclado');
INSERT INTO vendas.ex_produto VALUES (3, 'Monitor LCD');
INSERT INTO vendas.ex_produto VALUES (4, 'Caixas Acústicas');
INSERT INTO vendas.ex_produto VALUES (5, 'Scanner de Mesa');


--
-- Name: ex_cliente pk_ex_cliente; Type: CONSTRAINT; Schema: vendas; Owner: -
--

ALTER TABLE ONLY vendas.ex_cliente
    ADD CONSTRAINT pk_ex_cliente PRIMARY KEY (codcliente);


--
-- Name: ex_pedido pk_ex_pedido; Type: CONSTRAINT; Schema: vendas; Owner: -
--

ALTER TABLE ONLY vendas.ex_pedido
    ADD CONSTRAINT pk_ex_pedido PRIMARY KEY (codpedido);


--
-- Name: ex_produto pk_ex_produto; Type: CONSTRAINT; Schema: vendas; Owner: -
--

ALTER TABLE ONLY vendas.ex_produto
    ADD CONSTRAINT pk_ex_produto PRIMARY KEY (codproduto);


--
-- Name: ex_itempedido pk_itempedido; Type: CONSTRAINT; Schema: vendas; Owner: -
--

ALTER TABLE ONLY vendas.ex_itempedido
    ADD CONSTRAINT pk_itempedido PRIMARY KEY (codpedido, numeroitem);


--
-- Name: ex_itempedido fk_codpedido; Type: FK CONSTRAINT; Schema: vendas; Owner: -
--

ALTER TABLE ONLY vendas.ex_itempedido
    ADD CONSTRAINT fk_codpedido FOREIGN KEY (codpedido) REFERENCES vendas.ex_pedido(codpedido);


--
-- Name: ex_itempedido fk_itempedido_produto; Type: FK CONSTRAINT; Schema: vendas; Owner: -
--

ALTER TABLE ONLY vendas.ex_itempedido
    ADD CONSTRAINT fk_itempedido_produto FOREIGN KEY (codproduto) REFERENCES vendas.ex_produto(codproduto);


--
-- Name: ex_pedido pk_ex_pedido_cliente; Type: FK CONSTRAINT; Schema: vendas; Owner: -
--

ALTER TABLE ONLY vendas.ex_pedido
    ADD CONSTRAINT pk_ex_pedido_cliente FOREIGN KEY (codcliente) REFERENCES vendas.ex_cliente(codcliente);


--
-- PostgreSQL database dump complete
--
