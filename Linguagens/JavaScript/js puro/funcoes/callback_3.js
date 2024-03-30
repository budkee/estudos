// Aula 101 - Exemplo para ser executado no browser
document.getElementsByTagName('body') [0].onclick = function (evento) {
    console.log('O evento ocorreu!')
}

// Ao recarregar o browser, o callback não funciona, há de reintegrar o código para o console do browser.