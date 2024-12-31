-- Recupere os três funcionários mais bem pagos em cada departamento.

-- Colunas esperadas (renomeamento se necessário): nome_departamento, nome_funcionario, salario_funcionario
-- Ordenação: nome_departamento decrescente

with salario_rankeado as (
    select 
        d.dnome as nome_departamento,
        f.pnome as nome_funcionario,
        f.salario as salario_funcionario,
        row_number() over (partition by f.dnr order by f.salario desc) as rank_salario
    from 
        funcionario f
    join 
        departamento d on f.dnr = d.dnumero
)
select 
    nome_departamento,
    nome_funcionario,
    salario_funcionario
from 
    salario_rankeado
where 
    rank_salario <= 3
order by 
    nome_departamento desc, salario_funcionario desc;
