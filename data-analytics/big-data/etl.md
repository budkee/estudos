## Seção 8: ETL - Extração, Transformação e Carga de Dados

Assim como o petróleo necessita passar por processos para conseguirem ser utilizados, os dados em sua forma bruta também precisam de transformações. Diante disso, têm-se dois pipelines de dados: __ETL__ e __ELT__.

Os dois processos iniciam de forma semelhante, extraindo dados brutos oriundos de diversas possíveis fontes, como databases e/ou arquivos. A partir disso é que se divergem.

Após a extração dos dados, o próximo passo do ETL é transforma-los, normalmente ocupando uma _staging area_, e então armazena-los para depois serem utilizados para análises.

Já no ELT, os dados assim que extraídos já serão armazenados em sua forma bruta, para então os dados que forem necessários serem transformações depois. Essa inversão visa agilizar o pipeline de tratamento de dados, dado a grande velocidade de geração de novos dados.

-----
### Principais ferramentas de integração de dados para solucionar ETL e ELT:
* __Oracle Data Integration__ é uma ferramenta propritetária
* __Pentaho Data Integrator (PDI)__ é uma ferramenta propritetária
* __Apache Nifi__ é uma ferramenta open-source
* __Apache Spark__ é uma ferramenta open-source
* __Power Center__ é uma ferramenta propritetária
* __Apache Airflow__ é uma ferramenta open-source

Note que as ferramentas proprietárias normalmente vêm com auxilio de interfaces, não exigindo muitos códigos.

### Principais ferramentas para solução de ETL e ELT via Cloud Computing:
* __Azure Date Factory__ que possui integração com produtos Microsoft
* __AWS Glue__ tem como característica não necessitar de um servidor
* __AWS Athena__