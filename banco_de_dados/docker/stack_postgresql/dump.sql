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
-- Name: clinica; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA clinica;


--
-- Name: vendas; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA vendas;


--
-- Name: fn_consultas_agendadas(integer); Type: FUNCTION; Schema: public; Owner: -
--

CREATE FUNCTION public.fn_consultas_agendadas(codpaciente integer) RETURNS TABLE(codigo integer, data date)
    LANGUAGE plpgsql
    AS $$

BEGIN
	select codigo, data, codpaciente
	from clinica.consulta as con
	where con.data >= current_date;
END;
$$;


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: ambulatorio; Type: TABLE; Schema: clinica; Owner: -
--

CREATE TABLE clinica.ambulatorio (
    numero integer NOT NULL,
    andar smallint NOT NULL,
    capacidade smallint NOT NULL
);


--
-- Name: ambulatorio_numero_seq; Type: SEQUENCE; Schema: clinica; Owner: -
--

CREATE SEQUENCE clinica.ambulatorio_numero_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ambulatorio_numero_seq; Type: SEQUENCE OWNED BY; Schema: clinica; Owner: -
--

ALTER SEQUENCE clinica.ambulatorio_numero_seq OWNED BY clinica.ambulatorio.numero;


--
-- Name: consulta; Type: TABLE; Schema: clinica; Owner: -
--

CREATE TABLE clinica.consulta (
    codigo integer NOT NULL,
    codmedico integer NOT NULL,
    codpaciente integer NOT NULL,
    data date,
    hora time without time zone
);


--
-- Name: consulta_codigo_seq; Type: SEQUENCE; Schema: clinica; Owner: -
--

CREATE SEQUENCE clinica.consulta_codigo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: consulta_codigo_seq; Type: SEQUENCE OWNED BY; Schema: clinica; Owner: -
--

ALTER SEQUENCE clinica.consulta_codigo_seq OWNED BY clinica.consulta.codigo;


--
-- Name: funcionario; Type: TABLE; Schema: clinica; Owner: -
--

CREATE TABLE clinica.funcionario (
    codigo integer NOT NULL,
    nome character varying(40) NOT NULL,
    idade smallint NOT NULL,
    cpf character(14) NOT NULL,
    cidade character varying(30) NOT NULL,
    salario double precision NOT NULL
);


--
-- Name: funcionario_codigo_seq; Type: SEQUENCE; Schema: clinica; Owner: -
--

CREATE SEQUENCE clinica.funcionario_codigo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: funcionario_codigo_seq; Type: SEQUENCE OWNED BY; Schema: clinica; Owner: -
--

ALTER SEQUENCE clinica.funcionario_codigo_seq OWNED BY clinica.funcionario.codigo;


--
-- Name: hist_med_amb; Type: TABLE; Schema: clinica; Owner: -
--

CREATE TABLE clinica.hist_med_amb (
    "codMedico" integer,
    "codOldAmbulatorio" integer NOT NULL,
    "codNewAmbulatorio" integer NOT NULL,
    "dataAlteracao" date
);


--
-- Name: medico; Type: TABLE; Schema: clinica; Owner: -
--

CREATE TABLE clinica.medico (
    codigo integer NOT NULL,
    nome character varying(40) NOT NULL,
    idade smallint NOT NULL,
    cpf character(14) NOT NULL,
    cidade character varying(30) NOT NULL,
    especialidade character varying(50) NOT NULL,
    numambulatorio integer NOT NULL
);


--
-- Name: medico_codigo_seq; Type: SEQUENCE; Schema: clinica; Owner: -
--

CREATE SEQUENCE clinica.medico_codigo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: medico_codigo_seq; Type: SEQUENCE OWNED BY; Schema: clinica; Owner: -
--

ALTER SEQUENCE clinica.medico_codigo_seq OWNED BY clinica.medico.codigo;


--
-- Name: paciente; Type: TABLE; Schema: clinica; Owner: -
--

CREATE TABLE clinica.paciente (
    codigo integer NOT NULL,
    nome character varying(40) NOT NULL,
    idade smallint NOT NULL,
    cpf character(14) NOT NULL,
    cidade character varying(30) NOT NULL,
    doenca character varying(50) NOT NULL
);


--
-- Name: paciente_codigo_seq; Type: SEQUENCE; Schema: clinica; Owner: -
--

CREATE SEQUENCE clinica.paciente_codigo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: paciente_codigo_seq; Type: SEQUENCE OWNED BY; Schema: clinica; Owner: -
--

