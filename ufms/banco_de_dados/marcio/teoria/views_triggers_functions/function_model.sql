-- Linguagens Procedurais
-- PL/pgSQ

-- Sintaxe
CREATE OR REPLACE FUNCTION  <NOME> ( [Lista_de_Parâmetros]) 
RETURNS AS $$
[ DECLARE  declaração_de _variáveis ]
BEGIN
comandos
END; 
$$LANGUAGE nome_LinguagemProcedural;

-- Exemplo
CREATE OR REPLACE FUNCTION fn_retorna() RETURNS integer 
AS $$
DECLARE
    inteiro integer := 10;
BEGIN
    
    return inteiro;
END;
$$LANGUAGE  'plpgsql'

-- Exemplo | Execução da função
select fn_retorna()

