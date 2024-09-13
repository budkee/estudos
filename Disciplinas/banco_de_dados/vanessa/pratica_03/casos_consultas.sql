--------------------- Casos de uso: Empresa -----------------
-- Retorne  o nome do funcionário e de seu supervisor. Liste todos os funcionários, mesmo aqueles que não possuem supervisor.

-- Colunas esperadas (renomeamento se necessário): nome_funcionario, nome_supervisor

select 
	func.pnome as nome_funcionario,
	sup.pnome as nome_supervisor
from funcionario func
	left join funcionario sup
	on func.cpf_supervisor = sup.cpf

-- Liste os nomes dos funcionários, as horas trabalhadas e o nome dos projetos que os funcionários trabalharam e são controlado pelo departamento número 5.

-- Colunas esperadas: pnome, unome, horas, projnome
-- Ordernação: pnome e projnome crescente

select f.pnome, f.unome, t.horas, p.projnome
from funcionario f
	left join trabalha_em t
		on f.cpf = t.fcpf
	left join projeto p
		on t.pnr = p.projnumero
where p.dnum = 5
order by f.pnome, p.projnome asc

-- Liste para cada funcionario seu cpf, nome e salario, bem como o cpf o nome e o salario de seu gerente direto. Considere apenas os funcionários que possuem salario menor ou igual ao salário de seu gerente.

-- Colunas esperadas (renomeamento se necessário): cpf_funcionario, nome_funcionario, salario_funcionario, cpf_gerente, nome_gerente, salario_gerente
-- Ordenação: salario_funcionario decrescente

select 
	f.cpf as cpf_funcionario, 
	f.pnome as nome_funcionario, 
	f.salario as salario_funcionario,
	d.cpf_gerente as cpf_gerente,
	g.pnome as nome_gerente,
	g.salario as salario_gerente
from funcionario f
	left join departamento d
		on f.dnr = d.dnumero
	left join funcionario g
		on d.cpf_gerente = g.cpf
where f.salario <= g.salario
order by f.salario desc

-- Retorne o nome e o salario dos funcionários que possuem salário superior à média salarial de seu departamento.

-- Colunas esperadas (renomeamento se necessário): nome_funcionario, salario
-- Ordenação: dnr crescente

select 
	pnome as nome_funcionario,
	salario as salario
from funcionario f1
where salario > (
	select 
		round(avg(salario), 2) as media
	from funcionario f2
	where f1.dnr = f2.dnr
	group by f2.dnr
)
order by f1.dnr

-- Média de salário dos funcionários por departamento
select 
    dnr, 
    round(avg(salario), 2) as media
from funcionario
group by dnr
order by media

-- Recupere os funcionários que não possuem dependentes

-- Colunas esperadas: todos os atributos de funcionário
-- Ordenação: primeiro atributo(cpf) desc


select * 
from funcionario f
where not exists (
	select *
	from dependente d
	where f.cpf = d.fcpf
)
order by pnome desc







--------------------- Casos de uso: Produtos e Categoria -----------------
-- 1. Nossa empresa está em busca de um novo contrato para o fornecimento de novos produtos e para isso é necessário entender alguns dados dos nossos produtos. 

-- Seu trabalho é exibir o nome de todos os produtos, nome da categoria, nome dos fornecedores e o preço, para os produtos cujo preço seja maior que 500 e sua categoria seja 'Super Luxury' ou seu fornecedor seja 'Mike electro'. Considere todos os produtos, mesmo aqueles que não possuem fornecedor ou categoria.

-- Colunas esperadas: nome_poduto, nome_categoria, nome_fornecedor, preco

-- Ordenação: preco (ascendente)

select 
	p.nome as nome_poduto, 
	c.nome as nome_categoria, 
	f.nome as nome_fornecedor, 
	p.preco
from produto p
	left join categoria c
		on p.id_categoria = c.id
	left join fornecedor f
		on p.id_fornecedor = f.id
where p.preco > 500 and (c.nome = 'Super Luxury' or f.nome = 'Mike electro')
order by p.preco asc