ALTER SEQUENCE clinica.paciente_codigo_seq OWNED BY clinica.paciente.codigo;


--
-- Name: top_10_dow; Type: VIEW; Schema: clinica; Owner: -
--

CREATE VIEW clinica.top_10_dow AS
 SELECT codmedico,
    dia_semana
   FROM ( SELECT con.codmedico,
            con.codigo,
            con.data,
            EXTRACT(dow FROM con.data) AS dia_semana
           FROM clinica.consulta con) consulta
  WHERE ((dia_semana = (0)::numeric) OR (dia_semana = (6)::numeric))
 LIMIT 10;


--
-- Name: v1_pacientes; Type: VIEW; Schema: clinica; Owner: -
--

CREATE VIEW clinica.v1_pacientes AS
SELECT
    NULL::integer AS codigo,
    NULL::character varying(40) AS nome,
    NULL::character varying(50) AS doenca,
    NULL::smallint AS idade;


--
-- Name: cliente; Type: TABLE; Schema: vendas; Owner: -
--

CREATE TABLE vendas.cliente (
    codigo integer NOT NULL,
    nome character varying(50) NOT NULL,
    telefone character(10) NOT NULL
);


--
-- Name: cliente_codigo_seq; Type: SEQUENCE; Schema: vendas; Owner: -
--

CREATE SEQUENCE vendas.cliente_codigo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: cliente_codigo_seq; Type: SEQUENCE OWNED BY; Schema: vendas; Owner: -
--

ALTER SEQUENCE vendas.cliente_codigo_seq OWNED BY vendas.cliente.codigo;


--
-- Name: venda; Type: TABLE; Schema: vendas; Owner: -
--

CREATE TABLE vendas.venda (
    codigo integer NOT NULL,
    data date DEFAULT CURRENT_DATE NOT NULL,
    codcliente integer NOT NULL,
    codvendedor integer NOT NULL,
    valor numeric(12,2) NOT NULL
);


--
-- Name: venda_codigo_seq; Type: SEQUENCE; Schema: vendas; Owner: -
--

CREATE SEQUENCE vendas.venda_codigo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: venda_codigo_seq; Type: SEQUENCE OWNED BY; Schema: vendas; Owner: -
--

ALTER SEQUENCE vendas.venda_codigo_seq OWNED BY vendas.venda.codigo;


--
-- Name: vendedor; Type: TABLE; Schema: vendas; Owner: -
--

CREATE TABLE vendas.vendedor (
    codigo integer NOT NULL,
    nome character varying(50) NOT NULL,
    ctps character varying(20) NOT NULL,
    situacao character(1) DEFAULT 'A'::bpchar NOT NULL
);


--
-- Name: vendedor_codigo_seq; Type: SEQUENCE; Schema: vendas; Owner: -
--

CREATE SEQUENCE vendas.vendedor_codigo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: vendedor_codigo_seq; Type: SEQUENCE OWNED BY; Schema: vendas; Owner: -
--

ALTER SEQUENCE vendas.vendedor_codigo_seq OWNED BY vendas.vendedor.codigo;


--
-- Name: vw_vendedores_ativos; Type: VIEW; Schema: vendas; Owner: -
--

CREATE VIEW vendas.vw_vendedores_ativos AS
 SELECT vr.codigo,
    v.data,
    v.valor,
    vr.situacao
   FROM (vendas.vendedor vr
     LEFT JOIN vendas.venda v ON ((v.codvendedor = vr.codigo)))
  WHERE ((v.data >= (CURRENT_DATE - 30)) AND (vr.situacao = 'A'::bpchar));


--
-- Name: ambulatorio numero; Type: DEFAULT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.ambulatorio ALTER COLUMN numero SET DEFAULT nextval('clinica.ambulatorio_numero_seq'::regclass);


--
-- Name: consulta codigo; Type: DEFAULT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.consulta ALTER COLUMN codigo SET DEFAULT nextval('clinica.consulta_codigo_seq'::regclass);


--
-- Name: funcionario codigo; Type: DEFAULT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.funcionario ALTER COLUMN codigo SET DEFAULT nextval('clinica.funcionario_codigo_seq'::regclass);


--
-- Name: medico codigo; Type: DEFAULT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.medico ALTER COLUMN codigo SET DEFAULT nextval('clinica.medico_codigo_seq'::regclass);


--
-- Name: paciente codigo; Type: DEFAULT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.paciente ALTER COLUMN codigo SET DEFAULT nextval('clinica.paciente_codigo_seq'::regclass);


