#!/bin/bash

# Subir arquivo de log para o HDFS
hdfs dfs -mkdir -p /logs
hdfs dfs -put -f input/access_log.txt /logs/

# Executar o MapReduce
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
  -input /logs/access_log.txt \
  -output /output_logs \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py

# Mostrar resultado
hdfs dfs -cat /output_logs/part-00000
