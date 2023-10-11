# Desafio Final | CompassUOL

## Sobre

> Este projeto tem como objetivo apropriar os conhecimentos objetidos ao longo de 5 meses.

![Static Badge](https://img.shields.io/badge/Tema-Filmes_e_S%C3%A9ries-e0913e)
![Static Badge](https://img.shields.io/badge/Categoria-A%C3%A7%C3%A3o_e_Aventura-ffd966)

## Arquitetura do Projeto

![arq](arq-projeto.png)

## Coleta de dados | Raw

A extração de dados será feita através de uma função periódica utilizando o [AWS Lambda]() a partir de qualquer fonte disponível na internet como o Twitter ou o The Movie DataBase (TMDB).

A coleta poderá ser feita por:

- Nome do filme
- Gênero
- Nome de Atores/Atrizes
- Nome de Personagens
- Etc..

## Armazenamento dos dados | Raw S3

Após ter coletado os dados, seu armazenamento será feito em um bucket do [Amazon S3](), contendo os dados brutos dos filmes e séries selecionados. 

### ETL | Python & Docker

- [Configuração Docker]()