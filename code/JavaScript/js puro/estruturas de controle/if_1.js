function soBoaNoticia(nota) {
    if (nota >= 7) {
        console.log('Aprovado com ' + nota)
    }
}

soBoaNoticia(8.1)
soBoaNoticia(6.1) // Não retorna

function seForVerdadeEuFalo(valor) {
    if (valor) {
        console.log('É verdade...' + valor)
    }
}

seForVerdadeEuFalo() //Undefined -> False
seForVerdadeEuFalo(null) // False
seForVerdadeEuFalo(undefined) // False
seForVerdadeEuFalo(NaN) // False
seForVerdadeEuFalo('') // False
seForVerdadeEuFalo(0) // False
seForVerdadeEuFalo(-1) // True
seForVerdadeEuFalo(' ') //True
seForVerdadeEuFalo('?')
seForVerdadeEuFalo([])
seForVerdadeEuFalo([1, 2])
seForVerdadeEuFalo({})
