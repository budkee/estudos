-- M1. Liste os filmes que possuem classificação 3 ou 5. Considere apenas os títulos que possuem a letra 'o' como se segundo caractere e que possuem 1995 como parte do título. Colunas Esperadas (renomeamento se necessário): 
-- titulo_filme
-- Ordenação: titulo ascendente

select distinct f.titulo as titulo_filme
from filme f left join avaliacao a on f.idt_filme = a.idt_filme
where a.classificacao in (3, 5) and f.titulo like '_o%' and f.titulo like '%1995%'
order by titulo_filme

-- M2. Liste a segunda maior classificação de cada filme. Colunas Esperadas (renomeamento se necessário): idt_filme, segunda_maior_classificacao
-- Ordenação: idt_filme e segunda_maior_classificacao de forma crescente.

select f.idt_filme, max(a.classificacao) as segunda_maior_classificacao
from filme f left join avaliacao a on f.idt_filme=a.idt_filme
where a.classificacao in (4, 3) -- Considerando que as avaliações vão de 1 a 5
group by f.idt_filme
order by f.idt_filme, segunda_maior_classificacao


-- M3. Liste os filmes que possuem a menor quantidade de classificacoes. 
-- Colunas Esperadas (renomeamento se necessário): titulo_filme, qtd_classificacao
-- Ordenação: titulo_filme de forma decrescente

-- Classificacoes ordenados por titulo
select f.titulo as titulo_filme, a.classificacao
from avaliacao a left join filme f on f.idt_filme = a.idt_filme
order by f.titulo

-- Resposta
select f.titulo as titulo_filme, count(a.classificacao) as qtd_classificacao
from avaliacao a left join filme f on f.idt_filme = a.idt_filme
group by f.titulo
having count(a.classificacao) = (
    select min(qtd_classificacao)
    from (
        select count(a.classificacao) as qtd_classificacao
        from avaliacao a left join filme f on f.idt_filme = a.idt_filme
        group by f.titulo
    ) as subquery
)
order by f.titulo


-- M4. Liste todas as ocupações e a quantidade de usuários de cada uma delas. Considere apenas as ocupações que possuem a letra 'a' como se segundo caractere e a letra 'r' como último caractere.
-- Colunas Esperadas (renomeamento se necessário): nome_ocupacao, qtd_usuario
-- Ordenação: qtd_usuario em ordem decrescente

select o.nome as nome_ocupacao, count(u.idt_usuario) as qtd_usuario
from ocupacao o left join usuario u on o.idt_ocupacao = u.idt_ocupacao
where o.nome like '_a%' and o.nome like '_r'
order by qtd_usuario desc


-- M5. Liste os filmes que possuem a maior quantidade de classificacoes

-- Colunas Esperadas (renomeamento se necessário): titulo_filme, qtd_classificacao
-- Ordenação: titulo_filme de forma ascendente

select f.titulo as titulo_filme, count(a.classificacao) as qtd_classificacao
from avaliacao a left join filme f on f.idt_filme = a.idt_filme
group by f.titulo
having count(a.classificacao) = (
    select max(qtd_classificacao)
    from (
        select count(a.classificacao) as qtd_classificacao
        from avaliacao a left join filme f on f.idt_filme = a.idt_filme
        group by f.titulo
    ) as subquery
)
order by f.titulo

-- M6. Liste todos os filmes e categorize-os com base na classificação média.

-- 'Alta': Média de classificação superior ou igual a 4.
-- 'Média': Média de classificação igual a 3.
-- 'Baixa': Média de classificação inferior a 3.
-- Considere:

-- Colunas Esperadas (renomeamento se necessário): titulo_filme, categoria_avaliacao
-- Ordenação: titulo_filme em ordem ascendente.

select 
    f.titulo as titulo_filme, 
    case 
        when avg(a.classificacao) >= 4 then 'Alta'
        when avg(a.classificacao) = 3 then 'Média'
        when avg(a.classificacao) < 3 or avg(a.classificacao) = null then 'Baixa'
    end as categoria_avaliacao
from filme f left join avaliacao a on a.idt_filme = f.idt_filme
group by titulo_filme
order by titulo_filme