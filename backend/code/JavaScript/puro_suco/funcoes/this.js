// Aula 92 
// É uma forma de referenciar um determinado objeto dentro de um determinado contexto;
// Aula feita pelo console, revise esse conteúdo.
// O this não varia em uma função arrow.
// Avalie o contexto no qual o this está contido ou apontando.

//---------------------------------
// Aula 93
// Função Bind e o this
const pessoa = {
    saudacao: 'Bom dia!',
    falar() {
        console.log(this.saudacao)
    }
}

pessoa.falar()
const falar = pessoa.falar
falar() // Conflito entre os paradigmas funcional e OO

const falarDePessoa = pessoa.falar.bind(pessoa) // Amarra um objeto/função com uma outra função/objeto.
falarDePessoa() 

//--------------------------------
// Aula 94
// Solução com o bind
function Pessoa2() {
    this.idade = 0
    setInterval(function() {
        this.idade++
        console.log(this.idade)
    }.bind(this), 1000 /* 1000 milisegundos = 1 segundo; Quem dispara essa função é um temporizador */) 
}
new Pessoa2
// Solução usando self
function Pessoa3() {
    this.idade = 0

    const self = this
    setInterval(function() {
        this.idade++
        console.log(this.idade)
    }.bind(this), 1000 /* 1000 milisegundos = 1 segundo; Quem dispara essa função é um temporizador */)
}
new Pessoa3