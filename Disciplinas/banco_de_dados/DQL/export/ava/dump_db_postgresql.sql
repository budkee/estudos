--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2 (Debian 12.2-2.pgdg100+1)
-- Dumped by pg_dump version 12.2 (Debian 12.2-2.pgdg100+1)


--
-- Name: departamento; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.departamento (
    dnome character varying(255) NOT NULL,
    dnumero integer NOT NULL,
    gerssn integer,
    gerdatainicio date,
    CONSTRAINT departamento_dnumero_check CHECK ((dnumero > 0))
);


--
-- Name: dependente; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.dependente (
    essn integer NOT NULL,
    nome_dependente character varying(255) NOT NULL,
    sexo character(1),
    datanasc date,
    parentesco character varying(255),
    CONSTRAINT dependente_sexo_check CHECK ((sexo = ANY (ARRAY['F'::bpchar, 'M'::bpchar])))
);


--
-- Name: depto_localizacoes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.depto_localizacoes (
    dnumero integer NOT NULL,
    dlocalizacao character varying(255) NOT NULL
);


--
-- Name: empregado; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.empregado (
    pnome character varying(255) NOT NULL,
    minicial character(1),
    unome character varying(255) NOT NULL,
    ssn integer NOT NULL,
    datanasc date,
    endereco character varying(255),
    sexo character(2),
    salario numeric NOT NULL,
    superssn integer,
    dno integer,
    CONSTRAINT empregado_dno_check CHECK ((dno > 0)),
    CONSTRAINT empregado_salario_check CHECK ((salario > (0)::numeric)),
    CONSTRAINT empregado_sexo_check CHECK ((sexo = ANY (ARRAY['F'::bpchar, 'M'::bpchar])))
);


--
-- Name: projeto; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.projeto (
    pjnome character varying(255),
    pnumero integer NOT NULL,
    plocalizacao character varying(255),
    dnum integer
);


--
-- Name: trabalha_em; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.trabalha_em (
    essn integer NOT NULL,
    pno integer NOT NULL,
    horas real
);


--
-- Data for Name: departamento; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.departamento (dnome, dnumero, gerssn, gerdatainicio) VALUES ('Pesquisa', 5, 333445555, '1988-05-22');
INSERT INTO public.departamento (dnome, dnumero, gerssn, gerdatainicio) VALUES ('Administração', 4, 987654321, '1995-01-01');
INSERT INTO public.departamento (dnome, dnumero, gerssn, gerdatainicio) VALUES ('Sede administrativa', 1, 888665555, '1981-06-19');
INSERT INTO public.departamento (dnome, dnumero, gerssn, gerdatainicio) VALUES ('Inovação', 7, NULL, '1980-06-30');


--
-- Data for Name: dependente; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.dependente (essn, nome_dependente, sexo, datanasc, parentesco) VALUES (333445555, 'Alice', 'F', '1986-04-05', 'FILHA');
INSERT INTO public.dependente (essn, nome_dependente, sexo, datanasc, parentesco) VALUES (333445555, 'Theodore', 'M', '1983-10-25', 'FILHO');
INSERT INTO public.dependente (essn, nome_dependente, sexo, datanasc, parentesco) VALUES (333445555, 'Joy', 'F', '1958-05-03', 'CÔNJUGE');
INSERT INTO public.dependente (essn, nome_dependente, sexo, datanasc, parentesco) VALUES (987654321, 'Abner', 'M', '1942-02-28', 'CÔNJUGE');
INSERT INTO public.dependente (essn, nome_dependente, sexo, datanasc, parentesco) VALUES (123456789, 'Michael', 'M', '1988-01-04', 'FILHO');
INSERT INTO public.dependente (essn, nome_dependente, sexo, datanasc, parentesco) VALUES (123456789, 'Alice', 'F', '1988-12-30', 'FILHA');
INSERT INTO public.dependente (essn, nome_dependente, sexo, datanasc, parentesco) VALUES (123456789, 'Elizabeth', 'F', '1967-05-05', 'CÔNJUGE');
INSERT INTO public.dependente (essn, nome_dependente, sexo, datanasc, parentesco) VALUES (453453453, 'John', 'M', '1960-12-12', 'CÔNJUNGE');
INSERT INTO public.dependente (essn, nome_dependente, sexo, datanasc, parentesco) VALUES (333445555, 'Alicia', 'F', '2013-05-27', 'Neta');


