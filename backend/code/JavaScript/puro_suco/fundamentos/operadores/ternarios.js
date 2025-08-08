// Operadores ternários,
// 1ra parte: expressão relacional.
// 2da parte: (?) resultado caso seja V.
// 3ra parte: (:) resultado caso seja F.

const resultado1 = nota => nota >= 7 ? 'Aprovado' : 'Reprovado'

// Ou

const resultado2 = nota => {
    return nota >= 7 ? 'Aprovado' : 'Reprovado'
}

console.log(resultado1(7.1))
console.log(resultado2(6.2))

