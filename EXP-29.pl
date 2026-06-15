% Facts
fact(sunny).
fact(warm).

% Forward Chaining Rules
go_beach :-
    fact(sunny),
    fact(warm).

play_cricket :-
    fact(sunny).
