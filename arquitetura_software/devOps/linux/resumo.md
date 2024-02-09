
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

## Sumário | Linux

- [x] Resumo
- [x] Setup
- [x] Sobre
- [x] Links ou Referências
- [x] Certificado

## Resumo

> Neste curso foi possível aprender os conceitos fundamentais de Linux e aplicá-los na máquina virtual, bem como realizar a configuração da distribuição de escolha (Ubuntu), configurar e adicionar pela linha de comando os permissionamentos de usuários e grupos, além de realizar o gerenciamento de arquivos e diretórios. Por fim, foi apresentado conceitos básicos de rede e suas aplicações no ambiente, finalizando com a instalação de LAMP.

### Setup

> Antes de começar, você vai precisar baixar uma Máquina Virtual (VM) na sua máquina local para poder rodar a imagem do Ubuntu ou outra distribuição Linux. 
>
> - [VM para Windows e Mac Intel](https://www.virtualbox.org/wiki/Downloads)
> - [VM para Mac M1](https://mac.getutm.app/)
> 
> Configuração da VM para Mac M1
> 
> - [Passo a passo via Notion](https://www.notion.so/siriusb/Linux-026e819fdf434cc8894eff9cb3010b79?pvs=4)
> - [Vídeo para instalação](https://youtu.be/6mtfncj9vhU)
>

### Sobre
>
>#### Distribuições Linux
>
> São versões derivados de uma versão-pai do Linux. Por ser um sistema de código-aberto, alguns desenvolvedores sentem a necessidade de criar uma nova feature ou outra para melhorar o sistema. Assim, vão sendo criadas novas distribuições do software.
>
> ##### Algumas distribuições ...
>
> | Distribuição | Baseado em | Recomendado para | Sabores |
> | --- | --- | --- | --- | 
> | [Ubuntu](https://ubuntu.com/) |  [Debian](https://www.debian.org/index.pt.html) | Iniciantes com nenhum conhecimento em Linux | Kubuntu; Xubuntu; Lubuntu; Ubuntu MATE;  | 
> | [Elementary OS](https://elementary.io/pt_BR/) | [Ubuntu](https://ubuntu.com/) | Interface amigável para usuários MacOS | - |
> | [Mint](https://linuxmint.com/) | [Ubuntu](https://ubuntu.com/) | Iniciantes com hardware limitado ou debilitado | - |
> | [OpenSUSE](https://www.opensuse.org/) | [Linux](https://pt.wikipedia.org/wiki/Linux) | Administradores de sistemas | [SUSE Leap](https://get.opensuse.org/leap/15.5/); [SUSE Tumbleweed](https://get.opensuse.org/tumbleweed/) | 

> ### Kernel
>
> > É o núcleo responsável pelo direcionamento de ações do aplicativo. Ele serve como "ponte" entre os aplicativos e o hardware da sua máquina.
>
> 
> <a href="https://commons.wikimedia.org/wiki/File:Kernel_Layout.svg#/media/Ficheiro:Kernel_Layout.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/8/8f/Kernel_Layout.svg" alt="Kernel Layout.svg" height="300" width="380"></a>
> Por <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a> e <a href="https://commons.wikimedia.org/w/index.php?curid=4392180">Hiperligação</a>



## Vantagens do Linux
>
> - É um sistema operacional gratuito;
> - É a OS utilizado pela maioria dos servidores web;
> - Utilizado por grandes empresas (AWS, Google, Facebook e Instagram);
> - Requisito para análise de currículo;
> - Comunidade ativa;
> - Segurança;
> - Suporte nativo para várias linguagens;

## Terminal e Shell: qual é a diferença?
>
> ### Terminal
>
> É a interface da linha de comando (CLI) do sistema operacional (SO) que recebe os comandos de interesse do usuário.
> 
> - Windows: `cmd`
> - MacOs e Unix: `terminal`
>
> ### Shell
> 
> É o responsável por processar o comando recebido pelo Terminal.
>
> ## Sintaxe do comando
>
> 
>     servidor@usuario :~$ [comando] -[opcoes] [arquivos/diretorios]
>

> ## Comandos
>
> ### Início da sessão
> Atualizar novas versões do Sistema
> 
>     sudo apt update
>

> ### Busca e análise de objetos
>
> Mover para o diretório anterior
>
>     cd -
>
> Ver os itens do diretório de interesse em formato de lista
>
>     ls -l [diretório]
>
> Ver os itens do diretório de interesse em formato de lista *reversa*
>
>     ls -lr
>
> Ver o conteúdo de cada subdiretório
>
>     ls -R
>

> ### Acessar o manual do comando
>
> Terminal MacOS(Unix):
> 
>     man ls
>
> Terminal Linux:
> 
>     ls --help
>

> ### Diretórios
> 
> Criando um diretório
>
>     mkdir nome-diretorio
>
> Removendo um  diretório
>
>     rm nome-diretorio
>
> ### Arquivos
> 
> Criando um arquivo
>
>     mk nome-diretorio
>
> Removendo um  arquivo
>
>     rm nome-arquivo
>
> ### Download via link
> 
>     wget [link]

> ### Aplicativos
> 
> Instalar apps
> 
>     sudo apt install chromium-browser
>
> Desinstalar apps
>
>     sudo apt remove chromium-browser
>

## Links ou Referências 
> - [Download Ubuntu](https://ubuntu.com/)
> - [Linux Journey](https://linuxjourney.com/)
> - [The Linux Command Line](https://linuxcommand.org/tlcl.php)
> - ["Sabores de Linux: escolha o seu" via Medium](https://medium.com/os-systems/sabores-de-linux-escolha-o-seu-2798a45b3e32)
>
## Certificado
> ![certificado](./img/[2023]linux.jpg)