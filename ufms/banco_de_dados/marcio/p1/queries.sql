-- Listar o nome dos 5 colaboradores que mais executaram serviços na empresa.
select c.nome, count(*) as num_servicos
from colaborador c
left join servico s on c.num=s.num_equipe_trab
group by c.nome
order by num_servicos 
limit 5;

-- Liste os colaboradores que executaram serviços de carpintaria nos últimos 30 dias.

select c.nome, s.descricao, s.data_inicio_serv
from colaborador c
left join servico s on c.num=s.num_equipe_trab
where s.descricao="carpintaria" and s.data_inicio_serv>='2024-03-30'
group by c.nome, s.data_inicio_serv;