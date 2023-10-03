// Resolução de Bháskara

// Parâmetros: a, b e c.
// Ações: calcular e retornar o delta em forma de vetor; caso delta seja negativo retorne 'Delta é negativo'.

function bhaskara(a, b, c) {
    
    let delta = ((b)**2 -(4 * a * c))**1/2
    let resultado1 = (- b + delta)/ 2*a
    let resultado2 = (- b - delta)/ 2*a
    
    if (delta < 0) {
        
        return 'Delta é negativo'

    } else {
        
        return [resultado1, resultado2]
    }
    
    

}

console.log(bhaskara(3, -5, 12))
