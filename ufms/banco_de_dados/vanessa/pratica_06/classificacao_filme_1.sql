-- Realize uma consulta considerando as tabelas a seguir para listar os filmes que possuem todas as avaliações com classificacao igual a maior classificação que esse filme obteve.

-- Colunas esperadas: titulo_filme, classificacao
-- Ordenação: titulo_filme de forma crescente

with maior_classificacao as (
    select 
        f.idt_filme,
        max(a.classificacao) as maior_classificacao
    from 
        filme f
        left join avaliacao a on f.idt_filme = a.idt_filme
    group by 
        f.idt_filme
),
avaliacoes_unicas as (
    select 
        f.idt_filme,
        f.titulo,
        a.classificacao
    from 
        filme f
        left join avaliacao a on f.idt_filme = a.idt_filme
),
filmes_validos as (
    select 
        au.idt_filme,
        au.titulo,
        mc.maior_classificacao
    from 
        avaliacoes_unicas au
        join maior_classificacao mc on au.idt_filme = mc.idt_filme
    group by 
        au.idt_filme, 
        au.titulo, 
        mc.maior_classificacao
    having 
        count(distinct au.classificacao) = 1
)
select 
    titulo as titulo_filme,
    maior_classificacao as classificacao
from 
    filmes_validos
order by 
    titulo_filme asc;
