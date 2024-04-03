# Hypertext Transfer Protocol (HTTP)

## O que é?

Os métodos HTTP são verbos que indicam a ação que um cliente solicita que o servidor web execute em um recurso específico. Eles são parte fundamental do protocolo HTTP e são usados para realizar operações em recursos disponíveis em servidores web. Cada método tem um significado específico, determinando como a requisição deve ser processada pelo servidor e qual ação deve ser executada no recurso solicitado.

## Métodos HTTP

### GET

O método GET é usado para solicitar dados de um recurso específico no servidor web. Ele é usado para **buscar informações**, como páginas HTML, imagens, arquivos, entre outros, e não deve ter efeitos colaterais no servidor. Em termos simples, quando você abre uma página da web em um navegador, uma requisição GET é enviada para o servidor para obter e exibir o conteúdo da página.

### POST

O método POST é utilizado para enviar dados para o servidor web, geralmente para criar ou atualizar recursos. Ao contrário do GET, o POST pode ter efeitos colaterais no servidor, como criar um novo registro em um banco de dados ou enviar informações de um formulário para processamento. Ele é comumente usado em formulários da web para **enviar dados de entrada do usuário**.

### PUT

O método PUT é usado para atualizar ou substituir completamente um recurso específico no servidor. Ao enviar uma requisição PUT, o cliente envia uma representação completa do recurso com as modificações desejadas. Isso significa que o recurso será substituído pelo novo estado enviado na requisição PUT. O PUT é útil quando se deseja **atualizar completamente um recurso existente**.

### DELETE

O método DELETE é utilizado para remover um recurso específico do servidor web. Quando uma requisição DELETE é enviada para um recurso, **o servidor é instruído a removê-lo permanentemente do sistema**. Este método é usado quando não se deseja mais que um recurso exista no servidor, como deletar um post em um blog, remover um arquivo, entre outros. É uma operação que deve ser usada com cuidado, pois a exclusão é irreversível.
