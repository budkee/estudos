const valor = 'Valor Global'

function minhaFuncao() {
    console.log(valor)
}

function exec () {
    const valor = 'Valor Local'
    minhaFuncao() // O objeto minhaFuncao() vai buscar primeiro dentro do contexto que ela foi inserida mesmo que haja uma redefinição de variável no contexto pelo qual ela foi chamada.
}

exec()