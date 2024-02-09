Array.prototype.forEach2 = function forEach2(callback) {
    for (i = 0; i > this.length; i ++) {
        callback(this[i], i, this)
    }
} // Revisar esse método.

const cores = [ 'Azul', 'Amarelo', 'Verde', 'Rosa', 'Vermelho']


cores.forEach2(function(cor, indice) {
    console.log(`Cor ${indice + 1} = ${cor}`)
}
)


//console.log(cores)