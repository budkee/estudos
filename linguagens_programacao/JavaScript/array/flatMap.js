const escola = [ {
    nome: 'Turma M1',
    alunos: [{
        nome: 'Gustavo',
        nota: 8.3,
    }, {
        nome: 'Ana Rodrigues',
        nota: 7.4
    }]
}, {
    nome: 'Turma M2',
    alunos: [{
        nome: 'Paulo',
        nota: 9
    }, {
        nome: 'Gabriel',
        nota: 3.3
    }]
    
}]
const getNotaDoAluno = aluno => aluno.nota
const getNotasDaTurma = turma => turma.alunos.map(getNotaDoAluno)

const notas1 = escola.map(getNotasDaTurma)
console.log(notas1) // Retorna uma matriz, dois arrays dentro de outro array.

console.log([].concat([ 8.3, 7.4 ], [ 9, 3.3 ] )) // Retorna um array com todas as notas.
// Construindo uma função pra concatenar automaticamente:

Array.prototype.flatMap = function(callback) {
    return Array.prototype.concat.apply([], this.map(callback))
}
const notas2 = escola.flatMap(getNotasDaTurma)
console.log(notas2)