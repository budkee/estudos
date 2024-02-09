const aprovados = [ 'Agata', 'Julia', 'Ricardo', 'Rodrigo']
// Exibir o índice e o nome:
aprovados.forEach(
    function(nome,indice, array) {
        console.log(`${indice + 1}) ${nome}`)
    }
)
// Apenas os nomes
aprovados.forEach(nome => console.log(nome))
// Outra forma...
const exibirAprovados = aprovado => console.log(aprovado)
aprovados.forEach(exibirAprovados)