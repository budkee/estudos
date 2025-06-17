% Definiciones
colores([negra, azul, verde, morada, roja]).
personas([austin, james, jason, stan, sterlin]).
edad_agentes([25, 30, 35, 40, 45]).
paises([australia, brasil, alemania, libia, rusia]).
accesorios([reloj, lapiz, telefono, anillo, paraguas]).
habilidades([hacking, disfraces, conduccion, artes_marciales, parkour]).

% Estructura: agente(Nombre, Posicion, Edad, Color, Pais, Accesorio, Habilidad)
solucion(Agentes) :-
    % Crear estructura vacía con variables libres
    Agentes = [
        agente(_, 1, _, _, _, _, _),
        agente(_, 2, _, _, _, _, _),
        agente(_, 3, _, _, _, _, _),
        agente(_, 4, _, _, _, _, _),
        agente(_, 5, _, _, _, _, _)
    ],

    % ---------------- Reglas más restrictivas primero ----------------
    % 4. James es el agente secreto más joven.
    member(agente(james, _, 25, _, _, _, _), Agentes),

    % 9. Sterling está en uno de los extremos.
    member(agente(sterlin, PosSterlin, _, _, _, _, _), Agentes),
    (PosSterlin = 1; PosSterlin = 5),
    
    % 10. El hombre de la corbata roja tiene 40 años.
    member(agente(_, _, 40, roja, _, _, _), Agentes),

    % 17. Austin tiene 30 años.
    member(agente(austin, _, 30, _, _, _, _), Agentes),
    
    % 20. En la segunda posición está el espía que lleva la corbata Verde.
    nth1(2, Agentes, agente(_, 2, _, verde, _, _, _)),      % Acessa o elemento de Agentes na segunda posição
    
    % ---------------- Otras reglas ----------------
    % 5. El agente que va a Australia está junto al agente especializado en parkour.
    al_lado_de_pais_habilidad(Agentes, australia, parkour),

    % 18. El agente que tiene un Teléfono especial está exactamente a la izquierda del agente que va a África (libia). 
    exactamente_a_la_izquierda_de_accesorio_pais(Agentes, telefono, libia),

    % 11. El espía que va a Sudamérica (brasil) está exactamente a la izquierda del espía de 45 años.
    exactamente_a_la_izquierda_de_pais_edad(Agentes, brasil, 45),
    
    % ---------------- Agente de 35 años ----------------
    % 3. El agente de 35 años va a una misión en Trípoli (libia).
    member(agente(_, _, 35, _, libia, _, _), Agentes),
    
    % 14. El agente de 35 años está al lado del agente que va a Sydney (australia).
    al_lado_de_pais_edad(Agentes, libia, australia),
    
    % 15. El agente con conocimientos avanzados de Hacking está exactamente a la izquierda del hombre de 35 años.
    exactamente_a_la_izquierda_de_habilidad_edad(Agentes, hacking, 35),

    % -------------- James ---------------
    % 6. James está exactamente a la derecha del agente que tiene un reloj especial.
    exactamente_a_la_derecha_de_accesorio_nombre(Agentes, reloj, james),

    % -------------- Stan ----------------
    % 8. Stan está junto al agente que va a Asia. 
    al_lado_de_nombre_pais(Agentes, stan, alemania),

    % -------------- Jason ---------------
    % 12. Jason está exactamente a la izquierda de Austin.
    exactamente_a_la_izquierda_de_nombre_nombre(Agentes, jason, austin),
    
    % -------------- Austin --------------
    % 1. Austin está junto al agente que lleva la corbata negra.
    al_lado_de_nombre_color(Agentes, austin, negra),

    % 13. El experto en conducción está junto al hombre de 30 años (Austin).
    al_lado_de_habilidad_edad(Agentes, conduccion, 30),

    % 21. El espía que va a Australia está exactamente a la derecha del espía de 30 años (Austin).
    exactamente_a_la_derecha_de_edad_pais(Agentes, 30, australia),
    
    % 7. El espía que tiene un paraguas único está entre el agente cuarentón y Austin, por ese orden.
    entre_edad_accesorio_nombre(Agentes, 40, paraguas, austin),

    % 2. El maestro del Disfraz (disfraces) está exactamente a la derecha del agente que tiene un paraguas espía.
    exactamente_a_la_derecha_de_accesorio_habilidad(Agentes, paraguas, disfraces),
    
    % -------------- Corbata Morada -------------
    % 16. El espía con corbata morada está al lado del espía friki (hacking).
    al_lado_de_color_habilidad(Agentes, morada, hacking),

    % 19. El agente que lleva un Anillo de espía está en algún lugar a la derecha del agente que lleva la corbata Morada.
    a_la_derecha_de_color_accesorio(Agentes, morada, anillo).
    
