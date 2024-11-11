-- A1.1 Defina uma tabela temporária t_funcionario com os seguintes atributos: pnome varchar(255), cpf varchar(11), sexo character(2), salario numeric, cpf_supervisor varchar(11), dnr integer

create temp table t_funcionario (
    pnome varchar(255),
    cpf varchar(11),
    sexo character(2),
    salario numeric,
    cpf_supervisor varchar(11),
    dnr integer
)

-- A1.2. Crie uma function que apague todos os registros da tabela t_funcionario e, em seguida copie os registros da tabela funcionário para t_funcionário.
-- Nome da function: copiafuncionario

create or replace function copiafuncionario(tabela_dest text, tabela_orig text) returns text as 
$$
begin 
    -- 1. Apagar todos os registro em tabela_dest
    execute format('delete from %I', tabela_dest);
    raise notice 'Dados apagados com sucesso!';
    
    -- 2. Copiar todos os registro de tabela_orig em tabela_dest
    execute format('
		insert into %I 
		select 
			pnome,
			cpf,
			sexo,
			salario,
			cpf_supervisor,
			dnr
		from %I', tabela_dest, tabela_orig);
    raise notice 'Dados copiados com sucesso!';
    
	-- 3. Retornar mensagem de sucesso ou fracasso
	return 'Registros copiados com sucesso!';
exception
    when others then
        return 'Deu algum erro em algum lugar: ' || SQLERRM; 
end;
$$ language plpgsql;

-- A1.3. Faça uma chamada a função criada

select copiafuncionario('t_funcionario', 'funcionario');

-- Referência: https://www.postgresql.org/docs/17/plpgsql-statements.html#PLPGSQL-STATEMENTS-EXECUTING-DYN