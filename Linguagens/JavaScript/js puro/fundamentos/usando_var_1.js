// Utilizando variáveis: Globais e Locais
{
    {

        {

            {
                var sera = 'Será??'
                console.log(sera)
            }
        }
    }
}

console.log(sera)
// a variável é visivel dentro e fora do bloco

// -------------------------------------------------------

function teste() {
    var local = 123
    console.log(local)
} // Bloco associado a uma função

// executando | retornando a função
teste()

console.log(local) 
// Não é uma variável global, e, portanto, não será apresentada no console. -> [ReferenceError]

// Variáveis globais
// Ficam muito "dadas" pra qualquer pessoa, elas são visíveis em toda a sua aplicação.

// Variáveis locais
// Ficam mais reservadas, elas são visiveis apenas no escopo das suas respectivas funções.