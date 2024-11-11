-- 1. Crie um trigger chamado produtolog que chame uma function com o mesmo nome.

-- Esse trigger deve ser disparado sempre que for alterado o preço do produto. Nesse caso, uma tupla é inserida na tabela produto_log
-- Dica: Utilize CURRENT_DATE para inserir a data atual; 
-- Considere na tabela produto_log os tipos U (Update) e D (delete)

-- Definição da function
create or replace function produtolog() returns trigger as 
$$

begin
  raise notice 'Alteração encontrada. Ativando a função produtolog...';
  
  if TG_OP = 'UPDATE' then
    if old.preco is distinct from new.preco then
      raise notice 'Nova atualização encontrada. Inserindo no log do produto...';
      insert into produto_log (
        id_produto, 
        preco_antigo, 
        preco_novo, 
        data_alteracao, 
        tipo
      ) values (
        old.id,
        old.preco,
        new.preco,
        current_date,
        'U'
      );
    end if;

  elseif TG_OP = 'DELETE' then
    raise notice 'Nova deleção encontrada. Inserindo no log do produto...';
    insert into produto_log (
      id_produto, 
      preco_antigo, 
      preco_novo, 
      data_alteracao, 
      tipo
    ) values (
      old.id,
      old.preco,
      null,
      current_date,
      'D'
    );
  end if;
  return null;
end;
$$ language plpgsql;

-- Definição do trigger
create trigger produtolog
after update or delete on produto
for each row
execute function produtolog()

-- 2. Crie os comandos SQL necessários para testar todas as opções de ação do seu trigger

update produto
set preco = 9999.90
where nome = 'Blue Chair'

delete from produto
where id = 5

-- 3. Crie comandos SQL para apagar o trigger e a function

drop trigger produtolog on produto;
drop function produtolog;
