-- 7. Listar todos os países cujo PIB per capita foi maior que US$10.000 em 2005.
select p.nome
from pais p
join pib pb on p.Sigla = pb.Sigla
where pb.ano = 2005 and pb.valor/p.pop > 10000;


-- 9. Listar os nomes dos países cuja população é maior do que a população da Nigéria.
select p.nome
from pais p
where p.pop > (select p.pop from pais p where p.nome = 'Nigéria')


-- 11. Listar o histórico dos valores do produto ‘Soja’ entre 1990 e 2005.
select h.valor
from histvalor h
where h.data between '1990-01-01' and '2005-12-31'


-- 13. Listar o percentual de crescimento do PIB dos países do ‘Mercosul’ entre 2000 e 2005.
select 
	p.nome as NomePais,
	((pb_2005.valor - pb_2000.valor)/pb_2000.valor) as PercentualCrescimento
from pais p
join pib pb_2000 on pb_2000.Sigla = p.Sigla and pb_2000.Ano = '2000'
join pib pb_2005 on pb_2005.Sigla = p.Sigla and pb_2005.Ano = '2005'
where p.Nome in ('Brasil', 'Venezuela', 'Argentina', 'Paraguai', 'Uruguai')


-- 15. Calcular a média do PIB per capita dos países da Europa.
select 
	p.nome as NomePais,
	SUM(pb.valor/p.pop) as MediaPerCapita 
from pais p
join pib pb on pb.Sigla = p.Sigla
where p.Continente = 'Europa'
group by NomePais