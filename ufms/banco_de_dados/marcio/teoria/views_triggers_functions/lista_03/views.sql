-- Questão 1

CREATE VIEW vendas.CLIENTES_MAIORES_VIEW AS
SELECT *
FROM vendas.ex_cliente
WHERE AGE(CURRENT_DATE, datanascimento) >= INTERVAL '18 anos';

-- Questão 2

CREATE VIEW vendas.ULTIMO_PEDIDO_VIEW AS
SELECT p.*
FROM vendas.ex_pedido p
JOIN (
    SELECT codcliente, MAX(codpedido) AS ultimo_pedido
    FROM vendas.ex_pedido
    GROUP BY codcliente
) sub
ON p.codcliente = sub.codcliente AND p.codpedido = sub.ultimo_pedido;

-- Questão 3

CREATE VIEW vendas.TABELA_PRODUTO_VIEW AS
SELECT pr.codproduto, pr.descricao, ip.valorunitario
FROM vendas.ex_produto pr
JOIN (
    SELECT codproduto, valorunitario, ROW_NUMBER() OVER (PARTITION BY codproduto ORDER BY codpedido DESC) AS rn
    FROM vendas.ex_itempedido
) ip
ON pr.codproduto = ip.codproduto
WHERE ip.rn = 1;

-- Questão 4
create view vendas.LISTA_NOTA_VIEW as
select nf, extract(month from datapedido) as mes
from vendas.ex_pedido
where extract(year from datapedido) = 2024
order by datapedido;

-- Questão 5
create view vendas.PRODUTO_FAVORITO_VIEW as
select cli.nome, prod.descricao, count(itped.quantidade) as qnt_pedido
from vendas.ex_itempedido as itped	
	left join vendas.ex_produto as prod on itped.codproduto=prod.codproduto
	left join vendas.ex_pedido as ped on itped.codpedido=ped.codpedido
	left join vendas.ex_cliente as cli on ped.codcliente=cli.codcliente
group by cli.nome, prod.descricao, itped.quantidade
order by cli.nome;

-- Questão 6
create view vendas.PRODUTOS_DEFASADOS_VIEW as
select prod.descricao, itped.codproduto
from vendas.ex_pedido as ped
	left join vendas.ex_itempedido as itped on ped.codpedido = itped.codpedido
	left join vendas.ex_produto as prod ON prod.codproduto = itped.codproduto
where extract(month from ped.datapedido) <= extract(month from interval '3 months');
