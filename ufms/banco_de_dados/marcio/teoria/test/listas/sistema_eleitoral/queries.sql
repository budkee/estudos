--  Mostre o Número dos 5 candidatos mais votados.
select
    c.num,
    c.nome,
    count(*) as num_votos
from
    voto v
    left join candidato c on v.num_candidato = c.num
group by
    num_candidato
order by
    num_votos desc
limit 5;

-- Mostre os dados da Seção com menos Eleitores.
select
    e.num_secao,
    count(*) as num_eleitores,
    s.localidade,
    s.num_zona
from
    eleitor e
    left join secao s on e.num_secao = s.num
group by
    num_secao
order by
    num_eleitores
limit
    1;

-- Mostre os Partidos Políticos com mais Candidatos.
select
    p.nome_partido,
    count(*) as num_candidatos
from
    partido p
    left join candidato c on p.num = c.num_partido
group by
    p.num
order by
    num_candidatos desc;

-- Mostre a quantidade de Candidatos por Cargo.
select
    cargo,
    count(*) as num_candidatos
from
    candidato
group by
    cargo
order by
    num_candidatos desc;

-- Liste o boletim de urna com nome do candidato, número do candidato e total de votos por seção.
select
    c.nome,
    c.num,
    count(c.num) as num_votos,
    e.num_secao
from
    candidato c
    left join voto v on c.num = v.num_candidato
    left join secao s on s.num = v.num_secao
group by
    e.num_secao,
    c.num
order by
    num_votos desc;