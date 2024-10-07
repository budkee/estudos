-- 1. Criar uma sequence chamada id_seq que começa em 1 e incrementa de 1 em 1.

create sequence id_seq
as integer
increment 1
start 1

-- 2. Utilize a sequence criada na questão 1 para fazer o incremento automático no campo id da tabela cliente. Conside a relação CLIENTE (id:integer (PK), nome:string, email:string)

create table cliente (
	id integer default nextval('id_seq'),
	nome varchar(30),
	email varchar(50),
	primary key(id)
)

-- 3. Inserir pelo menos 3 tuplas com valores da sequence na coluna id:

insert into cliente (nome, email) 
values 
    ('Rolinda Tucano', 'rolinda@linda.com'), 
    ('Roger Petista', 'roger@real.br'), 
    ('Pablo Escobar', 'pablo.escobar@gmail.com')

-- 4. Verificar os registros inseridos na tabela cliente:

select * from cliente

-- 5. Considerar a tabela pedido abaixo e a sequence pedidoid_seq para inserir dados na tabela utilizando pedidoid_seq no comando de insert.

    CREATE TABLE pedido (
        id INTEGER PRIMARY KEY,
        cliente_id INTEGER,
        preco NUMERIC(10,2),
        data timestamp,
        FOREIGN KEY (cliente_id) REFERENCES cliente (id)
    );

    CREATE SEQUENCE pedidoid_seq;

    -- Certifique-se de que a tabela "cliente" já contenha registros com IDs correspondentes antes de inserir dados na tabela "pedido".

    -- Inserir dados na tabela pedido utilizando a sequence id_seq:

    insert into pedido (id, cliente_id, preco, data) 
    values 
        (nextval('pedidoid_seq'), 1, 223, now()), 
        (nextval('pedidoid_seq'), 2, 442, now()), 
        (nextval('pedidoid_seq'), 3, 55, now());

-- 6. Obter o próximo valor da sequence id_seq sem realmente inserir um registro na tabela:

select nextval('id_seq') as next_value;

-- 7. Alterar o valor atual da sequence id_seq para 30:

select setval('id_seq', 30) as valor_atual;

-- 8. Reinicie a sequence pedidoid_seq com o valor inicial 100.

select setval('pedidoid_seq', 100) as init_value;

-- 8. Reiniciar a sequence id_seq para o seu valor inicial:

alter sequence id_seq restart with 1;

-- 9. Definir um valor mínimo de 1 e um valor máximo de 1000 para a sequence id_seq:

alter sequence id_seq minvalue 1 maxvalue 1000;

-- 10. Criar a tabela pagamento com uma coluna idpagamento que gera valores automaticamente (utilize SERIAL).
-- Considere a relação pagamento (idpagamento(PK):integer, descricao:string, pedido_id:integer(FK))

create table pagamento (
    idpagamento serial primary key,
    descricao varchar(255),
    pedido_id integer,
    constraint fk_pedido foreign key (pedido_id) references pedido(id)
);

-- 11. Obter o valor atual da sequence gerada em pagamento.idpagamento sem avançá-la (Certifique-se de que a sequência foi criada corretamente):

select nextval(pg_get_serial_sequence('pagamento', 'idpagamento'));

-- 12. Inserir pelo menos 3 tuplas na tabela pagamento:

insert into pagamento (descricao, pedido_id)
values
    ('Banana com bolacha', 1),
    ('Paçoca amassada', 2),
    ('Comida abandonada', 3);

