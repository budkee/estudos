const fs = require('fs')

const caminho = __dirname + '/arquivo.json'

// Lendo de forma síncrona:
const conteudo = fs.readFileSync(caminho, 'utf-8')
console.log(conteudo)

// Lendo de forma assíncrona:
fs.readFile(caminho, 'utf-8', (err, conteudo) => {
    const config = JSON.parse(conteudo)
    console.log(`${config.db.host}:${config.db.port}`)
})
// De forma Síncrona, sem importar o fs:
const config = require('./arquivo.json')
console.log(config.db)

// Leitura de uma pasta:
fs.readdir(__dirname, (err, arquivos) => {
    console.log('Conteúdo da pasta:')
    console.log(arquivos)
})