-- Realize uma consulta considerando as tabelas a seguir para listar a segunda maior classificação de cada filme.

-- Colunas esperadas: idt_filme, segunda_maior_classificacao
-- Ordenação: idt_filme e segunda_maior_classificacao de forma crescente.

with classificacoes as (
    select
        f.idt_filme,
        a.classificacao
    from
        filme f
        left join avaliacao a on f.idt_filme=a.idt_filme  
    group by 
        f.idt_filme,
        a.classificacao
),
rank_classificacao as (
    select 
        idt_filme,
        classificacao,
        dense_rank() over (partition by idt_filme order by classificacao desc) as rank
    from   
        classificacoes
)
select 
    idt_filme,
    -- titulo,
    classificacao as segunda_maior_classificacao
from
    rank_classificacao
where
    rank = 2
order by idt_filme, segunda_maior_classificacao



