--Lista de Exercícios VIEW / MATERIALIZED VIEW

-- 	1.	Criação de View Complexa:

--Crie uma view chamada view_detalhes_funcionarios que mostre o nome completo dos funcionários (concatenando pnome, minicial e unome), seu departamento, o salário, e a média de salários de todos os funcionários no mesmo departamento. 
-- Utilize uma Window Function para calcular a média salarial dentro de cada departamento e outra Window Function para classificar o salário dos funcionários em cada departamento, de forma que o salário mais alto tenha a classificação 1.
-- Colunas esperadas: cpf, nome_completo, departamento, salario_funcionario, media_salarial, rank_salario.
-- Orderne pelo departamento e pelo rank_salario de forma ascendente

create view view_detalhes_funcionarios as

with media_salario_dpt as (
	select 
		dnr as departamento,
		round(avg(salario) over (partition by dnr), 2) as media_salarial
	from funcionario
), classificacao_salario as (
	select distinct
		f.cpf,
		f.pnome || ' ' || f.minicial || ' ' || f.unome as nome_completo,
		f.salario as salario_funcionario,
		ms.departamento,
		ms.media_salarial,
		dense_rank() over (partition by f.dnr order by f.salario desc) as rank_salario
	from 
		funcionario f 
		left join media_salario_dpt ms on f.dnr = ms.departamento
)
select 
	cpf,
	nome_completo,
	departamento,
	salario_funcionario,
	media_salarial,
	rank_salario
from classificacao_salario
order by departamento, rank_salario


-- 2.	Criação de Materialized View:
--Agora, crie uma Materialized View chamada mat_view_detalhes_funcionarios com a mesma consulta da view anterior.


create materialized view mat_view_detalhes_funcionarios as

with media_salario_dpt as (
	select 
		dnr as departamento,
		round(avg(salario) over (partition by dnr), 2) as media_salarial
	from funcionario
), classificacao_salario as (
	select distinct
		f.cpf,
		f.pnome || ' ' || f.minicial || ' ' || f.unome as nome_completo,
		f.salario as salario_funcionario,
		ms.departamento,
		ms.media_salarial,
		dense_rank() over (partition by f.dnr order by f.salario desc) as rank_salario
	from 
		funcionario f 
		left join media_salario_dpt ms on f.dnr = ms.departamento
)
select 
	cpf,
	nome_completo,
	departamento,
	salario_funcionario,
	media_salarial,
	rank_salario
from classificacao_salario
order by departamento, rank_salario



-- 3.	Alteração na Tabela Base:
--Faça uma alteração na tabela funcionario para aumentar o salário do funcionário chamado “James” em 10%. Exemplo:

update funcionario set salario = salario + (salario * 0.10) where pnome = 'James'


-- 4.	Verificação de Atualização:
-- Verifique se a materialized view possui os mesmos valores da view para o James

select * from mat_view_detalhes_funcionarios

-- 5.	Atualização da Materialized View:
-- Agora, faça o refresh da materialized view para que os dados reflitam as mudanças na tabela base:

refresh materialized view mat_view_detalhes_funcionarios;

--6. Verifique novamente os dados na materialized view e compare os resultados.

select * from mat_view_detalhes_funcionarios;