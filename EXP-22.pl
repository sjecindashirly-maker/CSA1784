% Facts
bird(sparrow).
bird(eagle).
bird(parrot).
bird(penguin).
bird(ostrich).

% Birds that cannot fly
cannot_fly(penguin).
cannot_fly(ostrich).

% Rule
can_fly(X) :-
    bird(X),
    \+ cannot_fly(X).
