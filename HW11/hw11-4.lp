% usage: clingo hw11-4.lp starwars-social-network.lp

% determine people in the same generation
% the last two parts to each rule are:
% - someone cannot be siblings with themselves
% - removing duplicates like (luke,leia) / (leia,luke)

% rule 1: siblings are in the same generation
same_gen(C1,C2) :- child_of(C1,P), child_of(C2,P), C1 != C2, not same_gen(C2,C1).

% rule 2: parents are in the same generation
same_gen(P1,P2) :- child_of(C,P1), child_of(C,P2), P1 != P2, not same_gen(P2,P1).

% rule 3: parents of children in the same generation are in the same generation (ex. in-laws)
same_gen(P1,P2) :- child_of(C1,P1), child_of(C2,P2), same_gen(C1,C2), C1 != C2, P1 != P2, not same_gen(P2,P1).

% rule 4: children of parents in the same generation are in the same generation (ex. cousins)
same_gen(C1,C2) :- child_of(C1,P1), child_of(C2,P2), same_gen(P1,P2), P1 != P2, C1 != C2, not same_gen(C2,C1).

% print nice
#show same_gen/2.
