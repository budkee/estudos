drop table if exists cliente cascade;
drop table if exists pedido cascade;

CREATE TABLE cliente (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255)
);
    
INSERT INTO cliente (id, nome, email) VALUES (1,'Doctor Who', 'doctorwho@timelords.com');
INSERT INTO cliente (id, nome, email) VALUES (2, 'Harry Potter', 'harry@potter.com');
INSERT INTO cliente (id, nome, email) VALUES (3, 'Captain Awesome', 'captain@awesome.com');

CREATE TABLE pedido (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    item VARCHAR(255),
    preco NUMERIC(10,2),
    FOREIGN KEY (cliente_id) REFERENCES cliente (id)
    );

INSERT INTO pedido (id, cliente_id, item, preco) VALUES (1, 1, 'Sonic Screwdriver', 1000.00);
INSERT INTO pedido (id, cliente_id, item, preco) VALUES (2, 2, 'High Quality Broomstick', 40.00);
INSERT INTO pedido (id, cliente_id, item, preco) VALUES (3, 1, 'TARDIS', 1000000.00);