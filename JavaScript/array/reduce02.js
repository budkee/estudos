const usuarios = [
    { 
        nome: 'Paulo', idade: 45, 
        ativo: false 
    },
    {
        nome: 'Lucca',
        idade: 33,
        ativo: false
    },
    {
        nome: 'Bruna',
        idade: 31,
        ativo: true
    }
]

// Desafio 01: Todos os usuários são ativos?
const todosAtivos = (resultado, usuario) => /* Condição */ resultado && usuario

const resultado01 = usuarios.map(a => a.ativo).reduce(todosAtivos)
console.log(resultado01)

// Desafio 02: Algum usuário é ativo? 
const algumAtivo = (resultado, usuario) => resultado || usuario
const resultado02 = usuarios.map(a => a.ativo).reduce(algumAtivo)
console.log(resultado02)