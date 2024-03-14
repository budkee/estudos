// Formatação de números

function formatacao(valor) {
    const formatado = valor.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
    return formatado;
}

console.log(formatacao(0.1+0.2))