--
-- Name: cliente codigo; Type: DEFAULT; Schema: vendas; Owner: -
--

ALTER TABLE ONLY vendas.cliente ALTER COLUMN codigo SET DEFAULT nextval('vendas.cliente_codigo_seq'::regclass);


--
-- Name: venda codigo; Type: DEFAULT; Schema: vendas; Owner: -
--

ALTER TABLE ONLY vendas.venda ALTER COLUMN codigo SET DEFAULT nextval('vendas.venda_codigo_seq'::regclass);


--
-- Name: vendedor codigo; Type: DEFAULT; Schema: vendas; Owner: -
--

ALTER TABLE ONLY vendas.vendedor ALTER COLUMN codigo SET DEFAULT nextval('vendas.vendedor_codigo_seq'::regclass);


--
-- Data for Name: ambulatorio; Type: TABLE DATA; Schema: clinica; Owner: -
--

INSERT INTO clinica.ambulatorio VALUES (1, 1, 30);
INSERT INTO clinica.ambulatorio VALUES (2, 1, 50);
INSERT INTO clinica.ambulatorio VALUES (3, 2, 40);
INSERT INTO clinica.ambulatorio VALUES (4, 2, 25);
INSERT INTO clinica.ambulatorio VALUES (5, 2, 55);


--
-- Data for Name: consulta; Type: TABLE DATA; Schema: clinica; Owner: -
--

INSERT INTO clinica.consulta VALUES (1, 1, 1, '2024-06-12', '14:00:00');
INSERT INTO clinica.consulta VALUES (2, 1, 4, '2015-10-13', '10:00:00');
INSERT INTO clinica.consulta VALUES (3, 2, 1, '2014-10-13', '09:00:00');
INSERT INTO clinica.consulta VALUES (4, 2, 2, '2015-10-13', '11:00:00');
INSERT INTO clinica.consulta VALUES (5, 2, 3, '2014-11-21', '23:50:00');
INSERT INTO clinica.consulta VALUES (6, 2, 4, '2015-10-14', '17:00:00');
INSERT INTO clinica.consulta VALUES (7, 3, 1, '2014-10-19', '18:00:00');
INSERT INTO clinica.consulta VALUES (8, 3, 3, '2010-10-12', '10:00:00');
INSERT INTO clinica.consulta VALUES (9, 3, 4, '2024-06-19', '13:00:00');
INSERT INTO clinica.consulta VALUES (10, 4, 4, '2024-06-20', '13:00:00');
INSERT INTO clinica.consulta VALUES (11, 4, 4, '2024-06-22', '19:30:00');


--
-- Data for Name: funcionario; Type: TABLE DATA; Schema: clinica; Owner: -
--

INSERT INTO clinica.funcionario VALUES (1, 'Rita', 32, '12510100020   ', 'São José', 1200);
INSERT INTO clinica.funcionario VALUES (2, 'Maria', 55, '12510100360   ', 'Palhoça', 1220);
INSERT INTO clinica.funcionario VALUES (3, 'Caio', 45, '12510147800   ', 'Florianópolis', 1100);
INSERT INTO clinica.funcionario VALUES (4, 'Carlos', 44, '12510105800   ', 'Florianópolis', 1200);
INSERT INTO clinica.funcionario VALUES (5, 'Paula', 33, '12510100000   ', 'Florianópolis', 2500);


--
-- Data for Name: hist_med_amb; Type: TABLE DATA; Schema: clinica; Owner: -
--



--
-- Data for Name: medico; Type: TABLE DATA; Schema: clinica; Owner: -
--

INSERT INTO clinica.medico VALUES (1, 'João', 40, '10000100000   ', 'Florianopolis', 'ortopedia', 1);
INSERT INTO clinica.medico VALUES (2, 'Graziele', 42, '11100100000   ', 'Blumenau', 'traumatologia', 2);
INSERT INTO clinica.medico VALUES (3, 'Pedro', 51, '10001101000   ', 'São José', 'pediatria', 2);
INSERT INTO clinica.medico VALUES (4, 'Leandro', 28, '11110100000   ', 'Joinville', 'ortopedia', 1);
INSERT INTO clinica.medico VALUES (5, 'Marcia', 33, '10110100000   ', 'Biguaçu', 'neurologia', 3);


--
-- Data for Name: paciente; Type: TABLE DATA; Schema: clinica; Owner: -
--

