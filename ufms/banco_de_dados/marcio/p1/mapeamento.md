# Mapeamento relacional 

## Entidades e atributos

- cliente(_num_: int, nome: varchar(36), endereco: varchar(50), telefone: varchar(18), data_cadastro: date)

- colaborador(_num_: int, nome: varchar(36), endereco: varchar(36), telefone: varchar(18), data_cadastro: date, escolaridade: varchar(36), linguas: varchar(36), servicos_aptidoes: varchar(200), **num_setor**: int)

- servico(_id_: int, descricao: varchar(250), **colab_num**: int, data_inicio_serv: date, **num_equipe_trab**: int)

- equipe_trab(_num_: int, **num_serv**: int, num_colab: int)

- setor_atividade(_num_: int, nome: varchar(36))

## PKs

- PK(cliente) = num
- PK(colaborador) = num
- PK(servico) = id
- PK(equipe_trab) = num
- PK(setor_atividade) = num

## FKs

- FKnum_setor(colaborador) = PK(setor_atividade)
- FKnum_equipe(servico) = PK(equipe_trab)
- FKnum_colab(equipe_trab) = PK(colaborador)
- FKnum_serv(equipe_trab) = PK(servico)
