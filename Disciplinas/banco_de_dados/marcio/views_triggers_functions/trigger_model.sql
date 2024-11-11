-- Uma trigger é composto por 4 partes:
-- 1. Momento: antes(BEFORE) e depois(AFTER) do evento ocorrer.
-- 2. Evento: define qual será o DML que acionará o gatilho (INSERT, UPDATE, DELETE).
-- 3. Tipo: define quantas vezes a ação será executada. Neste caso temos dois: ROW(para cada) e STATEMENT(apenas uma).
-- 4. Ação: define o que severá ser executado.

-- SINTAXE MODELO
CREATE TRIGGER nome_gatilho
{BEFORE | AFTER} 
{evento [OR outro_evento]} ON tabela
[FOR [EACH] {ROW | STATEMENT}]
EXECUTE PROCEDURE nome_funcao(argumentos)

-- Exemplo de aplicação | Auditoria 

-- Criação da função fn_audit_emp()
CREATE OR REPLACE FUNCTION fn_audit_emp() RETURNS TRIGGER AS $$
BEGIN
INSERT INTO emp_log VALUES (now(), userid, new.salario);
RETURN NEW;
END;
$$ language 'plpgsql';

-- Trigger
CREATE TRIGGER tr_log_emp
BEFORE INSERT OR UPDATE ON empregado
FOR EACH ROW 
EXECUTE PROCEDURE fn_audit_emp()
