drop table if exists produto cascade;
drop table if exists fornecedor cascade;
drop table if exists categoria cascade;

CREATE TABLE fornecedor (
  id integer PRIMARY KEY,
  nome varchar(255),
  rua varchar(255),
  cidade varchar(255),
  estado char(2)
);

CREATE TABLE categoria (
  id integer PRIMARY KEY,
  nome varchar(255)
);

CREATE TABLE produto (
  id integer PRIMARY KEY,
  nome varchar (255),
  qtd_estoque integer,
  preco numeric (10,2),
  id_fornecedor integer, 
  id_categoria integer,
  FOREIGN KEY (id_fornecedor) REFERENCES fornecedor (id),
  FOREIGN KEY (id_categoria) REFERENCES categoria (id)
);


INSERT INTO fornecedor (id, nome, rua, cidade, estado)
VALUES
  (1, 'Ajax SA',  'Rua Presidente Castelo Branco',  'Porto Alegre', 'RS'),
  (2, 'Sansul SA',  'Av Brasil',  'Rio de Janeiro', 'RJ'),
  (3, 'South Chairs', 'Rua do Moinho',  'Santa Maria',  'RS'),
  (4, 'Elon Electro', 'Rua Apolo',  'São Paulo',  'SP'),
  (5, 'Mike electro', 'Rua Pedro da Cunha', 'Curitiba', 'PR'),
  (6, 'Mike', 'Rua Teodoro Sampaio', 'São Paulo', 'SP');
  
INSERT INTO categoria (id, nome)
VALUES
  (1, 'Super Luxury'),
  (2, 'Imported'),
  (3, 'Tech'),
  (4, 'Vintage'),
  (5, 'Supreme');
  
INSERT INTO produto ( id, nome, qtd_estoque, preco, id_fornecedor, id_categoria)
VALUES
  (1, 'Blue Chair', 30, 300.00, 5,  5),
  (2, 'Red Chair',  50, 2150.00,  2,  1),
  (3, 'Disney Wardrobe',  400,  829.50, 4,  1),
  (4, 'Blue Toaster', 20, 999.90, null,  1),
  (5, 'TV', 30, 3000.25,  2,  2),
  (6, 'TV Led', 30, 2000, 5,  null);