const a = 1
const b = 2
const c = 3

const obj1 = { a, b, c }
console.log(obj1)

const nomeAtr = 'nota'
const valorAtr = 7.9

const obj2 = { }
obj2[nomeAtr] = valorAtr
console.log(obj2)

const obj3 = { [nomeAtr]: valorAtr}
console.log(obj3)

const obj4 = {
    funcao1 : function() {
        // ...
    },
    funcao2() {
        // ...
    }
}
console.log(obj4)