// Bug do JavaScript
const funcs = [] // Array

// Função de Incremento
for (var i = 0; i< 10 ; i++) {
  // Preenchimento do array pelo método .push utilizando uma função anônima sem parâmetro de entrada.
  funcs.push (function() {
    console.log(i)
    
  })
}

funcs[2]() // i = 10
funcs[8]() // i = 10

// Como var nao tem escopo de função, ele 
