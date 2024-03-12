// json = JavaScript Object Notation (Formato textual)
// Objeto é uma coleção de chaves-valores

const prod1 = {} // Representa um objeto (Temos um objeto vazio)
prod1.nome = 'Celular Ultra Mega'
prod1.preco = 12334.90
prod1['Desconto legal'] = 0.40 // Evitar atributos com espaço

console.log(prod1)

const prod2 = {
    nome: 'Camisa Polo',
    preco: 79.90,
    
    obj: {
        propriedade: 1,
        obj: {
            propriedade: 2
        }
    }
}

// JSON 
'{"nome": "Camisa Polo", "preco": 79.90}' 