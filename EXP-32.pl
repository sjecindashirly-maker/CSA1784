% Pattern Matching Example

greet(hello).
greet(hi).
greet(welcome).

check(X) :-
    greet(X),
    write(X), write(' matched successfully.').

check(X) :-
    write(X), write(' does not match any pattern.').
