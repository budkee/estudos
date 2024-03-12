const quaseArray = { 0: 'Rafael', 1: 'Jorge', 2: 'Bia'}
console.log(quaseArray)
Object.defineProperty(quaseArray, 'toString', {
    value: function() {
        return Object.values(this),
        enumerable; false
    }
})

console.log(quaseArray[0])

// O array propriamente dito
const array = [ 'Rafael', 'Jorge', 'Bia']
console.log(array)