// Tabela Verdade

// E
// V e V -> V
// V e F -> F
// F e ? -> F

// Ou
// V ou ? -> V
// F ou V -> V
// F ou F -> V 

// Revisar.
// V xor V -> F
// V xor F -> V 
// F xor V -> V
// F xor F -> F

// Negação
// !V -> F
// !F -> V

// Exemplo:

function compras(trabalho1, trabalho2) {
    const comprarSorvete = trabalho1 || trabalho2 // Ou: Se um deles for V, toda expressão será V.
    const comprarTv50 = trabalho1 && trabalho2 // E: Se o primeiro for falso, o resto da expressão será F.
    const comprarTv32 = trabalho1 != trabalho2 // Ou exclusivo: pode ser utilizado com a diferença.
    const manterSaudavel = !comprarSorvete // Negação lógica: não tomará sorvete.

    return { comprarSorvete, comprarTv50, comprarTv32, manterSaudavel } //ES2015: cria automaticamente um objeto chave-valor, onde, a constante é a chave e o valor das operações logicas é o valor.
}

console.log(compras(true, true))
console.log(compras(true, false))
console.log(compras(false, true))
console.log(compras(false, false))
