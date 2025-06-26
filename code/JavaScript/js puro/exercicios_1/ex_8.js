/**
 * Pedro joga N jogos de basquete por temporada. Para saber como está ele está progredindo, ele mantém registro de todos os as pontuações feitas por jogo. Após cada jogo ele anota no novo valor e confere se o mesmo é maior ou menor que seu melhor e pior desempenho. Dada uma lista string = “pontuação1 pontuação2 pontuação3 etc..”, escreva uma função que ao recebê-la irá comparar os valores um a um e irá retornar um vetor com o número de vezes que ele bateu seu recorde de maior número de pontos e quando fez seu pior jogo (Número do pior jogo). 
 * 
 * Obs.: O primeiro jogo não conta como novo recorde do melhor.  
 * Exemplo:  
 * String: “10 20 20 8 25 3 0 30 1” 
 * Retorno: [3, 7] (Significa que ele bateu três vezes seu recorde de melhor pontuação e a pior pontuação aconteceu no sétimo jogo.)
 * Lista da pontuação dos jogos e retorna um vetor com quantas vezes ela bateu seu recorde de pontos e o pior jogo da temporada.
 * @date 22/03/2024 - 12:03:26
 *
 * @type {string}
 */

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




