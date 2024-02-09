const valores = [7.7, 8.9, 6.3, 9.2]
console.log(valores[0], valores[3])
console.log(valores[4]) // valor indefinido

valores[4] = 10
console.log(valores)
console.log(valores.length) // Quantidade de elementos dentro do array.

valores.push({id: 3}, false, null, 'teste') // Adiciona elementos ao array.
console.log(valores)

console.log(valores.pop()) // Retira o ultimo elemento do array.
delete valores[0] 
console.log(valores)

console.log(typeof valores) // É um objeto.
