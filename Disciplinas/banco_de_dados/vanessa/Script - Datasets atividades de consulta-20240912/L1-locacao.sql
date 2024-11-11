drop table if exists locacao cascade;
drop table if exists cliente cascade;

CREATE TABLE cliente (
  id integer PRIMARY KEY,
  nome varchar(50),
  rua varchar(50),
  cidade varchar(50)
);

CREATE TABLE locacao (
  id integer PRIMARY KEY,
  data date,
  id_cliente integer,
  FOREIGN KEY (id_cliente) REFERENCES cliente (id)
);

INSERT INTO cliente (id, nome, rua, cidade)
VALUES
  (1, 'Giovanna Goncalves Oliveira',  'Rua Mato Grosso',  'Canoas'),
  (2, 'Kauã Azevedo Ribeiro', 'Travessa Ibiá',  'Uberlândia'),
  (3, 'Rebeca Barbosa Santos',  'Rua Observatório Meteorológico', 'Salvador'),
  (4, 'Sarah Carvalho Correia', 'Rua Antônio Carlos da Silva',  'Apucarana'),
  (5, 'João Almeida Lima',  'Rua Rio Taiuva', 'Ponta Grossa'),
  (6, 'Diogo Melo Dias',  'Rua Duzentos e Cinqüenta', 'Várzea Grande');
  

INSERT INTO locacao (id , data, id_cliente)
VALUES
  (1, '2016-09-10', 3),
  (2, '2016-02-09', 1),
  (3, '2016-02-08', 4),
  (4, '2015-02-09', 2),
  (5, '2016-02-03', 6),
  (6, '2016-04-04', 4);