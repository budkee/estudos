// Funções de juros
// O Tempo e a Taxa são em anos.

// Função 1
function jurosSimples(capInicio, taxaAplicacao, tempoAplicacao) {
    juros = capInicio * taxaAplicacao * tempoAplicacao //Juros Total (R$) 
    montanteSimples = capInicio + juros 
    return montanteSimples
}

// Função 2
function jurosComposto(capInicio, taxaAplicacao, tempoAplicacao) {
    juros = capInicio * ((1+taxaAplicacao)**tempoAplicacao - 1)
    montanteComposto = capInicio * ((1+taxaAplicacao)**tempoAplicacao)

    return montanteComposto
}

console.log(jurosSimples(100,0.1,5))
console.log(jurosComposto(1000,0.1,4))