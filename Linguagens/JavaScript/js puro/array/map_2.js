const carrinho = [
    '{"nome": "Borracha", "preco": 3.55 }',
    '{"nome": "Caneta", "preco": 7.95}',
    '{"nome": "FaberCastel", "preco": 43.00}',
    '{"nome": "Caderno", "preco": 25}'
]
// Retorne um array apenas com os preços:

// 1) Transformar o JSON em objeto; 
const paraObjeto = json => JSON.parse(json)
// 2) Criar a função que retorne o preco;
const apenasPreco = produto => produto.preco

// Incluindo a função map...
const resultado = carrinho.map(paraObjeto).map(apenasPreco)
console.log(resultado)

// Revisar esse conteúdo.
