-- ET3.1 - Crie um trigger, que valide as alteração na instância de funcionario considerando a seguinte restrição:
			-- Um funcionário não pode ser supervisor dele mesmo
		-- Regras:
			-- Nome do trigger: validafuncsupervisor
			-- Nome da function: validafuncsupervisor
			-- Utilize RAISE NOTICE / EXCEPTION para incluir mensagens na sua function  


	-- Definição do trigger
	create or replace trigger validafuncsupervisor
	before insert or update or delete of cpf, cpf_supervisor on funcionario 
	for each row
	execute function validafuncsupervisor()

	-- Definição da function
	create or replace function validafuncsupervisor() returns trigger as
	$$
		
	begin 
		if TG_OP = 'UPDATE' then
			if old.cpf_supervisor is distinct from new.cpf_supervisor then
				raise notice 'Nova atualização. Verificando se é a mesma pessoa...';
				if new.cpf_supervisor = old.cpf then
					raise exception 'Um funcionário não pode ser supervisor dele mesmo.';
				end if;
			end if;
		elseif TG_OP = 'INSERT' then
			raise notice 'Novo supervisor inserido. Verificando se é a mesma pessoa...';
			if new.cpf = new.cpf_supervisor then
				raise exception 'Um funcionário não pode ser supervisor dele mesmo.';
			end if;
		end if;

		return new;
	end;
	$$ language plpgsql;


-- 3.2 Crie um comando SQL para remover a function e o trigger

	drop trigger validafuncsupervisor on funcionario;
	drop function validafuncsupervisor;

-- 3.3 Crie um comando SQL para testar todas as ações de seu trigger

select * from funcionario;

update funcionario set cpf_supervisor = '123456789' where cpf = '123456789';
update funcionario set cpf_supervisor = '943775543' where cpf = '123456789';
insert into funcionario (cpf, cpf_supervisor) values (111112, 111112);
insert into funcionario (cpf, cpf_supervisor) values (111112, 123456789);