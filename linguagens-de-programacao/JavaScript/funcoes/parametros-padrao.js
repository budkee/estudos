// Estratégia #1 para gerar valor padrão
function soma1(a,b,c) {
    a = a || 1
    b = b || 1
    c = c || 1
    return a + b + c
} // Retorna com bug ao plotar o parâmetro 0.
console.log(soma1(), soma1(1,1,3), soma1(4), soma1(0,0,0))

//Outras estratégias: 
function soma2(a,b,c) {
    a = a != undefined? a:1 // Estratégia #02
    b = 1 in arguments ? b : 1 // Estratégia #03
    c = isNaN(c) ? 1 : c //Estratégia #04 -> Estratégia segura
    return a + b + c 
} // Não retorna com bugs*
console.log(soma2(), soma2(1,1,3), soma2(4), soma2(0,0,0))

// Valor padrão do ES2015
function soma3(a = 1, b = 1, c = 1) {
    return a + b + c
}
console.log(soma3(), soma3(1,1,3), soma3(4), soma3(0,0,0))