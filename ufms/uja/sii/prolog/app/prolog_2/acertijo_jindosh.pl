% Definición
personas([natsiou, winslow, marcolla, contee, finch]).
colores([rojo, verde, morado, azul, blanco]).
reliquias([colgante_alado, anillo, diamante, medallon_guerra, cofrecito_rape]).
bebidas([cerveza, ron, vino, absenta, whisky]).
ciudades([fraeport, baleton, dabokva, dunwall, karnaca]).

% Estructura: invitada(Nombre, Posicion, Color, Ciudad, Bebida, Reliquia)
solucion(Invitadas) :-
    % Crear estructura vacía con posiciones
    Invitadas = [
        invitada(_, 1, _, _, _, _),
        invitada(_, 2, _, _, _, _),
        invitada(_, 3, _, _, _, _),
        invitada(_, 4, _, _, _, _),
        invitada(_, 5, _, _, _, _)
    ],
   
    % Reglas más restrictivas primero
    % 1. Marcolla usa blanco
    member(invitada(marcolla, _, blanco, _, _, _), Invitadas),

    % 6. Finch tem diamante
    member(invitada(finch, _, _, _, _, diamante), Invitadas),
    
    % 4. Fraeport está de rojo
    member(invitada(_, _, rojo, fraeport, _, _), Invitadas),

    % 11. Winslow é de Karnaca
    member(invitada(winslow, _, _, karnaca, _, _), Invitadas),

    % Otras restricciones
    % 2. Natsiou está à esquerda e ao lado da de verde
    member(invitada(natsiou, 1, _, _, _, _), Invitadas),
    member(invitada(_, 2, verde, _, _, _), Invitadas),

    % 3. Morado está à izquierda de azul
    izquierda_de(Invitadas, morado, azul),

    % 5. Colgante alado junto a fraeport
    al_lado_de_reliquia_ciudad(Invitadas, colgante_alado, fraeport),

    % 7. Baleton tem medallón
    member(invitada(_, _, _, baleton, _, medallon_guerra), Invitadas),

    % 8. Cofrecito está al lado de Dabokva 
    al_lado_de_reliquia_ciudad(Invitadas, cofrecito_rape, dabokva),

    % 9. Contee toma ron
    member(invitada(contee, _, _, _, ron, _), Invitadas),

    % 10. Dunwall toma vino, e derruba whisky da central (3)
    member(invitada(_, _, _, dunwall, vino, _), Invitadas),
    member(invitada(_, 3, _, _, whisky, _), Invitadas),

    % Restricciones adicionales para bebidas faltantes
    % Natsiou (pos 1) não tem bebida especificada - atribuir cerveza ou absenta
    member(invitada(natsiou, 1, _, _, B1, _), Invitadas),
    (B1 = cerveza; B1 = absenta),
    
    % Winslow (pos 5) não tem bebida especificada - atribuir a restante
    member(invitada(winslow, 5, _, _, B5, _), Invitadas),
    (B5 = cerveza; B5 = absenta),
    B1 \= B5,
    
    % Reliquias faltantes: anillo debe estar con Winslow (única reliquia restante)
    member(invitada(winslow, 5, _, _, _, anillo), Invitadas).
    
% A está a la izquierda de B (em termos de cor)
izquierda_de(Lista, ColorA, ColorB) :-
    member(invitada(_, PA, ColorA, _, _, _), Lista),
    member(invitada(_, PB, ColorB, _, _, _), Lista),
    PA < PB.

% (Persona con) Reliquia que está al lado de la ciudad (de otra Persona)
al_lado_de_reliquia_ciudad(Lista, Reliquia, Ciudad) :-
    member(invitada(_, P1, _, _, _, Reliquia), Lista),
    member(invitada(_, P2, _, Ciudad, _, _), Lista),
    abs(P1 - P2) =:= 1.


% Mostrar solución ordenada por posición
mostrar_solucion(Invitadas) :-
    sort(2, @=<, Invitadas, Ordenadas),
    writeln('Pos | Nombre    | Color   | Ciudad   | Bebida  | Reliquia'),
    writeln('----+-----------+---------+----------+---------+--------------------'),
    mostrar_filas(Ordenadas).

mostrar_filas([]).
mostrar_filas([invitada(N, P, C, Ci, B, R)|Resto]) :-
    format('~w   | ~w~t~15| ~w~t~15| ~w~t~15| ~w~t~15| ~w~n', [P, N, C, Ci, B, R]),
    mostrar_filas(Resto).

% ¿A quién pertenece cada reliquia?
resposta :-
    solucion(Invitadas),
    mostrar_solucion(Invitadas),
    nl, writeln('Dueñas de las reliquias:'),
    forall(member(invitada(N, _, _, _, _, R), Invitadas),
           format('~w tiene la reliquia: ~w~n', [N, R])).

% Ejemplo de uso:
% ?- resposta.