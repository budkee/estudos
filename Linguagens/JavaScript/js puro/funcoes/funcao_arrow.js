// Funções Arrow #01 - Aula 95

let dobro = function (a) {
    return 2 * a
}

dobro = (a) => {
    return 2 * a
}

dobro = a => 2 * a // Retorno implícito com a sintaxe reduzida.

console.log(dobro(Math.PI))

let ola = function () {
    return 'Olá!'
}
ola = () => 'Olá!'
ola = _ => 'Olá!' // Possui parâmetro
console.log(ola())

// Funções Arrow #02 - Aula 96

function Pessoa() {
    this.idade = 0

    setInterval(() => {
        this.idade++
        console.log(this.idade)
    }, 1000)
}
// new Pessoa

// Funções Arrow #03 - Aula 97

let comparaComThis = function (param) {
    console.log(this === param)
}
 comparaComThis(global)

 const obj = {}
 comparaComThis = comparaComThis.bind(obj) // Aqui ele não mais aponta para o escopo global e passa a apontar para o obj
 comparaComThis(global)
 comparaComThis(obj)

 let comparaComThisArrow = param => console.log(this === param)
 comparaComThisArrow(global)
 comparaComThisArrow(module.exports /* ou this */)

 comparaComThisArrow = comparaComThisArrow.bind(obj)
 comparaComThisArrow(obj)
 comparaComThisArrow(module.exports)