let array = [1, 2, 30, 4, 5]
// Desse array, como eu retiro o menor valor?
// Looping de contagem
var numRecorde = 0
var numPiorJogo = 0

function temporada(array) {
    for (let i in array) {
        let recordeAtual = 0
        let piorJogo = 0
        if (array[i+1] < array[i+2]) {
            recordeAtual = array[i+2]
            numRecorde =+ 1
        } else if (array[i+1] >= array[i+2]) {
            continue
        } else if (array[i] < array[i+1]) {
            piorJogo = array[i]
            
        }
    }    
    return console.log([numRecorde, numPiorJogo])
}

for (let i in array) {
    var numRecorde = 0
    if (array[i+1] < array[i+2]) {
        numRecorde = array[i+1]
        console.log(numRecorde)
    }   
} return [numRecorde]