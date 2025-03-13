import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Criação dos objetos
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Início do Job
job.init(args['JOB_NAME'], args)


source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Criação do dataframe
df = glueContext.create_dynamic_frame.from_options(
    
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {
        "withHeader": True, "separator": ","
    }
    
    )

# Filtros de interesse
# 1. Colocar os valores da coluna 'nome' em Maiúsculo
only_1934 = df.filter(lambda row: row['anoLancamento'] == '1934')
# 2. Contagem das linhas do DataFrame
# 3. Contagem de nomes agrupado por ano e sexo, e ordenado por ano de modo decrescente
# 4. Nome feminino mais registrado e o respectivo ano de registro
# 5. Nome masculino mais registrado e o respectivo ano de registro
# 6. Total de registros para cada ano (Apresentar as 10 primeiras linhas ordenada por Ano de modo crescente)

# Outputs

glueContext.write_dynamic_frame.from_options(
    
    frame = only_1934,
    connection_type = "s3",
    connection_options = { "path":target_path },
    format = "parquet"

    )

# Fim do Job
job.commit()