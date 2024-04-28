# Notown Records | Modelagem Relacional

![notown](../img/notown_records.jpg)

## Entidades e atributos | Kaê

**Álbum**: (**id_album**, formato, titulo, data_direitos_autorais, produtor)
**Música**: (**id_musica**, titulo, album, autor)
**Instrumento**: (**id_instrumento**, tom_musical, nome)
**Endereco**: (**num_telefone**)
**Músico**: (_cpf_, nome)

## Entidades e atributos | Marcio

**Álbum**: (_id_, formato, titulo, data)
**Música**: (_id_, titulo)
**Instrumento**: (__tom_, _nome__)
**Endereco**: (_telefone_, cep, logradouro)
**Músico**: (_cpf_, nome, telefone)

## Relacionamentos | Kaê

**Produz**: Músico (0,n) e Álbum (1,1)
**Compõe**: Músico (0,n), Álbum (1,n) ou Música (1,n)
**Interpreta**: Músico (1,n), Música (1,n)
**Toca**: Músico (1,n), Instrumento (1,1)
**eh_utilizado**: Instrumento (0,1) e Música (1,n)

## Relacionamentos | Marcio

**Produz**: Músico (0,n) e Álbum (1,1)
**Escreve**: Músico (0,n), Álbum (1,n) ou Música (1,n)
**Participa**: Músico (0,n) e Música (1,n)
**Interpreta**: Músico (1,n), Música (0,n) ou Instrumento (0,n)
**Possui**: Música (1,n) e Álbum (1,n)
**Contém**: Música (0,n) e Instrumento (0,n)
**Mora**: Endereço (1,n) e Músico (1,n)
