-- U1.1 Ana se encontra em uma emboscada porque fez um update sem where e acabou zerando todos os valores da coluna preco. Para sua sorte, o preco pode ser calculado novamente sabendo o tipo do produto.

-- Se o tipo do produto é igual A, o preco será 22.0
-- Se o tipo do produto é igual B, o preco será 75.0
-- Se o tipo do produto é igual C, o preco será 53.5

-- O seu trabalho é criar um function que corrige preco de todos os produtos (utilize apenas um comando update). 
-- Nome da function: corrigeUpdateSemWhere
create or replace function corrigeUpdateSemWhere() returns text as
$$
begin
	
	update produto 
	set preco = case
		when tipo = 'A' then 22.0
		when tipo = 'B' then 75.0
		when tipo = 'C' then 53.5
		else preco
	end;
	
	return 'Preços atualizados com sucesso!';
end;
$$ language plpgsql;


-- U1.2 Crie um comando SQL para fazer uma chamada à function definida

select corrigeUpdateSemWhere();

-- U1.3 Crie um comando SQL para remover a function definida

drop function corrigeUpdateSemWhere();