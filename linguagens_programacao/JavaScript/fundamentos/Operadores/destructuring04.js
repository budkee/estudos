function rand([min = 0, max = 1000]) {
    if (min > max) [min, max] = [max, min]
    const valor = Math.random() * (max - min) + min
    return Math.floor(valor)
}

console.log(rand([50, 40])) // [max, min]
console.log(rand([992])) // Apenas o min
console.log(rand([, 10])) // Apenas o max
console.log(rand([]))
console.log(rand())
