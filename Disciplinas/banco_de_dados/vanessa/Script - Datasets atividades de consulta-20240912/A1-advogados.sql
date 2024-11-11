DROP TABLE IF EXISTS advogado;

CREATE TABLE advogado(
  registro INTEGER PRIMARY KEY,
  nome VARCHAR(255),
  numero_cliente INTEGER
 );
   
 INSERT INTO advogado(registro, nome, numero_cliente)
 VALUES (1648, 'Marty M. Harrison', 5),
	(2427, 'Jonathan J. Blevins', 15),
	(3365, 'Chelsey D. Sanders', 20),
	(4153, 'Dorothy W. Ford', 16),
	(5525, 'Penny J. Cormier', 6);