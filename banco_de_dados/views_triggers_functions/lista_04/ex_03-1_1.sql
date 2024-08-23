SELECT 
	vr.codigo,
	vr.nome,
	vr.ranking,
	v.data,
	extract(quarter from v.data) as trimestre,
	sum(v.valor) as total_vendas
FROM vendas.vendedor as vr
	left join vendas.venda as v on vr.codigo = v.codvendedor
where extract(year from data) = extract(year from date_trunc('year', current_date - interval '1 year'))
group by v.data, vr.codigo
ORDER BY v.data ASC 

	
-- Calculo total de vendas por vendedor do ano de 2010 por trimestre
SELECT 
	v.data,
	vr.codigo,
	vr.nome,
	vr.ranking,
	extract(year from v.data) as ano,
	extract(quarter from v.data) as trimestre,
	sum(v.valor) as total_vendas
FROM vendas.vendedor as vr
	left join vendas.venda as v on vr.codigo = v.codvendedor
where extract(year from data) = 2010
group by vr.codigo, trimestre, v.data
ORDER BY v.data, total_vendas ASC 


-- Calculo total de vendas por vendedor do ano de 2010
SELECT 
	vr.codigo,
	vr.nome,
	vr.ranking,
	v.data,
	sum(v.valor) as total_vendas
FROM vendas.vendedor as vr
	left join vendas.venda as v on vr.codigo = v.codvendedor
where extract(year from data) = 2010
group by v.data, vr.codigo
ORDER BY v.data ASC 

-- Vendedor + Vendas
SELECT *
FROM vendas.vendedor as vr
	left join vendas.venda as v on vr.codigo = v.codvendedor
where extract(year from data) = 2010
ORDER BY data ASC 