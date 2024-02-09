// Função da divisão - Parâmetros (dividendo,divisor), Retorno (resto, quociente)
function Divisao(dividendo, divisor) {
    quoc = dividendo / divisor
    resto = dividendo % divisor
    return [resto, quoc]
}
console.log(Divisao(323, 2))