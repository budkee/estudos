// Lista da pontuação dos jogos e retorno de um vetor com quantas vezes ela bateu seu recorde de pontos e o pior jogo da temporada.
let string = "10, 20, 20, 8, 25, 3, 0, 30, 1"

// 1. Separar os elementos da string
function separadorDeString(stringASerSeparada, separador) {
    var arrayDaString = stringASerSeparada.split(separador);
    return console.log(arrayDaString)
    //console.log('A string original é: "' + stringASerSeparada + '"');
    //console.log('O separador é: "' + separador + '"');
    //console.log('O array tem ' + arrayDaString.length + ' elementos: ' + arrayDaString.join(' / '));
}
  
var comma = ',';
const pontuacoes = separadorDeString(string, comma);

// 2. 

