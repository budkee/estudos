var numero = 1  // Variável global
{
  var numero = 2  // Variável global também.
  console.log('dentro =', numero)
}
console.log('fora =', numero)

// As variáveis estão no mesmo escopo.
// O var é visivel dentro e fora do escopo do bloco, ele não tem escopo de bloco.