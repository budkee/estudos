-- Query: Total de vendas do mês passado por vendedor
select 
	cod_vendedor,
	situacao_vendedor,
	sum(valor_venda) as total_vendas
from (
	select
		vdr.codigo as cod_vendedor,
		vdr.nome as nome_vendedor,
		vdr.situacao as situacao_vendedor,
		vds.codigo as cod_venda,
		vds.data as data_venda,
		COALESCE(SUM(vds.valor), 0) as valor_venda
	from vendas.vendedor as vdr
		left join vendas.venda as vds on vdr.codigo = vds.codvendedor
) as vendas_vendedor_ult_mes
where vendas_vendedor_ult_mes.data_venda >= date_trunc('month', current_date) - interval '1 month' and vendas_vendedor_ult_mes.data_venda < date_trunc('month', current_date)
group by cod_vendedor, situacao_vendedor
order by cod_vendedor, total_vendas

-- Query: Total de vendas por vendedor
select 
	cod_vendedor,
	sum(valor_venda) as total_vendas
from (
	select
		vdr.codigo as cod_vendedor,
		vdr.nome as nome_vendedor,
		vdr.situacao as situacao_vendedor,
		vds.codigo as cod_venda,
		vds.data as data_venda,
		COALESCE(SUM(vds.valor), 0) as valor_venda
	from vendas.vendedor as vdr
		left join vendas.venda as vds on vdr.codigo = vds.codvendedor
	-- where vds.data >= date_trunc('month', current_date) - interval '1 month' and vds.data < date_trunc('month', current_date)
) as vendas_vendedor_ult_mes
group by cod_vendedor
order by cod_vendedor, total_vendas



-- Query: Vendas por vendedor do mês passado 
select 
	vdr.codigo as cod_vendedor,
	vdr.nome as nome_vendedor,
	vdr.situacao as situacao_vendedor,
	vds.codigo as cod_venda,
	vds.data as data_venda,
	COALESCE(SUM(vds.valor), 0) as valor_venda
from vendas.vendedor as vdr
	left join vendas.venda as vds on vdr.codigo = vds.codvendedor
where vds.data >= date_trunc('month', current_date) - interval '1 month' and vds.data < date_trunc('month', current_date)
order by cod_vendedor, data_venda, valor_venda


-- Query: Vendas por vendedor
select 
	vdr.codigo as cod_vendedor,
	vdr.nome as nome_vendedor,
	vdr.situacao as situacao_vendedor,
	vds.codigo as cod_venda,
	vds.data as data_venda,
	COALESCE(SUM(vds.valor), 0) as valor_venda
from vendas.vendedor as vdr
	left join vendas.venda as vds on vdr.codigo = vds.codvendedor
order by cod_vendedor, data_venda, valor_venda