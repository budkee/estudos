% Declaración de Mujer
mujerCis(joana).
mujerCis(leticia).
mujerTrans(luana).
mujerTrans(lazuli).
mujer(X):- mujerTrans(X); mujerCis(X).

% Declaración de Hombre
hombreTrans(joao).
hombreTrans(otavio).
hombreTrans(roberto).
hombreCis(pedro).
hombreCis(caio).
hombreCis(alejandro).
hombre(X):- hombreTrans(X); hombreCis(X).

% Declaración de No Binario
noBinario(joao).
noBinario(otavio).
noBinario(lazuli).
noBinario(caio).

% Estado de vida 
vive(joana).
vive(luana).
vive(joao).
vive(pedro).
vive(otavio).
vive(leticia).
vive(roberto).
vive(lazuli).
vive(caio).

% Edad
edad(joana, 97).
edad(luana, 99).
edad(joao, 93).
edad(pedro, 60).
edad(otavio, 50).
edad(roberto, 32).
edad(lazuli, 30).
edad(caio, 24).
edad(alejandro, 15).
mayorDeEdad(X) :- vive(X), edad(X, E), E >= 18.

% Parejas
pareja(joana, luana).
pareja(pedro, otavio).
pareja(roberto, lazuli).

% Progenitores | Gestante
progenitorGestante(joana, pedro).
progenitorGestante(otavio, lazuli).
progenitorGestante(roberto, caio).
progenitorGestante(roberto, alejandro).

% Progenitores | No Gestante
progenitorNoGestante(luana, pedro).
progenitorNoGestante(pedro, lazuli).
progenitorNoGestante(lazuli, caio).
progenitorNoGestante(lazuli, alejandro).

% Determinación de progenitor gestante o no gestante
progenitorGestante(X) :- mujerCis(X); hombreTrans(X); (noBinario(X), not(hombreCis(X))).
progenitorNoGestante(X) :- hombreCis(X); mujerTrans(X); (noBinario(X), not(mujerCis(X))).

% ¿Hay progenitor?
progenitor(X,Y):- progenitorGestante(X,Y); progenitorNoGestante(X,Y).
tieneDescendente(X):- progenitor(X,_).

% Relación de (a/de)scendencia
descendienteDe(Y, X) :- progenitor(X, Y).
ascendienteDe(X, Y) :- descendienteDe(Y, X).

% Núcleo familiar
adre(X):- hombreTrans(X); mujerTrans(X); noBinario(X).
madre(X,Y):- progenitorGestante(X,Y), mujerCis(X); mujerTrans(X).
padre(X,Y):- progenitorNoGestante(X,Y), hombreCis(X); hombreTrans(X).
hermane(X,Y):- progenitor(Z,X), progenitor(Z,Y), X\=Y.
hije(X, Y) :- descendienteDe(X, Y).
abuele(X, Y) :- progenitor(X, Z), progenitor(Z, Y).
bisabuele(X, Y) :- progenitor(X, Z), abuele(Z, Y).


% Consultas ejemplo
% ?- mayorDeEdad(joao).
% ?- adre(lazuli).
% ?- descendienteDe(joao, X).
% ?- ascendienteDe(lazuli, Y).
% ?- hermane(X, caio).
% ?- abuele(joana, Y).
% ?- bisabuele(joao, Y).