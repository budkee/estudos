function tratarErroELancar(erro) {
    throw new Error('...')
    throw {
        nome: erro.nome,
        msg: erro.mensagem,
        date: new Date
    }
    throw 'qualquerCoisa'
    throw 110
    
}



function imprimirNomeGritado(obj) {
    try {
        console.log(obj.nome.toUpperCase() + '!!!')
    } catch (erro) {
        tratarErroELancar(erro)
    } finally {
        console.log('final')
    }
    
}

const obj = {nome: 'Roberto'}
imprimirNomeGritado(obj)