--
-- Data for Name: depto_localizacoes; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.depto_localizacoes (dnumero, dlocalizacao) VALUES (1, 'Houston');
INSERT INTO public.depto_localizacoes (dnumero, dlocalizacao) VALUES (4, 'Stafford');
INSERT INTO public.depto_localizacoes (dnumero, dlocalizacao) VALUES (5, 'Bellaire');
INSERT INTO public.depto_localizacoes (dnumero, dlocalizacao) VALUES (5, 'Sugarland');
INSERT INTO public.depto_localizacoes (dnumero, dlocalizacao) VALUES (5, 'Houston');


--
-- Data for Name: empregado; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.empregado (pnome, minicial, unome, ssn, datanasc, endereco, sexo, salario, superssn, dno) VALUES ('Alicia', 'J', 'Zelaya', 999887777, '1968-01-19', '3321 Castle, Spring, TX', 'F ', 2500, 943775543, 4);
INSERT INTO public.empregado (pnome, minicial, unome, ssn, datanasc, endereco, sexo, salario, superssn, dno) VALUES ('John', 'B', 'Smith', 123456789, '1965-01-09', '731 Fondren, Houston, Tx', 'M ', 30000, 333445555, 5);
INSERT INTO public.empregado (pnome, minicial, unome, ssn, datanasc, endereco, sexo, salario, superssn, dno) VALUES ('Ramesh', 'K', 'Narayan', 666884444, '1962-09-15', '975 Fire Oak, Humble, TX', 'M ', 38000, 333445555, 5);
INSERT INTO public.empregado (pnome, minicial, unome, ssn, datanasc, endereco, sexo, salario, superssn, dno) VALUES ('Joyce', 'A', 'English', 453453453, '1972-07-31', '5631 Rice, Houston, TX', 'F ', 25000, 333445555, 5);
INSERT INTO public.empregado (pnome, minicial, unome, ssn, datanasc, endereco, sexo, salario, superssn, dno) VALUES ('Franklin', 'T', 'Wong', 333445555, '1955-12-08', '638 Voss, Houston, Tx', 'M ', 40000, 888665555, 5);
INSERT INTO public.empregado (pnome, minicial, unome, ssn, datanasc, endereco, sexo, salario, superssn, dno) VALUES ('Jennifer', 'S', 'Wallace', 987654321, '1941-06-20', '291 Berry, Bellarie, TX', 'F ', 43000, 888665555, 4);
INSERT INTO public.empregado (pnome, minicial, unome, ssn, datanasc, endereco, sexo, salario, superssn, dno) VALUES ('Ahmad', 'V', 'Jabbar', 987987987, '1969-03-29', '980 Dallas, Houston, TX', 'M ', 25000, 987654321, 4);
INSERT INTO public.empregado (pnome, minicial, unome, ssn, datanasc, endereco, sexo, salario, superssn, dno) VALUES ('James', 'E', 'Borg', 888665555, '1937-11-10', '450 Stone, Houston, TX', 'M ', 55000, NULL, 1);
INSERT INTO public.empregado (pnome, minicial, unome, ssn, datanasc, endereco, sexo, salario, superssn, dno) VALUES ('Robert', 'F', 'Scott', 943775543, '1942-07-21', '2365 Newcastle Rd, Bellaire, TX', 'M ', 58000, 888665555, 1);


