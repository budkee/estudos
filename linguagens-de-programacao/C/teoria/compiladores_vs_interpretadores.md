## Compiladores vs. Interpretadores | C
>
> Ao executar um programa, o código escrito pode ser **compilado** ou **interpretado**.
>

### Linguagens Compiladas

> ![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white) ![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white) ![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) ![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![Objective-C](https://img.shields.io/badge/OBJECTIVE--C-%233A95E3.svg?style=for-the-badge&logo=apple&logoColor=white) 
> 
> Para as linguagens compiladas, o código percorre duas etapas antes de ser realmente executado: execução do compilador e execução do (código) nativo. 
>
> ![compilador](https://lh6.googleusercontent.com/80KkpsaGvzNzneQMQP7Uq4IOXYIgaWxUqRL2VxZFJGXEcTOeDc2B0h2eSgz1YZLSF17idTsNkcsv1tR00JFc1jtsoeoMXalSivfTF3f0wJo8AtQI4uGccaIsFFpFPmmQfVhyfF0U)
> 
> Nesta etapa de compilação, o código escrito em uma linguagem de alto nível é compilado para um arquivo em código binário (ou nativo) a nível de máquina (baixo nível).
>
> > Executando o compilador
>            
>    <span style= "color: purple">user@pc:~$</span> [gcc](https://blog.betrybe.com/tecnologia/compilador-o-que-e/#:~:text=dezembro%20de%202014.-,GCC,-GNU%20Compiler%20Collection) meu_programa.c
>
> > Executando o nativo
> 
>    <span style= "color: purple">user@pc:~$</span> ./a.out
> 
> #### Vantagens
> 
> - Menor tempo de execução
> - Maior confiabilidade do código final
>
> #### Desvantagens
>
> - Caso tenha que fazer uma alteração, será necessário recompilar todo o código
> 

### Linguagens Interpretadas
>
> ![PHP](https://img.shields.io/badge/php-%23777BB4.svg?style=for-the-badge&logo=php&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Ruby](https://img.shields.io/badge/ruby-%23CC342D.svg?style=for-the-badge&logo=ruby&logoColor=white) ![Perl](https://img.shields.io/badge/perl-%2339457E.svg?style=for-the-badge&logo=perl&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![C#](https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=c-sharp&logoColor=white)
> 
> Em contrapartida, aquelas linguagens que são interpretadas, como o [Python](../Python/resumo.md), percorre apenas uma etapa: execução do código de alto nível linha por linha.
>
> ![interpretadores](https://media.geeksforgeeks.org/wp-content/uploads/20200530152827/223-1.png)
>
> #### Vantagens
>
> - Fáceis de utilizar
> - Execução do código linha por linha
> - Melhor uso da memória, uma vez que não há intermediários pelo caminho
>
> #### Desvantagens
>
> - Maior tempo de execução
> - Menor confiabilidade
> - É necessário ter o programa do interpretador para ser executado
>
> 