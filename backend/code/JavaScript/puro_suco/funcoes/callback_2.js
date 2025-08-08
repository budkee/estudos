const notas = [9, 1, 4.4, 9.8, 7, 2.2, 6, 7.3, 8.2]

// Sem callback
let notasBaixas = []
for (let i in notas) {
    if (notas[i] < 7) {
        notasBaixas.push(notas[i])
    }
}
console.log('Sem Callback')
console.log(notasBaixas, '\n')

// Com callback ----------------------------
// Sem a função arrow
const notasBaixas2 = notas.filter(function (nota){
    return nota < 7
})
console.log('Callback sem a função arrow')
console.log(notasBaixas2, '\n')
// Com a função arrow
const notasMenorQue7 = nota => nota < 7;
const notasBaixas3 = notas.filter(notasMenorQue7);
console.log('Callback com a função arrow')
console.log(notasBaixas3)