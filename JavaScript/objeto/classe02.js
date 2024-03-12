// Utilizando Herança com Classe
class Avo {
    constructor(sobrenome) {
        this.sobrenome = sobrenome
    }
}

class Pai extends Avo {
    constructor(sobrenome, profissao = 'Professor') {
        // super de superclasse, que no caso é o Avo
        super(sobrenome)
        this.profisssao = profissao
    }
}

class Filho extends Pai {
    constructor() {
        super('Silva')
    }
}

// Instanciando a classe..
const filho = new Filho
console.log(filho)