-- 2. Nossa empresa quer investir melhor em seus fornecedores, para isso precisamos entender qual é a quantidade de produtos vendidos por fornecedor e a quantidade de produtos que cada fornecedor disponibiliza em seu estoque.

-- Crie um consulta que retorne: nome_fornecedor, qtd_produtos, qtd_estoque. É importante mostrar inclusive os fornecedores que não possuem produtos e estoque (quantidade igual a zero).

-- Ordene pelo nome do fornecedor de forma descendente.
-- Dica: você pode utilizar a função COALESCE(atributo, 0) para substituir algum valor null por zero.

select 
	f.nome as nome_fornecedor, 
	count(p.id) as qtd_produtos, 
	coalesce(sum(p.qtd_estoque), 0) as qtd_estoque
from fornecedor f 
	left join produto p
		on f.id = p.id_fornecedor
group by f.nome
order by f.nome desc, qtd_estoque


--------------------- Casos de uso: Clientes e Pedidos -----------------
-- 1. Nossos clientes estão comprando muitos produtos, mas não sabemos exatamente quais. Por isso, seu trabalho é gerar um relatório que retorne o nome do cliente o item que ele comprou e o preço desse item. É importante retornar também os clientes que nunca realizaram pedidos.

-- Colunas esperadas: nome, item, preço
-- Ordenação: nome

select 
	c.nome,
	p.item,
	p.preco
from cliente c
	left join pedido p
		on c.id = p.cliente_id
order by c.nome

--------------------- Casos de uso: Entrega de pacotes -----------------
-- 1. Você trabalha em uma transportadora e precisa mostrar com urgência o ano e o nome de todos os clientes que:

-- enviaram e receberam pacotes que são azuis ou do ano de 2015. 
-- Além disso o endereço do seu remetente ou destinatário não seja de Taiwan. 
-- Colunas esperadas: ano, nome_envio, nome_recibo

-- Ordenação: ano e nome_envio descendente

select 
	envp.ano,
	u_env.nome as nome_envio,
	u_rec.nome as nome_recibo
from usuario u_env
	left join pacote envp
		on u_env.id = envp.id_usuario_envio
	left join usuario u_rec
		on u_rec.id = envp.id_usuario_recibo
where (envp.cor = 'azul' or envp.ano = 2015) and (u_env.endereco != 'Taiwan' and u_rec.endereco != 'Taiwan')
order by envp.ano desc, u_env.nome desc

--------------------- Casos de uso: Locação -----------------
-- 1. A locadora pretende fazer uma promoção para os clientes que ainda não fizeram nenhuma locação.

-- Seu trabalho é nos entregar o ID e o nome dos clientes que não realizaram nenhuma locação.

select 
	c.id,
	c.nome,
	l.id
from cliente c
	left join locacao l
		on c.id = l.id_cliente
where l.id is null

-- 2. Liste o os filmes que são dos gêneros 'Action', 'Horror' e 'Wars'.

-- Colunas Esperadas (renomeamento se necessário): titulo_filme, nome_genero
-- Ordenação: titulo_filme em ordem decrescente

select 
	f.titulo as titulo_filme, 
	g.nome as nome_genero
from filme f
	left join filme_genero fg
		on f.idt_filme = fg.idt_filme
	left join genero g
		on fg.idt_genero = g.idt_genero
where g.nome in ('Action', 'Horror', 'Wars')
order by f.titulo desc

-- 3. Liste os filmes que possuem classificação 3 ou 5. Considere apenas os títulos que possuem a letra 'o' como se segundo caractere e que possuem 1995 como parte do título.

-- Colunas Esperadas (renomeamento se necessário): titulo_filme
-- Ordenação: titulo_filme ascendente
-- UTILIZE SUBCONSULTAS IN/NOT IN 

select 
	f.titulo
from filme f
	left join avaliacao a
		on a.idt_filme = f.idt_filme
where a.classificacao in (3, 5) and f.titulo like '_o%' and f.titulo like '%1995%'
group by f.titulo
order by f.titulo asc