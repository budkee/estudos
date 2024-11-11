drop table if exists cliente cascade;
drop table if exists operacao cascade;

CREATE TABLE cliente (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(50),
    investimento NUMERIC
);

CREATE TABLE operacao (
    id INTEGER PRIMARY KEY,
    cliid INTEGER,
    mes INTEGER,
    lucro NUMERIC, 
    foreign key (cliid) references cliente(id)
);

INSERT INTO cliente (id, nome, investimento) values
(1, 'Daniel', 500 ),
(2, 'Oliveira', 2000),
(3, 'Lucas', 1000);

INSERT INTO operacao (id, cliid, mes, lucro) values
( 1,    1,  1,  230 ),
( 2,    2,  1,  1000),
( 3,    2,  2,  1000),
( 4,    3,  1,  100 ),
( 5,    3,  2,  300 ),
( 6,    3,  3,  900 ),
( 7,    3,  4,  400 );
