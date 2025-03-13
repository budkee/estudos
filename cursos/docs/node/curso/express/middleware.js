// Exemplo para aplicação do padrão middleware/chain of responsability
// Passos para o processamento
const passo1 = (contexto, next) => {
    contexto.valor1 = 'oi'
    next()
}

const passo2 = (contexto, next) => {
    contexto.valor2 = 'oie'
    next()
}

const passo3 = contexto => contexto.valor3 = 'oiee'

// Função executora
const exec = (contexto, ...middlewares) => {
    const execPasso = indice => {
        // Verifica
        middlewares && indice < middlewares.length && middlewares[indice](contexto, () => execPasso(indice + 1))
    }
    execPasso(0)
}

// Teste
const contexto = {}
exec(contexto, passo1, passo2, passo3)
console.log(contexto)