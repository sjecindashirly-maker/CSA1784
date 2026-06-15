% Graph edges
edge(a,b).
edge(a,c).
edge(b,d).
edge(b,e).
edge(c,f).
edge(c,g).

% Heuristic values
h(a,6).
h(b,4).
h(c,3).
h(d,5).
h(e,2).
h(f,1).
h(g,0).

% Goal node
goal(g).

% Best First Search
bestfs(Node) :-
    goal(Node),
    write('Goal Reached: '), write(Node), nl.

bestfs(Node) :-
    edge(Node, Next),
    h(Next, _),
    write('Visiting: '), write(Next), nl,
    bestfs(Next).
