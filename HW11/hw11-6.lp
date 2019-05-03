% usage: clingo hw11-6.lp starwars-social-network.lp

% combine people and droids
character(P) :- person(P,_).
character(P) :- droid(P,_).

% determine how many people Character has spoken to
conversations(P,N) :- N = #count { Other : speaks_with(P,Other); Other: speaks_with(Other, P) }, character(P).

% find the character with the max
influential(N) :- N = #max { N : conversations(_,N) }, conversations(_,N).

% print nice
%#show conversations/2.
#show influential/1.

