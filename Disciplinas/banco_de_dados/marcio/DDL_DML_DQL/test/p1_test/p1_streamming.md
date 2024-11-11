# Mapeamento Relacional | Serviço de Streamming

## Entidade, atributos e relacionamentos

- usuario(_cpf_: varchar(14), nome: varchar(36), telefone: varchar(13), email: varchar(36), senha: varchar(8), **endereco_cobranca**: varchar(36), num_cc: int, **status_pagamento**: varchar(14))

- endereco(*cpf_cliente: varchar(14), cep: varchar(10)*, logradouro: varchar(50), **apelido**: varchar(36))

- mensalidade(*id_mes*: int, **cpf_cliente**: varchar(14), **cc_cliente**: int, **email_cliente**: varchar(36), **status**: varchar(14))

- ator(*id*: int, nome: varchar(36), data_nascimento: date, local_nascimento: varchar(20), **filmes**: varchar(36), **series**: varchar(36), **documentarios**: varchar(36))

- avaliacao(_id_: int, **id_video**: int, **id_usuario**: varchar(14), nota: int)

- catalogo(*id_filmes, id_series, id_documentario*: int)

- filmes(_id_: int, **titulo**: varchar(36), ano_prod: date, duracao_minutos: int, **id_ator**: int)

- series(_id_: int, **titulo**: varchar(36), ano_prod: date, duracao_minutos: int, **prox_ep**: int, **id_ator**: int)

- documentarios(_id_: int, **titulo**: varchar(36), ano_prod: date, duracao_minutos: int, nome_prod: varchar(20), **id_ator**: int)

## PKs

- PK(usuario) = cpf: varchar(14)
- PK(endereco) = cpf_cliente: varchar(14), cep: varchar(10)
- PK(mensalidade) = id_mes
- PK(ator) = id: int
- PK(avaliacao) = id: int
- PK(catalogo) = id_filmes, id_series, id_documentario: int
- PK(filmes) = id: int
- PK(series) = id: int
- PK(documentarios) = id: int

## FKs

- FKendereco_cobranca(usuario) = PK(endereco)
- FKstatus_usuario(usuario) = PK(mensalidade)

- FKcpf_cliente(endereco) = PK(usuario)

- FKcpf_cliente(mensalidade) = PK(usuario)
- FKcc_cliente(mensalidade) = PK(usuario)
- FKemail_cliente(mensalidade) = PK(usuario)

- FKator_filme(ator) = PK(filme)
- FKator_serie(ator) = PK(serie)
- FKator_documentario(ator) = PK(documentario)

- FKid_filme(catalogo) = PK(filme)
- FKid_serie(catalogo) = PK(serie)
- FKid_documentario(catalogo) = PK(documentario)

- FKprox_ep(serie) = PK(serie)

## Diagrama do serviço