drop table if exists produto;
CREATE TABLE produto (
  id NUMERIC PRIMARY KEY,
  nome CHARACTER VARYING (255),
  quantidade NUMERIC,
  preco NUMERIC
);

INSERT INTO produto (id, nome, quantidade, preco)
VALUES 
  (1, 'Two-door wardrobe',  100,  80),
  (2, 'Dining table', 1000, 560),
  (3, 'Towel holder', 10000,  4.50),
  (4, 'Computer desk',  350,  200),
  (5, 'Chair',  3000, 210.64),
  (6, 'Single bed', 750,  5);