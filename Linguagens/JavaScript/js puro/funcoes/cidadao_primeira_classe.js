// Função em JS é First-Class Object (ou First-Class Cítizens)
// Higher-order Fuction
// Isto significa que a função pode ser vista como um dado. Você pode passar uma função como parâmetro, por exemplo.

// Forma literal
function fun1() { }

// Armazenando uma função em uma variável 
const fun2 = function () {}

// Armazenando uma função em um array
const array = [function (a,b) { return a + b }, fun1]
console.log(array[0](2,3))

// Armazenando uma função em um atributo de objeto
const obj = {}
obj.falar = function () {return 'Opa!'}
console.log(obj.falar())

// Passando uma função como parâmetro
function run(fun) {
    fun()
}
run (function () { console.log('Executando...')})

// Uma função pode retornar ou conter uma outra função.
function soma (a,b) {
    return function(c) {
        console.log(a + b + c)
    }
}
soma (2 ,3)(4)
const cincoMais = soma(2,3)
cincoMais(9)