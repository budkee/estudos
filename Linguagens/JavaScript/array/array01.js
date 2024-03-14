console.log(typeof Array, typeof new Array, typeof [])
//-----------------------------------------------
let aprovados = new Array('Bia', 'Carlos', 'Ana')
console.log(aprovados)
// ou
aprovados = ['Bia', 'Carlos', 'Ana']
//-----------------------------------------------
console.log(aprovados[0])
console.log(aprovados[1])
console.log(aprovados[2])
// E se eu tentar o 3ro índice?
console.log(aprovados[3])
// Adicionando o 3ro índice...
aprovados[3] = 'Paulo' // Intuitivo
aprovados[9] = 'Rafael'
// ou
aprovados.push('Abismo') // Tradicional

// Quantos elementos eu tenho no array?
console.log(aprovados.length)

console.log(aprovados[8])
console.log(aprovados[8] === undefined)

console.log(aprovados)
aprovados.sort() // Ordena os elementos do array
console.log(aprovados)

// Como excluir elementos?
delete aprovados[1]
console.log(aprovados)

// ------------------------------
// 2. Outras funcionalidades:
aprovados = ['Bia', 'Ana', 'Carlos', 'Jorge', 'Matheus']
// 2.1 Manipulação de elementos pelo método .splice()

// Exclusão de elementos
aprovados.splice(/* A partir desse índice */ 1 ,/* Exclua */ 2 /* elementos*/)
console.log(aprovados)

// 2.1.1 Exclusão de elementos com a respectiva substituição  
aprovados.splice(1,2, 'Ronaldo', 'João')
console.log(aprovados)


// 2.1.2 Adição de elementos em lugares específicos 
aprovados.splice(/* A partir desse índice */ 1 ,/* Exclua */ 0 /* elementos */,/* e adicione os seguintes inputs:  */ 'Bobby', 'Thabata')
console.log(aprovados)

// 2.1.3 Substituição de elementos do array por inputs novos
aprovados.splice(/* A partir do índice*/ 1,/* Exclua o índice */1 /* e coloque em seu lugar: */, 'Bola de fogo 1', 'Bola de fogo 2')
console.log(aprovados)

