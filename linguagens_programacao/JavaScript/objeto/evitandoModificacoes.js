// Alguns métodos para restringir o código/objeto.
// Object.preventExtensions
// Podemos apenas deletar ou alterar atributos porém não podemos adicionar novos atributos

const produto = Object.preventExtensions(
    {
        nome: 'Qualquer',
        preco: 3.99,
        tag: 'promoção'
    }
)
console.log('O objeto é extensível:', Object.isExtensible(produto))
produto.nome = 'Borracha'
produto.descricao = 'Borracha escolar branca'
delete produto.tag
produto.data = '12/09/2022' 

console.log(produto)

// Object.seal
// Podemos apenas alterar os valores dos atributos, não podendo adicionar ou deletar atributos.
const pessoa = { nome: 'Ju', idade: 38 }
Object.seal(pessoa)
console.log('O objeto está selado:', Object.isSealed(pessoa))

delete pessoa.nome
pessoa.sobrenome = 'Silva'
pessoa.idade = 33
console.log(pessoa)

// Object.freeze = selado + valores constantes
// Não se pode alterar, deletar ou adicionar novos atributos
const cadeira = {
    braco: 'largo',
    poltrona: false,
    madeira: 'carvalho'
} 
Object.freeze(cadeira)
cadeira.tamanhoAltura = 10
delete cadeira.braco
console.log(cadeira)