% Predicados auxiliares
al_lado_de_pais_edad(Agentes, Pais, Pais2) :-
    member(agente(_, Pos1, _, _, Pais, _, _), Agentes),
    member(agente(_, Pos2, _, _, Pais2, _, _), Agentes),
    abs(Pos1 - Pos2) =:= 1.

al_lado_de_pais_habilidad(Agentes, Pais, Habilidad) :-
    member(agente(_, Pos1, _, _, Pais, _, _), Agentes),
    member(agente(_, Pos2, _, _, _, _, Habilidad), Agentes),
    abs(Pos1 - Pos2) =:= 1.

exactamente_a_la_izquierda_de_habilidad_edad(Agentes, Habilidad, Edad) :-
    member(agente(_, Pos1, _, _, _, _, Habilidad), Agentes),
    member(agente(_, Pos2, Edad, _, _, _, _), Agentes),
    Pos1 is Pos2 - 1.

exactamente_a_la_izquierda_de_accesorio_pais(Agentes, Accesorio, Pais) :-
    member(agente(_, Pos1, _, _, _, Accesorio, _), Agentes),
    member(agente(_, Pos2, _, _, Pais, _, _), Agentes),
    Pos1 is Pos2 - 1.

exactamente_a_la_izquierda_de_pais_edad(Agentes, Pais, Edad) :-
    member(agente(_, Pos1, _, _, Pais, _, _), Agentes),
    member(agente(_, Pos2, Edad, _, _, _, _), Agentes),
    Pos1 is Pos2 - 1.

exactamente_a_la_derecha_de_accesorio_nombre(Agentes, Accesorio, Nombre) :-
    member(agente(_, Pos1, _, _, _, Accesorio, _), Agentes),
    member(agente(Nombre, Pos2, _, _, _, _, _), Agentes),
    Pos1 is Pos2 - 1.

al_lado_de_nombre_pais(Agentes, Nombre, Pais) :-
    member(agente(Nombre, Pos1, _, _, _, _, _), Agentes),
    member(agente(_, Pos2, _, _, Pais, _, _), Agentes),
    abs(Pos1 - Pos2) =:= 1.

exactamente_a_la_izquierda_de_nombre_nombre(Agentes, Nombre1, Nombre2) :-
    member(agente(Nombre1, Pos1, _, _, _, _, _), Agentes),
    member(agente(Nombre2, Pos2, _, _, _, _, _), Agentes),
    Pos1 is Pos2 - 1.

al_lado_de_nombre_color(Agentes, Nombre, Color) :-
    member(agente(Nombre, Pos1, _, _, _, _, _), Agentes),
    member(agente(_, Pos2, _, Color, _, _, _), Agentes),
    abs(Pos1 - Pos2) =:= 1.

al_lado_de_habilidad_edad(Agentes, Habilidad, Edad) :-
    member(agente(_, Pos1, _, _, _, _, Habilidad), Agentes),
    member(agente(_, Pos2, Edad, _, _, _, _), Agentes),
    abs(Pos1 - Pos2) =:= 1.

exactamente_a_la_derecha_de_edad_pais(Agentes, Edad, Pais) :-
    member(agente(_, Pos1, Edad, _, _, _, _), Agentes),
    member(agente(_, Pos2, _, _, Pais, _, _), Agentes),
    Pos1 is Pos2 + 1.

entre_edad_accesorio_nombre(Agentes, Edad, Accesorio, Nombre) :-
    member(agente(_, PosEdad, Edad, _, _, _, _), Agentes),
    member(agente(_, PosAcc, _, _, _, Accesorio, _), Agentes),
    member(agente(Nombre, PosNom, _, _, _, _, _), Agentes),
    PosAcc is PosEdad + 1,
    PosNom is PosAcc + 1.

exactamente_a_la_derecha_de_accesorio_habilidad(Agentes, Accesorio, Habilidad) :-
    member(agente(_, Pos1, _, _, _, Accesorio, _), Agentes),
    member(agente(_, Pos2, _, _, _, _, Habilidad), Agentes),
    Pos2 is Pos1 + 1.

al_lado_de_color_habilidad(Agentes, Color, Habilidad) :-
    member(agente(_, Pos1, _, Color, _, _, _), Agentes),
    member(agente(_, Pos2, _, _, _, _, Habilidad), Agentes),
    abs(Pos1 - Pos2) =:= 1.

a_la_derecha_de_color_accesorio(Agentes, Color, Accesorio) :-
    member(agente(_, Pos1, _, Color, _, _, _), Agentes),
    member(agente(_, Pos2, _, _, _, Accesorio, _), Agentes),
    Pos2 > Pos1.

% ¿Quién es el agente que tiene la habilidad de artes marciales?
resposta :-
    solucion(Agentes),
    member(agente(Nombre, _, _, _, _, _, artes_marciales), Agentes),
    format('El agente que tiene la habilidad de artes marciales es: ~w~n', [Nombre]).