# Sistema de Apoio a Amigo Secreto (SAAS) | Diferenças na Modelagem Relacional

![saas](../img/amigo_secreto.jpg)

## Entidades e atributos | Kaê

**Sorteio**(**id_sorteio**, data_hora, resultado)
**Resultado**(**id_participante, id_amigo_secreto**)
**Patrocinador**(**id_patrocinador**, aviso_geral)
**Mensagem**(**id_patrocinador**, data_hora_envio, conteudo_mensagem, remetente, destinatario)
**Participante**(**id_participante**, codinome, nome, ramal, sugestao_presente)
**AvaliacaoSugestao**(**id_avaliacao**, id_participante_avaliador, avaliacao_sugestao)

## Entidades e atributos | Marcio

**Participante**(_codinome_, eh_patrocin)
**Mensagem**(_ID_, eh_aviso, msg)
**Sugestao** <entidade_fraca>(_descricao_)
**Presente** <entidade_fraca>(_descricao_)

## Relacionamentos | Kaê

**Participa**: Participante (1,1) e Sorteio (4, 60)
**Organiza**: Sorteio (1,n) e Patrocinador (1,1)
**Envia**: Participante (1,n) e Mensagem (2,n)
**Realiza**: Participante (0,n) e AvaliacaoSugestao (1,n)

## Relacionamentos | Marcio

**Envia**: Participante (0,n) e Mensagem (1,1)
**Recebe**: Participante (0,n) e Mensagem (1,1)
**Faz**: Participante (1,n) e Sugestão (1,1)
**Cadastra**: Presente (1,1) e Participante (0,n)
**Sortear**: Participante (1,n)