--
-- Data for Name: projeto; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.projeto (pjnome, pnumero, plocalizacao, dnum) VALUES ('ProdutoX', 1, 'Bellaire', 5);
INSERT INTO public.projeto (pjnome, pnumero, plocalizacao, dnum) VALUES ('ProdutoY', 2, 'Sugarland', 5);
INSERT INTO public.projeto (pjnome, pnumero, plocalizacao, dnum) VALUES ('ProdutoZ', 3, 'Houston', 5);
INSERT INTO public.projeto (pjnome, pnumero, plocalizacao, dnum) VALUES ('Automatização', 10, 'Stafford', 4);
INSERT INTO public.projeto (pjnome, pnumero, plocalizacao, dnum) VALUES ('Reorganização', 20, 'Houston', 1);
INSERT INTO public.projeto (pjnome, pnumero, plocalizacao, dnum) VALUES ('Novos Benefícios', 30, 'Stafford', 4);


--
-- Data for Name: trabalha_em; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (999887777, 10, 5);
INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (123456789, 1, 32.5);
INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (123456789, 2, 7.5);
INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (666884444, 3, 40);
INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (453453453, 1, 20);
INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (453453453, 2, 20);
INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (333445555, 2, 10);
INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (333445555, 3, 10);
INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (333445555, 10, 10);
INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (333445555, 20, 10);
INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (999887777, 30, 30);
INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (987987987, 10, 35);
INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (987987987, 30, 5);
INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (987654321, 30, 20);
INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (987654321, 20, 15);
INSERT INTO public.trabalha_em (essn, pno, horas) VALUES (888665555, 20, 35);


--
-- Name: departamento departamento_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.departamento
    ADD CONSTRAINT departamento_pkey PRIMARY KEY (dnumero);


--
-- Name: dependente dependente_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dependente
    ADD CONSTRAINT dependente_pkey PRIMARY KEY (essn, nome_dependente);


--
-- Name: depto_localizacoes depto_localizacoes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.depto_localizacoes
    ADD CONSTRAINT depto_localizacoes_pkey PRIMARY KEY (dnumero, dlocalizacao);


--
-- Name: empregado empregado_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.empregado
    ADD CONSTRAINT empregado_pkey PRIMARY KEY (ssn);


--
-- Name: projeto projeto_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projeto
    ADD CONSTRAINT projeto_pkey PRIMARY KEY (pnumero);


--
-- Name: trabalha_em trabalha_em_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.trabalha_em
    ADD CONSTRAINT trabalha_em_pkey PRIMARY KEY (essn, pno);


--
-- Name: departamento gerente; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.departamento
    ADD CONSTRAINT gerente FOREIGN KEY (gerssn) REFERENCES public.empregado(ssn);


--
-- Name: depto_localizacoes numerodepartamento; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.depto_localizacoes
    ADD CONSTRAINT numerodepartamento FOREIGN KEY (dnumero) REFERENCES public.departamento(dnumero);


--
-- Name: projeto numerodepartamento; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projeto
    ADD CONSTRAINT numerodepartamento FOREIGN KEY (dnum) REFERENCES public.departamento(dnumero);


--
-- Name: empregado numerodepto; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.empregado
    ADD CONSTRAINT numerodepto FOREIGN KEY (dno) REFERENCES public.departamento(dnumero);


--
-- Name: trabalha_em numeroprojeto; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.trabalha_em
    ADD CONSTRAINT numeroprojeto FOREIGN KEY (pno) REFERENCES public.projeto(pnumero);


--
-- Name: dependente ssnempregado; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dependente
    ADD CONSTRAINT ssnempregado FOREIGN KEY (essn) REFERENCES public.empregado(ssn);


--
-- Name: empregado supervisor; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.empregado
    ADD CONSTRAINT supervisor FOREIGN KEY (superssn) REFERENCES public.empregado(ssn);


--
-- PostgreSQL database dump complete
--