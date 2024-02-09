const usuarios = [
    { 
        nome: 'Paulo', idade: 45, 
        ativo: false 
    },
    {
        nome: 'Lucca',
        idade: 33,
        ativo: false
    },
    {
        nome: 'Bruna',
        idade: 31,
        ativo: true
    }
]

// Calculando a média das idades...
const resultado = usuarios.map(u => u.idade).reduce(function(acumulador, atual) {
    //console.log(acumulador, atual)
    return (acumulador + atual)/usuarios.length
})

console.log(resultado)