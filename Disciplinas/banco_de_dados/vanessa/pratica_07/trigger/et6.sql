-- ET6

-- 6.1 Crie um comando SQL para alterar a tabela funcionario adicionando a coluna idadefunc (integer) 
	alter table funcionario add column idadefunc integer;

-- 6.2 Crie uma função chamada calculaIdade() que receba como parâmetro o cpf do funcionário (varchar(11)) e retorne um inteiro com a sua idade. 
		-- Observações:
			-- Nome da function: calculaIdade
			-- Dica: para calcular a idade utilize a seguinte consulta: select extract(year from age(datanasc)) from funcionario where cpf=<parametro>;
	create or replace function calculaIdade(cpf_in varchar(11)) returns integer as
	$$ 
	declare
		idade integer;
	begin

		idade := (
			select extract(year from age(datanasc)) 
			from funcionario 
			where cpf=cpf_in
		);
		return idade;

	end;
	$$ language plpgsql;



-- 6.3 - Utilizando a function desenvolvida em 6.2, crie um trigger chamada  com as seguintes regras:
		-- Cada vez que for inserida/atualizado uma nova tupla ou o campo datanasc calcule a idade desse funcionário a partida da sua data de nascimento (datanasc) e 
		-- atualize o campo idadefunc deste funcionário com esse valor calculado. 
		-- Ao atualizar o campo exiba uma mensagem com o nome do funcionário, sua data de nascimento e a idade calculada
		
		-- Nome do trigger: atualizaidade
		-- Nome da function: atualizaidade
		-- Utilize RAISE NOTICE / EXCEPTION para incluir mensagens na sua function  

		-- Definição do trigger
		create or replace trigger atualizaidade
		before insert or update on funcionario
		for each row
		execute function atualizaidade()

		-- Definição da function
		create or replace function atualizaidade() returns trigger as 
		$$
		declare
			idade integer;
		begin
			if TG_OP = 'UPDATE' or TG_OP = 'INSERT' then
				raise notice 'Nova atualização em funcionario. Calculando sua idade...';
				-- Calcular a idade
				idade := (select extract(year from age(new.datanasc)));
				
				-- Inserir na tabela
				-- update funcionario set idadefunc = idade where cpf = new.cpf;
				new.idadefunc := idade;
				raise notice 'Tudo certo! Funcionário %, nascido em %, com % anos.', new.pnome, new.datanasc, idade;
			end if;
			
			return new;

		end;
		$$ language plpgsql;

-- 6.4 Crie um comando SQL para testar a função calculaidade
	
	select calculaIdade('987654321');

-- 6.5 Crie um comando SQL para apagar a função calculaidade

	drop function calculaIdade;

-- 6.6 Crie comandos SQL para testar todas as ações de seu trigger
	select * from funcionario;
	insert into funcionario(pnome, datanasc, cpf) values ('Kaê', '2000-10-16', '09889989009');
	update funcionario set datanasc = '1969-05-12' where cpf = '111112';

-- 6.7 Crie um comando SQL para remover a function e o trigger

	drop trigger atualizaidade on funcionario;
	drop function atualizaidade;