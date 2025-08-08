function regimeDeCapitalizacaoComposto (c, i, n) {
    j = c * ((1+i)**n - 1)
    MontCap = c * ((1+i)**n)
    return MontCap
}

console.log(regimeDeCapitalizacaoComposto(1000, 0.1, 4))