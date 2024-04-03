// Função para Juros Simples
/**
 * A primeira função retornará o montante da aplicação financeira sob o regime de juros simples e a segunda retornará o valor da aplicação sob o regime de juros compostos. 
 * @date 22/03/2024 - 12:00:19
 *
 * @param {*} capInicio
 * @param {*} taxaAplicacao
 * @param {*} tempoAplicacao
 * @returns {*}
 */
function jurosSimples(capInicio, taxaAplicacao, tempoAplicacao) {
    juros = capInicio * taxaAplicacao * tempoAplicacao //Juros Total (R$) 
    montanteSimples = capInicio + juros 
    return montanteSimples
}

// Função para Juros Composto
function jurosComposto(capInicio, taxaAplicacao, tempoAplicacao) {
    juros = capInicio * ((1+taxaAplicacao)**tempoAplicacao - 1)
    montanteComposto = capInicio * ((1+taxaAplicacao)**tempoAplicacao)

    return montanteComposto
}

console.log(jurosSimples(100,0.1,5))
console.log(jurosComposto(1000,0.1,4))