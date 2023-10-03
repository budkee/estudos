# Eficiência Algorítmica

## Sumário

- [O que é eficiência algorítmica?](#)
- [](#)
- [](#)
- [Links e Referências](#links-e-referências)

## O que é eficiência algorítmica?

É uma forma de calcular e analisar o quão eficiente é um determinado algoritmo de acordo com o número máximo de repetições necessárias para execução e o tamanho do array. Assim, o número máximo de tentativas necessárias para uma busca linear e uma busca binária aumenta conforme aumenta o tamanho do array de candidatos.

## Notação Assintótica

A notação assintótica é utilizada para avaliar o **tempo de execução** de um código. Nesta análise, o tempo de execução vai depender, entre outros fatores, da velocidade de processamento do computador, da linguagem de programação e do compilador utilizado para execução. Dessa forma, num primeiro instante, pensamos no tempo de execução de um algoritmo como a função do tamanho de seu input (número de elementos do array). Em segunda instância, podemos analisar através de gráficos, o quão rápido uma função cresce com o tamanho da entrada, representado pela **taxa de crescimento** do tempo de execução. Quando descartamos os coeficientes constantes e os termos menos significativos, usamos notação assintótica. Vamos estudar suas três formas: notação Big-Θ(Theta), notação Big-O e notação Ω(Ômega).

- [Notação Big-Θ | Khan Academy](https://pt.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/big-big-theta-notation): Quando usamos a notação big-Θ estamos dizendo que temos um limite assintoticamente restrito no tempo de execução. "Assintoticamente" porque ele importa apenas para valores grandes de `n`. "Limite restrito" porque definimos o tempo de execução para um fator constante **superior e inferior**, como na imagem a seguir:

    ![big-theta](https://cdn.kastatic.org/ka-perseus-images/c14a48f24cae3fd563cb3627ee2a74f56c0bcef6.png)
- [Notação Big-O | Khan Academy](https://pt.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/big-o-notation): Seria conveniente ter uma forma de notação assintótica que diga "o tempo de execução cresce no máximo até um determinado valor, mas poderia crescer mais devagar". A notação "big-O" serve para essas ocasiões, fornencendo **apenas o limite superior** do tempo de execução.

    ![big-o](https://cdn.kastatic.org/ka-perseus-images/501211c02f4c6765f60f23842450e1151cfd9c89.png)
- [Notação Big-Ω | Khan Academy](): Algumas vezes, queremos dizer que um algoritmo leva ao menos uma certa quantidade de tempo, sem fornecer um limite superior. Usamos a notação Ω, que é a letra grega "omega" maiúscula. Assim, a notação Ω é utilizada para **limites assintóticos inferiores**, uma vez que delimita de modo otimista o aumento do tempo de execução para entradas suficientemente extensas.

### Complexidade Assintótica

A complexidade assintótica descreve como o desempenho de um algoritmo se comporta quando a entrada se torna muito grande, ignorando os detalhes específicos da implementação (como as constantes e outros termos de ordem inferior da função) e se concentrando apenas na tendência geral (taxa de crescimento).

### Funções por Ordem de crescimento
- Funções constantes
- Funções logarítmicas
- Funções lineares
- Funções linearítmicas
- Funções polinomiais
- Funções exponenciais
- Funções fatoriais


## Exercícios

- [Algorítmo para verificar se existem elementos repetidos](vetor_elemento-repetido.c)

## Links e Referências

- [Vídeo-aula](https://www.youtube.com/playlist?list=PL5_KtwXMxt5nAcfuOHvlUI2eUNPRLT4XQ)
- [Comparando funções algorítmicas](https://www.desmos.com/calculator/x50y6keodu?lang=pt-BR)
- [Notação Assintótica | Khan Academy](https://pt.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/asymptotic-notation)
- [Análise de Algorítmos | GeeksForGeeks](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/)
