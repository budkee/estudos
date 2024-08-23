-- Database
create database ecommerce;

-- Tabelas
-- endereco
create table endereco (
    enderecoid serial not null,
    clienteid integer,
    rua varchar(100),
    cidade varchar(50),
    estado varchar(50),
    cep varchar(10),
    primary key(enderecoid)
);
-- cliente
create table cliente (
    clienteid serial not null,
    nome varchar(100),
    email varchar(100),
    telefone varchar(15),
    primary key(clienteid)
);

-- c.1. cadastro cliente
alter table cliente add column DataCadastro timestamp default current_timestamp; 

-- categoria
create table categoria (
    categoriaid serial not null,
    nome varchar(100),
    categoriapaiid integer,
    primary key (categoriaid)
);
-- pedido
create table pedido (
    pedidoid serial not null,
    clienteid integer,
    datapedido date,
    total numeric(10,2), -- (tamanho inteiro, qnt de casas decimais)
    primary key (pedidoid)
);
-- c.3. Defina o valor default da coluna Total como '0'
alter table pedido alter column total set default 0;

-- produto
create table produto (
    produtoid serial not null,
    nome varchar(100),
    descricao text,
    preco numeric(10,2),
    estoque integer,
    primary key (produtoid)
);
-- produto_pedido
create table produto_pedido (
    pedidoid integer not null,
    produtoid integer not null,
    quantidade integer,
    primary key (pedidoid, produtoid)
);
-- produto_categoria
create table produto_categoria (
    produtoid integer not null,
    categoriaid integer not null,
    primary key (produtoid, categoriaid)
);

-- Adicionando as restrições (FKs e DELETEs)

-- FKs
-- cliente_endereco em endereco
alter table endereco add constraint fk_cliente_endereco foreign key (clienteid) references cliente(clienteid)
-- c.2. ON DELETE | Ao excluir um cliente, os endereços relacionados também serão excluídos em endereço
on delete cascade;

-- cliente_pedido em pedido
alter table pedido add constraint fk_cliente_pedido foreign key (clienteid) references cliente(clienteid);

-- pedidoid_produto_pedido em produto_pedido
alter table produto_pedido add constraint fk_pedidoid_produto_pedido foreign key (pedidoid) references pedido(pedidoid);

-- produtoid_produto_pedido em produto_pedido
alter table produto_pedido add constraint fk_produtoid_produto_pedido foreign key (produtoid) references produto(produtoid);

-- produtoid_produto_categoria em produto_categoria
alter table produto_categoria add constraint fk_produtoid_produto_categoria foreign key (produtoid) references produto(produtoid);

-- categoriaid_produto_categoria em produto_categoria
alter table produto_categoria add constraint fk_categoriaid_produto_categoria foreign key (categoriaid) references categoria(categoriaid);

-- categoriapaiid_categoria em categoria | Auto-relacionamento
alter table categoria add constraint fk_categoriapaiid_categoria foreign key (categoriapaiid) references categoria(categoriaid);

