drop table if exists usuario cascade;
drop table if exists pacote cascade;

CREATE TABLE usuario(
    id  numeric PRIMARY KEY,
    nome    varchar(50),
    endereco varchar(50)
);
CREATE TABLE pacote(
    id_pacote  numeric PRIMARY KEY,
    id_usuario_envio  numeric,
    id_usuario_recibo numeric,
    cor   varchar(50),
    ano    integer,
    FOREIGN KEY (id_usuario_envio) REFERENCES usuario(id),
    FOREIGN KEY (id_usuario_recibo) REFERENCES usuario(id)  
);

INSERT INTO usuario(id,nome,endereco)
VALUES
    (1,'Edgar Codd','England'),
    (2,'Peter Chen','Taiwan'),
    (3,'Jim Gray','United States'),
    (4,'Elizabeth O''Neil','United States');

INSERT INTO pacote(id_pacote,id_usuario_envio,id_usuario_recibo,cor,ano)
VALUES
    (1,1,2,'azul',2015),
    (2,1,3,'azul',2019),
    (3,2,4,'vermelho',2019),
    (4,2,1,'verde',2018),
    (5,3,4,'vermelho',2015),
    (6,4,3,'azul',2019);