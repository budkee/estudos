function calcularSalario(qntTrabalhadaPorHora , valorPorHora) {
    salarioMensal =  qntTrabalhadaPorHora * valorPorHora
    return console.log(`Salário do Mês: R$${salarioMensal}`)
}
calcularSalario(150,40.5)
