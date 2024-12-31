drop table if exists produto;
create table produto (
id numeric primary key,
nome varchar(50),
tipo char,
preco numeric
);

insert into produto (id, nome, tipo, preco) values (1, 'Monitor','B',0);
insert into produto (id, nome, tipo, preco) values (2, 'Headset','A',0);
insert into produto (id, nome, tipo, preco) values (3, 'PC Case','A',0);
insert into produto (id, nome, tipo, preco) values (4, 'Computer Desk','C',0);
insert into produto (id, nome, tipo, preco) values (5, 'Gaming Chair','C',0);
insert into produto (id, nome, tipo, preco) values (6, 'Mouse','A',0);