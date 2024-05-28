function regimeDeCapitalizacaoSimples (c, i, n) {
    j = c * i * n //Juros Total (R$) 
    MontCap = c + j // Montante Final em R$ 
    return MontCap
}

let c = 100
let i = 0.1 // ao ano (a.a)
let n = 5 // anos

console.log(`O montante final da capitalização simples obtida após 5 anos com uma taxa de juros de 10% a.a e um capital inicial de R$100 é de R$${regimeDeCapitalizacaoSimples(c, i, n)}.`)