const sequencia = {
    _valor: 1, // O uso do _ é uma convenção para mostrar que a variável é encapsulada/privada;
    get valor() { return this._valor++},
    set valor(valor) {
        if (valor > this._valor) {
            this._valor = valor
        }
    }
}

console.log(sequencia.valor, sequencia.valor)
sequencia.valor = 1000
console.log(sequencia.valor, sequencia.valor)
sequencia.valor = 900 // Ele não retorna por conta da condição que foi imposta na linha 5
console.log(sequencia.valor, sequencia.valor)