-- ET4.1 - Crie um trigger, que valide as alteração na instância de trabalha_em considerando a seguinte restrição:
			
		-- Um funcionário não pode ter carga horária de trabalho superior a 40h
	-- Regras:
		-- Nome do trigger: valida40horas
		-- Nome da function: valida40horas
		-- Utilize RAISE NOTICE / EXCEPTION para incluir mensagens na sua function  

-- Definição do trigger
create or replace trigger valida40horas
before insert or update of fcpf, horas on trabalha_em
for each row
execute function valida40horas()

-- Definição da function
create or replace function valida40horas() returns trigger as
$$ 
declare 
carga_horaria integer;
begin 

raise notice 'Validando a carga horária de trabalho...';
carga_horaria := (
	select sum(horas)
	from trabalha_em
	where fcpf=new.fcpf
);

if carga_horaria is null then
	carga_horaria := 0;
end if;

if TG_OG = 'INSERT' then 
	carga_horaria := carga_horaria + new.horas;
elseif TG_OG = 'UPDATE' then 
	carga_horaria := carga_horaria + new.horas - old.horas;
end if;

if carga_horaria > 40 then
	raise exception 'Carga horária maior do que o permitido.';
else
	raise notice 'Carga horária ok';
end if;

return new; -- Inserção
-- return null; -- Sem inserção
end;
$$ language plpgsql;	

-- 4.2 Crie um comando SQL para remover a function e o trigger

drop trigger valida40horas on trabalha_em;
drop function valida40horas;

-- 4.3 Crie um comando SQL para testar todas as ações de seu trigger

select * from trabalha_em;
-- Teste > 40 | Esperado 'Carga horária maior do que o permitido.'
insert into trabalha_em (fcpf, pnr, horas) values (12345678, 3, 41);
-- Teste <= 40 | Esperado 'Carga horária ok'
insert into trabalha_em (fcpf, pnr, horas) values (12345678, 3, 40);
update trabalha_em set horas = 41 where fcpf = '123456789' and pnr = 2;
update trabalha_em set horas = 40 where fcpf = '123456789' and pnr = 2;
