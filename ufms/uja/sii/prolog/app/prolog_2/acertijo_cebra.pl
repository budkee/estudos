% Definiciones
nacionalidad([noruego, ingles, espanol, ucraniano, japones]).
color([rojo, verde, amarillo, azul, marfil]).
mascota([perro, cebra, caracoles, zorro, caballo]).
bebida([agua, cafe, leche, te, jugo_naranja]).
cigarro([chesterfield, kools, lucky_strike, parliament, old_gold]).

% Estructura: casa(Nacionalidad, Color, Mascota, Bebida, Cigarillo).
solucion(Casas):-
    % Inicializa estructura de casas con variables libres
    Casas = [C1, C2, C3, C4, C5],

    % Cada casa es: casa(Nacionalidad, Color, Mascota, Bebida, Cigarro)
    C1 = casa(_, _, _, _, _),
    C2 = casa(_, _, _, _, _),
    C3 = casa(_, _, _, _, _),
    C4 = casa(_, _, _, _, _),
    C5 = casa(_, _, _, _, _),

    % Reglas más restrictivas primero
    % P10: El noruego vive en la primera casa
    C1 = casa(noruego, _, _, _, _),

    % P9: El hombre que vive en la casa del centro bebe leche
    C3 = casa(_, _, _, leche, _),

    % P2: El inglés vive en la casa roja
    member(casa(ingles, rojo, _, _, _), Casas),

    % P3: El español tiene un perro
    member(casa(espanol, _, perro, _, _), Casas),

    % P4: En la casa verde se bebe café
    member(casa(_, verde, _, cafe, _), Casas),

    % P5: El ucraniano bebe té
    member(casa(ucraniano, _, _, te, _), Casas),

    % P6: La casa verde está justo a la derecha de la marfil
    nextto(casa(_, marfil, _, _, _), casa(_, verde, _, _, _), Casas),

    % P7: El que fuma Old Gold tiene caracoles
    member(casa(_, _, caracoles, _, old_gold), Casas),

    % P8: En la casa amarilla se fuman Kools
    member(casa(_, amarillo, _, _, kools), Casas),

    % P11: El que fuma Chesterfield vive al lado del dueño del zorro
    al_lado(casa(_, _, _, _, chesterfield), casa(_, _, zorro, _, _), Casas),

    % P12: El que fuma Kools vive al lado del dueño del caballo
    al_lado(casa(_, _, _, _, kools), casa(_, _, caballo, _, _), Casas),

    % P13: El que fuma Lucky Strike bebe jugo de naranja
    member(casa(_, _, _, jugo_naranja, lucky_strike), Casas),

    % P14: El japonés fuma Parliament
    member(casa(japones, _, _, _, parliament), Casas),

    % P15: El noruego vive al lado de la casa azul
    al_lado(casa(noruego, _, _, _, _), casa(_, azul, _, _, _), Casas).

% Predicado auxiliar: "X está al lado de Y en la lista"
al_lado(X, Y, Lista) :- nextto(X, Y, Lista) ; nextto(Y, X, Lista).

% Respostas
quem_tem_cebra(Nome) :-
    solucion(Casas),
    member(casa(Nome, _, zebra, _, _), Casas).

quem_bebe_agua(Nome) :-
    solucion(Casas),
    member(casa(Nome, _, _, agua, _), Casas).

resposta :-
    quem_tem_cebra(Cebra),
    quem_bebe_agua(Agua),
    format('Quien tiene la cebra: ~w~n', [Cebra]),
    format('Quien bebe água: ~w~n', [Agua]).

% Ejemplo de uso:
% ?- resposta.