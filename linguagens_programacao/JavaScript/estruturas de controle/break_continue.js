const nums = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]

for (let x in nums) {
    if (x == 5) {
        break // Ele age em relação ao bloco mais próximo dele. Neste caso, ele não age sobre o bloco if, e sim, sobre o bloco for.
    }
    console.log(`Índice ${x} = Valor ${nums[x]}`)
}
console.log(10 * ('---'))
for (let y in nums) {
    if (y == 5) {
        continue
    }
    console.log(`Índice ${y} = Valor ${nums[y]}`)
}
rotulo: 
for (let a in nums) {
    for (let b in nums) {
        if  (a == 2 && b ==3) break rotulo
        console.log(`Par = (${a},${b}) `)
    }
}