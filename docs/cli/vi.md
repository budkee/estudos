# Guia Básico de Uso do vi / vim

O `vi` é um editor de texto tradicional em sistemas Unix/Linux. Ele possui modos de operação distintos que precisam ser compreendidos para editar arquivos eficientemente.


## 1. Abrindo o vi

```bash
vi nome_do_arquivo
````

Se o arquivo não existir, ele será criado.

## 2. Modos do vi

O vi possui **dois modos principais**:

1. **Modo Normal (ou Comando)**: usado para navegar e emitir comandos.

   * Ao abrir o arquivo, você está nesse modo.
2. **Modo Inserção**: usado para inserir texto.

### Como alternar:

* `i` → entra no modo inserção **antes do cursor**
* `I` → insere no **início da linha**
* `a` → entra no modo inserção **após o cursor**
* `A` → insere no **final da linha**
* `Esc` → volta para o modo normal

## 3. Movimentação do cursor

No modo normal, use:

* `h` → mover para **esquerda**
* `l` → mover para **direita**
* `j` → mover **para baixo**
* `k` → mover **para cima**
* `0` → início da linha
* `^` → primeiro caractere não vazio da linha
* `$` → fim da linha
* `gg` → início do arquivo
* `G` → fim do arquivo

## 4. Inserindo texto

No modo normal, digite:

* `i` → inserir **antes do cursor**
* `a` → inserir **após o cursor**
* `o` → abre **uma nova linha abaixo**
* `O` → abre **uma nova linha acima**

## 5. Apagando texto

No modo normal:

* `x` → apaga o **caractere sob o cursor**
* `X` → apaga o **caractere antes do cursor**
* `dd` → apaga a **linha inteira**
* `D` → apaga do **cursor até o final da linha**

## 6. Copiar e colar (yank e paste)

* `yy` → copia a **linha inteira**
* `yw` → copia **uma palavra**
* `p` → cola **após o cursor**
* `P` → cola **antes do cursor**

## 7. Salvando e saindo

No modo normal:

* `:w` → salva (write)
* `:q` → sai (quit)
* `:wq` ou `:x` → salva e sai
* `:q!` → sai sem salvar

## 8. Procurar texto

* `/palavra` → procura a palavra **para frente**
* `?palavra` → procura a palavra **para trás**
* `n` → próximo resultado
* `N` → resultado anterior

## 9. Substituição

* `:s/antigo/novo/` → substitui **na linha atual**
* `:%s/antigo/novo/g` → substitui **em todo o arquivo**


## 10. Dicas rápidas

* Use sempre `Esc` para garantir que está no **modo normal** antes de emitir comandos.
* Combine comandos com movimentos:

  * `d$` → apaga do **cursor até o final da linha**
  * `d0` → apaga do **início da linha até o cursor**
  * `y$` → copia do **cursor até o final da linha**
