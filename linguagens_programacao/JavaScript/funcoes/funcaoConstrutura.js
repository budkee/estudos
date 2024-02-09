function Carro(velMax = 200, delta = 5) {
    // class private
    let velAtual = 0
    // class public
    this.acelerar = function () {
        if (velAtual + delta <= velMax) {
            velAtual += delta
        } else {
            velAtual = velMax
        }
    }
    // class public
    this.getvelAtual = function () {
        return velAtual
    }
}

const uno = new Carro
uno.getvelAtual()
uno.acelerar()
console.log(uno.getvelAtual())

const ferrari = new Carro(350, 20)
console.log(ferrari.getvelAtual())
ferrari.acelerar()
ferrari.acelerar()
console.log(ferrari.getvelAtual())