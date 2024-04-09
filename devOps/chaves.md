# Chaves Secretas

## O que são chaves públicas?

Chaves públicas são um componente fundamental da criptografia de chave pública, um método de criptografia que utiliza um par de chaves para comunicação segura. Cada usuário tem um par de chaves: uma chave pública e uma chave privada. A chave pública é compartilhada livremente com outros usuários ou sistemas, enquanto a chave privada é mantida em segredo.

A chave pública é usada para criptografar mensagens ou dados antes de serem enviados. Uma vez criptografados com a chave pública, os dados só podem ser descriptografados pela chave privada correspondente. Isso permite que os usuários enviem mensagens seguras uns aos outros sem compartilhar suas chaves privadas.

## O que são chaves privadas?

Chaves privadas são a contraparte das chaves públicas em sistemas de criptografia de chave pública. Cada usuário ou entidade possui uma chave privada que é mantida em segredo absoluto. A chave privada é usada para descriptografar mensagens ou dados que foram criptografados com a chave pública correspondente.

Em um sistema de criptografia de chave pública, a chave privada nunca deve ser compartilhada com ninguém, exceto o proprietário da chave. Se a chave privada for comprometida, a segurança de todas as comunicações que dependem dela estará em risco.

## Como criar chaves para a minha máquina?

Para criar chaves para a sua máquina, você pode usar ferramentas e bibliotecas disponíveis para a geração de chaves criptográficas. Aqui está um exemplo simples de como você pode criar um par de chaves usando o OpenSSL, uma ferramenta de código aberto amplamente utilizada para criptografia:

### Usando OpenSSL para gerar um par de chaves RSA:

1. Abra o terminal ou prompt de comando em seu sistema.

2. Use o seguinte comando para gerar uma chave privada RSA de 2048 bits e armazená-la em um arquivo chamado `chave-privada.pem`:

    openssl genpkey -algorithm RSA -out chave-privada.pem -pkeyopt rsa_keygen_bits:2048

3. Agora, você pode extrair a chave pública correspondente da chave privada gerada:

    openssl rsa -pubout -in chave-privada.pem -out chave-publica.pem

Isso criará a chave pública e a salvará em um arquivo chamado chave-publica.pem.

## Links e Referências

- [Keypairs on AWS EC2 Instances](https://github.com/kamranahmedse/developer-roadmap/blob/master/src/data/roadmaps/aws/content/101-ec2/103-keypairs.md)