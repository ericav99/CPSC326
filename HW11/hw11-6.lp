% usage: clingo hw11-6.lp starwars-social-network.lp

% combine people and droids
character(P) :- person(P,_).
character(P) :- droid(P,_).

% determine how many people Character has spoken to
conversations(C,N) :- N = #count { Other : speaks_with(C,Other); Other: speaks_with(Other, C) }, character(C).

% find the character with the max
influential(C) :- C = #max { N : conversations(C,N) }, character(C).

% print nice
%#show conversations/2.
#show influential/1.

