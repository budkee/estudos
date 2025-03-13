# Comandos

Baixar a imagem da amazon do Jupyter Notebook:

    docker pull amazon/aws-glue-libs:glue_libs_4.0.0_image_01

Subir o container, acessando o console do container, montando o volume (-v), passando a variáveis de ambiente (-e), pedindo pra remover depois que parar de utilizar (--rm), dando também um nome (--name), passando a porta de acesso no navegador (-p), identificando a imagem a ser executada no container e por último, o script a ser executado ao ser iniciado:

    docker run -it -v ~/.aws:/home/glue_user/.aws \
    -v $JUPYTER_WORKSPACE_LOCATION:/home/glue_user/workspace/jupyter_workspace/ \ -e AWS_PROFILE=$PROFILE_NAME \
    -e DISABLE_SSL=true \
    --rm \
    -p 8888:8888 \
    --name glue_jupyter_lab \
    amazon/aws-glue-libs:glue_libs_4.0.0_image_01 \
    /home/glue_user/jupyter/jupyter_start.sh

## Link e Referências

- [Docker Hub | Amazon Glue Libs](https://hub.docker.com/r/amazon/aws-glue-libs/tags)
