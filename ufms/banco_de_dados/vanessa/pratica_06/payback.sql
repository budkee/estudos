-- Uma empresa de investimentos deseja calcular o payback de seus clientes ao descobrir qual será o mês em que o acumulado das operações do empreendimento equivalem ou são superiores ao investimento inicial. Por exemplo, o cliente Lucas investiu R$ 1000 e apenas no terceiro mês obteve o seu payback, já que a soma de todas as suas operações foi superior ao seu investimento. Por outro lado, o cliente Daniel não conseguiu atingir seu payback já que seu investimento foi de R$ 500 e a soma de todas as suas operações foi R$ 230. Você precisa mostrar o nome do cliente, o investimento inicial, qual o mês do retorno do investimento e qual é o seu valor de retorno (valor acumulado - valor investimento inicial). Além disso, você deve mostrar o resultado ordenado do maior para o menor retorno.

-- Colunas esperadas: nome, investimento, mes_retorno, valor_retorno
-- Ordenação: valor_retorno descendente



with valor_acumulado as (
    select
        c.nome,
        c.investimento,
        o.mes,
        sum(o.lucro) over (partition by o.cliid order by o.mes) as lucro_acumulado
    from 
        operacao o 
        left join cliente c on o.cliid=c.id
), 
payback as (
    select 
        nome,
        investimento,
        mes,
        lucro_acumulado - investimento as valor_retorno,
        row_number() over (partition by nome order by mes) as num_row
    from
        valor_acumulado
    where
        lucro_acumulado >= investimento
)
select 
    nome, 
    investimento, 
    mes as mes_retorno, 
    valor_retorno 
from 
    payback
order by valor_retorno desc

-- Resposta Vanessa
select 
 nome, 
 investimento,
 min(mes) mes_retorno, 
 min(soma-investimento) valor_retorno 
 from cliente c join 
    (select cliid, mes, lucro, 
    sum(lucro) over (partition by cliid order by mes) soma 
    from operacao
    group by cliid, mes, lucro
    order by 1, 2)tb on c.id=tb.cliid
where soma >= investimento 
group by nome, investimento
order by 4 desc;