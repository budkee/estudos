let frutas = [ 'banana', 'maça', 'uva', 'abacaxi']
frutas.pop() // Retira o abacaxi (último) da lista
console.log(frutas)

frutas.push('tomate')
console.log(frutas)

frutas.shift() // Retira a banana da lista (o primeiro da lista)
console.log(frutas)
frutas.unshift('Laranja')
console.log(frutas)
// --------- Resetando a lista --------------------
console.log('--------------------------------------')
frutas = [ 'banana', 'maça', 'uva', 'abacaxi']
console.log(frutas)
// Adicionando elementos:

frutas.splice(0, 0, 'Tomate', 'Limão', 'Laranja')
console.log(frutas)
frutas.splice(2, 0, 'Cacau', 'Abacate', 'Cajá')
console.log(frutas)

// Removendo elementos:

frutas.splice(5, 1, 'Laranja persa')
console.log(frutas)

// --------- Resetando a lista --------------------
console.log('\n--------------------------------------')
frutas = [ 'banana', 'maça', 'uva', 'abacaxi']
console.log('Lista original:', frutas)

// Gerando um novo array a partir frutas:
const algumasFrutas = frutas.slice(/* Gere um novo array a partir do índice*/ 3 )

// O 3ro índice é incluso
console.log(algumasFrutas)

const algumasFrutas1 = frutas.slice(/* A partir do índice*/ 0,/* gere um novo array até o indice */ 3 /* não o incluindo. */)
console.log(algumasFrutas1)