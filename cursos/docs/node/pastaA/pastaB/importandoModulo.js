const moduloA = require('../../moduloA')
console.log(moduloA.ola)

const lobash = require('lobash')
console.log(lobash.ola)

const msn = require('../pastaB/pastaC')
console.log(msn.msn)

// Módulos core
const http = require('http')

http.createServer((req, res) => {
    res.write('Cafe e tudo de bom!')
    res.end() // Finalizar a resposta
}).listen(8080)