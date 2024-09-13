-- 1. Criar uma TRIGGER no banco de dados de vendedores que não permita que compras abaixo de R$ 10,00 sejam aceitas. Caso a situação ocorra, dispare uma exceção que invalide a inserção.

CREATE OR REPLACE FUNCTION verifica_valor() RETURNS TRIGGER AS 
$$
BEGIN
	IF NEW.valor < 10 
		THEN RAISE EXCEPTION 'Compra não pode ser menor que R$10';
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER antes_inserir
BEFORE INSERT ON vendas.venda
FOR EACH ROW 
EXECUTE PROCEDURE verifica_valor();

-- 2. Crie uma FUNÇÃO que mude a situacao dos vendedores para inativo quando a venda total do mês passado destes vendedores for inferior a R$ 1.000,00.
-- Vendas do mês passado por vendedor
-- create view vendas.VENDAS_VENDEDOR_ULT_MES as
select 
	v.codvendedor, 
	sum(v.valor) as total_vendas,
	vr.situacao
from vendas.venda as v
	left join vendas.vendedor as vr on v.codvendedor = vr.codigo
where extract(month from data) < extract(month from CURRENT_DATE)
group by v.codvendedor, vr.situacao
order by v.codvendedor asc;


CREATE OR REPLACE FUNCTION altera_situacao() RETURNS void AS
$$
DECLARE
	rec RECORD;
BEGIN
	FOR rec IN
		select 
			v.codvendedor, 
			sum(v.valor) as total_vendas,
			vr.situacao
		from vendas.venda as v
			left join vendas.vendedor as vr on v.codvendedor = vr.codigo
		where extract(month from data) < extract(month from CURRENT_DATE)
		group by v.codvendedor, vr.situacao
		order by v.codvendedor asc
	LOOP
		IF rec.situacao = 'A' THEN
			IF rec.total_vendas < 1000 THEN
				UPDATE vendas.vendedor 
				SET situacao = 'I'
				WHERE codigo = rec.codvendedor;
			END IF;
		END IF;
	END LOOP;
END;
$$ LANGUAGE 'plpgsql';

-- 3. FUNCTION
-- Crie um campo texto de 16 caracteres na tabela de vendedores chamado ranking. 
ALTER TABLE vendas.vendedor ADD COLUMN ranking VARCHAR(16);
-- Logo após, crie uma FUNÇÃO que calcule o total de vendas de cada vendedor por trimestre, considerando somente as vendas de Janeiro a Dezembro do ano passado. 
CREATE OR REPLACE FUNCTION ranking_trimestre() RETURNS void AS
$$
DECLARE
	rec RECORD;
BEGIN
	-- Calculo total de vendas de cada vendedor por trimestre (JAN a DEZ)
	FOR rec IN
		SELECT 
			vr.codigo,
			vr.nome,
			vr.ranking,
			v.data,
			extract(year from v.data) as ano,
			extract(quarter from v.data) as trimestre,
			sum(v.valor) as total_vendas
		FROM vendas.vendedor as vr
			left join vendas.venda as v on vr.codigo = v.codvendedor
		where extract(year from data) = 2010
		group by v.data, vr.codigo
		ORDER BY v.data ASC 
	LOOP
		IF rec.situacao = 'A' THEN
			IF rec.total_vendas < 1000 THEN
				UPDATE vendas.vendedor 
				SET situacao = 'I'
				WHERE codigo = rec.codvendedor;
			END IF;
		END IF;
	END LOOP;
END;
$$ LANGUAGE 'pspgsql';
-- Conte quantos trimestres o vendedor vendeu acima de R$ 50.000,00. 
---- Se foi 0 trimestres, atualize o ranking dele para “Nivel 1”, 
---- se foi 1 trimestre: “Nivel 2”, 
---- 2 trimestres: “Nivel 3”, 
---- 3 trimestres: “Nível 4” 
---- e 4 trimestres: “Nível 5”.




-- 4. Crie uma TRIGGER que não permita a duplicação do número da carteira de trabalho dos vendedores (ctps). Caso ocorra a duplicação, dispare uma exceção informando o erro. Rejeite a operação.

CREATE OR REPLACE FUNCTION vendas.dont_duplica() RETURNS TRIGGER AS
$$ 
BEGIN 
	IF NEW.ctps exists
		THEN RAISE EXCEPTION 'Operação inválida, número já existente!';
	END IF;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER verifica_duplicado
BEFORE INSERT OR UPDATE ON vendas.vendedor
FOR EACH ROW
EXECUTE PROCEDURE dont_duplica();


-- 5. Crie um TRIGGER que não permita cadastrar vendas em finais de semana. Caso algum vendedor tente fazer isso, dispare uma exceção e rejeite a operação.

-- Extrair sábado e domingo
select *
from vendas.venda
where extract(DOW from data) in (0,6);

-- Função
CREATE OR REPLACE FUNCTION verifica_dia() RETURNS TRIGGER AS
$$
BEGIN
	-- SE FOR (0,6) ENTAO RAISE EXCEPTION 'Fora do horário comercial permitido.'	
	IF CURRENT_DATE = extract(DOW from data) in (0,6)
		THEN RAISE EXCEPTION 'Fora do horário comercial permitido.';
	END IF;
END;
$$ LANGUAGE 'plpgsql';

-- Trigger
CREATE TRIGGER sem_capitalismo_fds
BEFORE INSERT OR UPDATE ON vendas.venda
FOR EACH ROW
EXECUTE PROCEDURE verifica_dia();

