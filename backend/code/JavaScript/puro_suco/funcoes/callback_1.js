const fabricantes = ['Mercedes', 'Audi', 'BMW'];

function imprimir(nome, indice) {
    console.log(`${indice + 1} . ${nome}`)
}
console.log('Lista dos fabricantes:')
fabricantes.forEach(imprimir) // A função .forEach vai primeiro pegar o parâmetro valor, depois o parâmetro índice. 

console.log('\nFabricantes:')
fabricantes.forEach(fabricante => console.log(fabricante))
