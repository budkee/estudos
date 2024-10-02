-- 1. Criar uma TRIGGER no banco de dados de vendedores que não permita que compras abaixo de R$ 10,00 sejam aceitas. Caso a situação ocorra, dispare uma exceção que invalide a inserção.

create or replace function verifica_valor() returns trigger as $$
begin
	if NEW.valor < 10
		then raise exception 'Compora não pode ser menor que R$10';
	end if;
	return NEW;
end;
$$ language 'plpgsql';

create trigger antes_inserir
before insert on vendas.venda
for each row
execute function verifica_valor();

-- Teste
insert into vendas.venda(data, codcliente, codvendedor, valor) values('2023-02-01', 1, 4, 9);
insert into vendas.venda(data, codcliente, codvendedor, valor) values('2023-02-01', 1, 4, 19);