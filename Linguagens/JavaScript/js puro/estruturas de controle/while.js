// Quantidade indeterminada (e determinada) de vezes
function getInteiroAleatorioEntre(min, max) {
    const valor = Math.random() * (max - min) + min
    // Se Math.random() for 0, o valor retornado será o valor minimo.
    // Se Math.random() for 1, o valor retornado será  o valor máximo.
    // Qualquer outro Math.random(), o valor retornado estará dentro do intervalo (max - min).
    return Math.floor(valor)
}

let opcao = 0

while(opcao != -1 ) {
    opcao = getInteiroAleatorioEntre(-1, 10)
    console.log(`A Opção escolhida foi ${opcao}.`)
}

console.log('Até a próxima!')