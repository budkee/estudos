Array.prototype.filter2 = function(callback) {
    const novoArray = []
    for (let i = 0; i < this.length; i++) {
        
        if(callback(this[i], i, this)) {
            novoArray.push(this[i])
        }
    } 
    return novoArray
}


const produtos = [ 
    { 
        nome: 'Notebook',
        preco: 2488,
        fragil: true,
    },
    { 
        nome: 'iPad pro',
        preco: 5000,
        fragil: true,
    },
    { 
        nome: 'Copo de Vidro',
        preco: 28,
        fragil: true,
    },
    { 
        nome: 'Copo de plástico',
        preco: 3.99,
        fragil: false,
    }
]

const filtroCaro = produto => produto.preco >= 500
const filtroFragil = produto => produto.fragil;

const resultado = produtos.filter2(filtroCaro).filter2(filtroFragil)

console.log(resultado) 