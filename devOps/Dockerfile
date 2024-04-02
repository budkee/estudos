FROM ubuntu:latest

# Copie o script para dentro do container
COPY setup.sh /setup.sh

# Defina o script como executável
RUN chmod +x /setup.sh

# Adicione a execução do script ao final do arquivo de inicialização do container
CMD ["/setup.sh"]