INSERT INTO clinica.paciente VALUES (1, 'Ana', 20, '220100000     ', 'Florianópolis', 'gripe');
INSERT INTO clinica.paciente VALUES (2, 'Ricardo', 24, '8110100000    ', 'Palhoça', 'fratura');
INSERT INTO clinica.paciente VALUES (3, 'Lucia', 30, '17910100000   ', 'Biguaçu', 'tendinite');
INSERT INTO clinica.paciente VALUES (4, 'Fernando', 28, '12510100000   ', 'Joinville', 'sarampo');


--
-- Data for Name: cliente; Type: TABLE DATA; Schema: vendas; Owner: -
--

INSERT INTO vendas.cliente VALUES (1, 'Fulano', '1111111111');
INSERT INTO vendas.cliente VALUES (2, 'Beltrano', '2222222222');
INSERT INTO vendas.cliente VALUES (3, 'Sicrano', '3333333333');


--
-- Data for Name: venda; Type: TABLE DATA; Schema: vendas; Owner: -
--

INSERT INTO vendas.venda VALUES (1, '2024-06-06', 1, 1, 200.00);
INSERT INTO vendas.venda VALUES (2, '2012-06-09', 2, 2, 100.00);
INSERT INTO vendas.venda VALUES (3, '2013-02-01', 3, 1, 1200.00);
INSERT INTO vendas.venda VALUES (4, '2010-05-30', 2, 3, 1700.00);
INSERT INTO vendas.venda VALUES (5, '2024-02-01', 1, 4, 1900.00);
INSERT INTO vendas.venda VALUES (6, '2024-06-13', 1, 4, 500.00);
INSERT INTO vendas.venda VALUES (7, '2024-03-01', 2, 1, 700.00);
INSERT INTO vendas.venda VALUES (8, '2011-03-14', 1, 2, 350.00);
INSERT INTO vendas.venda VALUES (9, '2012-03-22', 3, 1, 900.00);
INSERT INTO vendas.venda VALUES (10, '2010-03-01', 1, 3, 5000.00);
INSERT INTO vendas.venda VALUES (11, '2014-11-03', 3, 1, 1000.00);
INSERT INTO vendas.venda VALUES (12, '2024-06-01', 1, 3, 2000.00);
INSERT INTO vendas.venda VALUES (13, '2012-04-26', 1, 1, 3000.00);
INSERT INTO vendas.venda VALUES (14, '2010-08-28', 1, 4, 4000.00);


--
-- Data for Name: vendedor; Type: TABLE DATA; Schema: vendas; Owner: -
--

INSERT INTO vendas.vendedor VALUES (1, 'Jose', '1111', 'A');
INSERT INTO vendas.vendedor VALUES (2, 'Maria', '2222', 'I');
INSERT INTO vendas.vendedor VALUES (3, 'Ana', '3333', 'A');
INSERT INTO vendas.vendedor VALUES (4, 'Henrique', '4444', 'I');
INSERT INTO vendas.vendedor VALUES (5, 'Pedro', '5555', 'I');


--
-- Name: ambulatorio_numero_seq; Type: SEQUENCE SET; Schema: clinica; Owner: -
--

SELECT pg_catalog.setval('clinica.ambulatorio_numero_seq', 1, false);


--
-- Name: consulta_codigo_seq; Type: SEQUENCE SET; Schema: clinica; Owner: -
--

SELECT pg_catalog.setval('clinica.consulta_codigo_seq', 1, false);


--
-- Name: funcionario_codigo_seq; Type: SEQUENCE SET; Schema: clinica; Owner: -
--

SELECT pg_catalog.setval('clinica.funcionario_codigo_seq', 1, false);


--
-- Name: medico_codigo_seq; Type: SEQUENCE SET; Schema: clinica; Owner: -
--

SELECT pg_catalog.setval('clinica.medico_codigo_seq', 1, false);


--
-- Name: paciente_codigo_seq; Type: SEQUENCE SET; Schema: clinica; Owner: -
--

SELECT pg_catalog.setval('clinica.paciente_codigo_seq', 1, false);


--
-- Name: cliente_codigo_seq; Type: SEQUENCE SET; Schema: vendas; Owner: -
--

SELECT pg_catalog.setval('vendas.cliente_codigo_seq', 3, true);


--
-- Name: venda_codigo_seq; Type: SEQUENCE SET; Schema: vendas; Owner: -
--

SELECT pg_catalog.setval('vendas.venda_codigo_seq', 14, true);


--
-- Name: vendedor_codigo_seq; Type: SEQUENCE SET; Schema: vendas; Owner: -
--

