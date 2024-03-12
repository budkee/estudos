let num1 = 1
let num2 = 2

num1++ 
console.log(num1)

--num1 // Prefixo
console.log(num1)

console.log(++num1 === num2--) // Ele compara antes de decrementar. Não recomenda-se 

console.log(num1 === num2)