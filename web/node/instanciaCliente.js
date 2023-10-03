
const contadorA = require('./instanciaUnica')
const contadorB = require('./instanciaUnica')


const contadorC = require('./instanciaNova')() // O () invoca a função factory do arquivo requirido.
const contadorD = require('./instanciaNova')()

// Teste
contadorA.inc()
contadorA.inc()
console.log(contadorA.valor, contadorB.valor)

contadorC.inc()
contadorC.inc()
console.log(contadorC.valor, contadorD.valor)