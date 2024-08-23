-- Mostre os 5 candidatos mais votados(número de id).
SELECT
    voto,
    count(*) as total_votos
FROM
    `Eleitor`
GROUP BY
    voto
ORDER BY
    voto
LIMIT
    5;

-- Mostre os dados da Seção com menos Eleitores.
SELECT
    s.id,
    count(*) as numero_eleitores,
    s.nome,
    s.zona
FROM
    Eleitor e
    LEFT JOIN Seção s on e.numero_secao = s.id
GROUP BY
    s.id
ORDER BY
    numero_eleitores;

-- Mostre os Partidos Políticos com mais Candidatos.
SELECT
    p.nome,
    count(*) as numero_candidatos
FROM
    Candidato c
    LEFT JOIN Partido p on c.partido = p.id
GROUP BY
    p.nome
ORDER BY
    numero_candidatos DESC;

-- Mostre a quantidade de Candidatos por Cargo
SELECT
    cargo,
    count(*) as numero_candidatos
FROM
    Candidato
GROUP BY
    cargo
ORDER BY
    numero_candidatos DESC;

-- Liste o boletim de urna com nome do candidato, número do candidato e total de votos por seção.
SELECT
    s.id as seção,
    c.nome as nome_candidato,
    c.numero,
    count(*) total_votos
FROM
    Seção s,
    Eleitor e
    LEFT JOIN Candidato c on e.voto = c.numero
GROUP BY
    seção,
    nome_candidato,
    c.numero
ORDER BY
    seção,
    total_votos DESC;