SELECT pg_catalog.setval('vendas.vendedor_codigo_seq', 5, true);


--
-- Name: ambulatorio ambulatorio_pkey; Type: CONSTRAINT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.ambulatorio
    ADD CONSTRAINT ambulatorio_pkey PRIMARY KEY (numero);


--
-- Name: consulta consulta_pkey; Type: CONSTRAINT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.consulta
    ADD CONSTRAINT consulta_pkey PRIMARY KEY (codigo);


--
-- Name: funcionario funcionario_cpf_key; Type: CONSTRAINT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.funcionario
    ADD CONSTRAINT funcionario_cpf_key UNIQUE (cpf);


--
-- Name: funcionario funcionario_pkey; Type: CONSTRAINT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.funcionario
    ADD CONSTRAINT funcionario_pkey PRIMARY KEY (codigo);


--
-- Name: hist_med_amb hist_med_amb_pkey; Type: CONSTRAINT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.hist_med_amb
    ADD CONSTRAINT hist_med_amb_pkey PRIMARY KEY ("codNewAmbulatorio");


--
-- Name: medico medico_cpf_key; Type: CONSTRAINT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.medico
    ADD CONSTRAINT medico_cpf_key UNIQUE (cpf);


--
-- Name: medico medico_pkey; Type: CONSTRAINT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.medico
    ADD CONSTRAINT medico_pkey PRIMARY KEY (codigo);


--
-- Name: paciente paciente_cpf_key; Type: CONSTRAINT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.paciente
    ADD CONSTRAINT paciente_cpf_key UNIQUE (cpf);


--
-- Name: paciente paciente_pkey; Type: CONSTRAINT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.paciente
    ADD CONSTRAINT paciente_pkey PRIMARY KEY (codigo);


--
-- Name: cliente cliente_pkey; Type: CONSTRAINT; Schema: vendas; Owner: -
--

ALTER TABLE ONLY vendas.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (codigo);


--
-- Name: venda venda_pkey; Type: CONSTRAINT; Schema: vendas; Owner: -
--

ALTER TABLE ONLY vendas.venda
    ADD CONSTRAINT venda_pkey PRIMARY KEY (codigo);


--
-- Name: vendedor vendedor_pkey; Type: CONSTRAINT; Schema: vendas; Owner: -
--

ALTER TABLE ONLY vendas.vendedor
    ADD CONSTRAINT vendedor_pkey PRIMARY KEY (codigo);


--
-- Name: v1_pacientes _RETURN; Type: RULE; Schema: clinica; Owner: -
--

CREATE OR REPLACE VIEW clinica.v1_pacientes AS
 SELECT codigo,
    nome,
    doenca,
    idade
   FROM clinica.paciente p
  WHERE ((idade > 25) AND ((doenca)::text = ANY ((ARRAY['tendinite'::character varying, 'gripe'::character varying, 'sarampo'::character varying])::text[])))
  GROUP BY codigo;


--
-- Name: consulta consulta_codmedico_fkey; Type: FK CONSTRAINT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.consulta
    ADD CONSTRAINT consulta_codmedico_fkey FOREIGN KEY (codmedico) REFERENCES clinica.medico(codigo);


--
-- Name: consulta consulta_codpaciente_fkey; Type: FK CONSTRAINT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.consulta
    ADD CONSTRAINT consulta_codpaciente_fkey FOREIGN KEY (codpaciente) REFERENCES clinica.paciente(codigo);


--
-- Name: medico medico_numambulatorio_fkey; Type: FK CONSTRAINT; Schema: clinica; Owner: -
--

ALTER TABLE ONLY clinica.medico
    ADD CONSTRAINT medico_numambulatorio_fkey FOREIGN KEY (numambulatorio) REFERENCES clinica.ambulatorio(numero);


--
-- Name: venda venda_codcliente_fkey; Type: FK CONSTRAINT; Schema: vendas; Owner: -
--

ALTER TABLE ONLY vendas.venda
    ADD CONSTRAINT venda_codcliente_fkey FOREIGN KEY (codcliente) REFERENCES vendas.cliente(codigo);


--
-- Name: venda venda_codvendedor_fkey; Type: FK CONSTRAINT; Schema: vendas; Owner: -
--

ALTER TABLE ONLY vendas.venda
    ADD CONSTRAINT venda_codvendedor_fkey FOREIGN KEY (codvendedor) REFERENCES vendas.vendedor(codigo);


--
-- PostgreSQL database dump complete
--

