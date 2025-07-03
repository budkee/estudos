FROM postgres:latest

COPY postgres.conf /etc/postgresql/postgresql.conf

CMD [ "postgres", "-c", "config_file=/etc/postgresql/postgresql.conf" ]

# ENTRYPOINT [ "chmod", "644", "docker-entrypoint-initdb.d/init.sql" ]
