"""_summary_

Serializing and deserializing data using Avro
Reference: https://avro.apache.org/docs/++version++/getting-started-python/

"""
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

# PATHS
schema_path = "user_schema.avsc"
data_path = "users.avro"

# 1. Getting the schema from a file
schema = avro.schema.parse(open(schema_path, "r").read())

# 2. Creating data
users = [
    {
        "name": "Alyssa", 
        "surname": "Huston",
        "cpf": "123.456.789-01",
        "email": "alyssa@gmail.com"
    },
    {
        "name": "Ben", 
        "surname": "Huston",
        "cpf": "123.433.789-01",
        "email": "baum@gmail.com"
    }

]

# 3. Writing binary data to an Avro file: this will create a file named "users.avro"
with open(data_path, "wb") as out_file:
    writer = DataFileWriter(out_file, DatumWriter(), schema)
    
    for user in users:
        writer.append(user)
    writer.close()

# 4. Reading data from the Avro file
print("Reading data from Avro file:")
with open(data_path, "rb") as in_file:
    reader = DataFileReader(in_file, DatumReader())
    
    for usuario in reader:
        print(usuario)
    reader.close()

