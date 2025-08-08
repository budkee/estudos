// Retira algum elemento de um objeto { } ou de um array []. ES2015.

const [a] = [10]
const [n1, n2, n3, n4, n5, n6 = 0] = [10, 7, 9, 8]
const [,[, nota]] = [[, 8, 8], [9, 6, 8]] // Revisar.

console.log(a)
console.log(n1, n3, n5, n6)
console.log(nota)
