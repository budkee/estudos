drop table if exists aluno cascade;
CREATE TABLE aluno (
  id INTEGER PRIMARY KEY,
  nome VARCHAR(255),
  nota NUMERIC
);

INSERT INTO aluno(id, nome, nota)
VALUES (1, 'Terry B. Padilla',7.3),
       (2, 'William S. Ray',0.6),
       (3, 'Barbara A. Gongora', 7.0),
       (4, 'Julie B. Manzer', 6.7),
       (5, 'Teresa J. Axtell', 4.6),
       (6, 'Ben M. Dantzler', 9.6);
