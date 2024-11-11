-- B2.1 Crie uma função para inserir um novo funcionário na tabela t_funcionario. 
-- Essa função deve receber os atributos da tabela como parâmetro e, ao final do operação, escrever uma mensagem de sucesso.
-- Nome da function: insereFuncionario
create or replace function insereFuncionario(
    pnome varchar, 
    cpf varchar, 
    sexo character, 
    salario numeric, 
    cpf_supervisor varchar, 
    dnr integer
) returns text as 
$$
begin
    execute format('
        insert into t_funcionario (
            pnome, 
            cpf, 
            sexo, 
            salario, 
            cpf_supervisor, 
            dnr
        )
        values (
            %L, 
            %L, 
            %L, 
            %s, 
            %L, 
            %s
        );
    ', pnome, cpf, sexo, salario, cpf_supervisor, dnr
    );
    return 'Funcionário adicionado com sucesso!';
exception
    when others then
        return 'Deu erro em algum lugar: ' || SQLERRM;
end;
$$ language plpgsql;

-- B2.2. Faça uma chamada a função criada para inserir um novo registro

select insereFuncionario(
    'Kaê', 
    '09890989033', 
    'M', 
    44000, 
    '888665555', 
    5
);

-- B2.3. Apaga a função definida

drop function insereFuncionario;

-- Referência: https://www.postgresql.org/docs/17/plpgsql-statements.html#PLPGSQL-STATEMENTS-EXECUTING-DYN
