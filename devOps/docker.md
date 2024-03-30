# Docker

## Banco de Dados
### Container para MySQL Server

    docker pull mysql
    docker run --name mysql_server -e MYSQL_ROOT_PASSWORD=sirius -d -p 3306:3306 mysql
    docker network create rede
    docker network connect rede mysql_server

### Container para Interface do PhpMyAdmin

    docker pull phpmyadmin
    docker run --name pma_interface -e PMA_ARBITRARY=1 -d -p 8090:80 phpmyadmin
    docker network connect rede pma_interface
