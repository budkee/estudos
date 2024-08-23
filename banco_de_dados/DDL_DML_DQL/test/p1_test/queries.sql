-- Liste o titulo de todos os FILMES com duração acima de 60 minutos que possuem a participação do ator Arnold Schwarzenegger.
select f.titulo
from filmes f
left join ator a on f.id_ator=a.id
where f.duracao_minuntos>=60 and a.nome="Arnold Schwarzenegger"
-- Liste os títulos dos documentários avaliados pela usuária ’Gabriela’, onde ela realizou uma avaliação com nota acima de 5 (em uma escala de 0 a 10).
select d.titulo
from documentarios d 
left join avaliacao av on d.id=av.id_video
left join usuario u on av.id_usuario=u.id 
where u.nome="Gabriela" and av.nota>5; 
