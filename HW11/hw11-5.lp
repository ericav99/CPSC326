% usage: clingo hw11-5.lp starwars-social-network.lp

% determine characters that have appeared in all movies
all_movies(C) :- appears_in(C,episode1), appears_in(C,episode2), appears_in(C,episode3), appears_in(C,episode4), appears_in(C,episode5), appears_in(C,episode6), appears_in(C,episode7).

% print nice
#show all_movies/1.
