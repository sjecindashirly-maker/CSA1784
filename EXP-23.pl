% Facts

male(john).
male(robert).
male(david).

female(mary).
female(linda).
female(susan).

parent(john, robert).
parent(mary, robert).

parent(john, linda).
parent(mary, linda).

parent(robert, david).
parent(susan, david).

% Rules

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

brother(X, Y) :-
    male(X),
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

sister(X, Y) :-
    female(X),
    parent(Z, X),
    parent(Z, Y),
    X \= Y.
