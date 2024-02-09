const usuarios = [
    { 
        nome: 'Paulo', 
        idade: 45, 
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
    },
    {
        nome: 'Jorge',
        idade: 18,
        ativo: true
    }
]

// Calculando a média das idades com duas abordagens diferentes
// Imperativo: demonstra o como fazer isso.
let total1 = 0
for (i=0; i < usuarios.length; i++) {
    total1 += usuarios[i].idade
}
console.log(total1 / usuarios.length)

// Declarativo: você declara tudo que vai precisar e armazena os valores em constantes ou varáveis e trabalha a lógica do resultado final.
const pegarIdade = usuarios => usuarios.idade
const soma = (total, valorAtual) => total + valorAtual

const total2 = usuarios.map(pegarIdade).reduce(soma)
console.log(total2/usuarios.length)