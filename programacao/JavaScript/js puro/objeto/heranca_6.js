// Função construtora
function Aula(nome, videoID) {
    this.nome = nome
    this.videoID = videoID
}
// Criação de objetos a partir da função construtora, ou Instanciando objetos a partir da função construtora.
const aula1 = new Aula('Bem Vindo', 123)
const aula2 = new Aula('Até mais', 456)

//Simulando o 'new' mostrando os conceitos de herança

function nova(f, ...params) {
    const obj = {}
    obj.__proto__ = f.prototype
    f.apply(obj, params)
    return obj
}

const aula3 = nova(Aula, 'Olá', 444)
const aula4 = nova(Aula, 'Tchau', 222)
console.log(aula3, aula4)