CREATE TABLE BLOCO 
(	IdBloco		INT,
    NomeBloco	VARCHAR(15),
    Anofund		INT,
	PRIMARY KEY (IdBloco)
);

CREATE TABLE PAIS 
(	Sigla		VARCHAR(15),
    SiglaNet	VARCHAR(15),
    Nome		VARCHAR(15),
    Area		VARCHAR(15),
    Pop			INT,
    Continente	VARCHAR(15),
    BRIC		VARCHAR(15),
    NomeIngles	VARCHAR(15),
	PRIMARY KEY (Sigla)
);

CREATE TABLE BLOCO_PAIS 
(	Sigla	VARCHAR(15),
    IdBloco	INT,
 	PRIMARY KEY (Sigla, IdBloco),
 	FOREIGN KEY (IdBloco) REFERENCES BLOCO(IdBloco),
 	FOREIGN KEY (Sigla) REFERENCES PAIS(Sigla)
);

CREATE TABLE IDIOMA 
(	Sigla	VARCHAR(15),
    Idioma	VARCHAR(15),
	PRIMARY KEY (Sigla, Idioma),
  	FOREIGN KEY (Sigla) REFERENCES PAIS(Sigla)
);

CREATE TABLE PIB 
(	Sigla	VARCHAR(15),
    Ano 	INT,
    Valor	INT,
	PRIMARY KEY (Sigla, Ano),
  	FOREIGN KEY (Sigla) REFERENCES PAIS(Sigla)
);

CREATE TABLE PRODUTO
(	CodProd			INT,
    NomeProd		VARCHAR(15),
    Unidade			INT,
    DescrProduto	VARCHAR(15),
    TipoProd		VARCHAR(15),
    Class			VARCHAR(15),
	PRIMARY KEY (CodProd)
);

CREATE TABLE HISTVALOR
(	idProduto	INT,
    Data		DATE,
    Valor		INT,
 	PRIMARY KEY (idProduto, Data),
  	FOREIGN KEY (idProduto) REFERENCES PRODUTO(CodProd)
);

CREATE TABLE IMP
(	Pais	VARCHAR(15),
    CodProd	INT,
    Ano		INT, 
    Quant	INT, 
    Valor	INT,
 	PRIMARY KEY (Pais, CodProd, Ano),
  	FOREIGN KEY (CodProd) REFERENCES Produto(CodProd)
);

CREATE TABLE EXP
(	Pais	VARCHAR(15),
    CodProd	INT,
    Ano		INT, 
    Quant	INT, 
    Valor	INT,
 	PRIMARY KEY (Pais, CodProd, Ano),
  	FOREIGN KEY (CodProd) REFERENCES Produto(CodProd)
);