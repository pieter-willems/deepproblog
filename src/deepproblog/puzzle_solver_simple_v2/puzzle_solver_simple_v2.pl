nn(puzzle_net,[X],Y,[triangle,circle,hexagon,pentagon,square,right_triangle,trapeze,rhombus,kite]) :: shape(X,Y).
nn(colour_net,[X],Y,[red,yellow,green,cyan,blue,magenta]) :: colour(X,Y).


same([[A,B],[A,B]]).
same([[A,A],[A,A]]).
shifted([[A,B],[B,A]]).

puzzle(Rows) :- same(Rows).
puzzle(Rows) :- shifted(Rows).

% solution(Tl,Tr,Bl,S,C) :- shape(Tl,Tl2), shape(Tr,Tr2), shape(Bl,Bl2), puzzle([[Tl2,Tr2],[Bl2,S]]),
%                            colour(Tl,Tl3), colour(Tr,Tr3), colour(Bl,Bl3), same([[Tl3,Tr3],[Bl3,C]]),
%                            shifted([[Tl3,Tr3],[Bl3,C]]).

% solution(Tl,Tr,Bl,S,C):- shape(Tl,Tl2), shape(Tr,Tr2), shape(Bl,Bl2), same([[Tl2,Tr2],[Bl2,S]]), colour(Tl,Tl3),
%                            colour(Tr,Tr3), colour(Bl,Bl3), same([[Tl3,Tr3],[Bl3,C]]).

%solution(Tl,Tr,Bl,S,C):- shape(Tl,Tl2), shape(Tr,Tr2), shape(Bl,Bl2), shifted([[Tl2,Tr2],[Bl2,S]]), colour(Tl,Tl3),
%                            colour(Tr,Tr3), colour(Bl,Bl3), same([[Tl3,Tr3],[Bl3,C]]).

%solution(Tl,Tr,Bl,S,C):- shape(Tl,Tl2), shape(Tr,Tr2), shape(Bl,Bl2), same([[Tl2,Tr2],[Bl2,S]]), colour(Tl,Tl3),
%                            colour(Tr,Tr3), colour(Bl,Bl3), shifted([[Tl3,Tr3],[Bl3,C]]).

%solution(Tl,Tr,Bl,S,C):- shape(Tl,Tl2), shape(Tr,Tr2), shape(Bl,Bl2), shifted([[Tl2,Tr2],[Bl2,S]]), colour(Tl,Tl3),
%                            colour(Tr,Tr3), colour(Bl,Bl3), shifted([[Tl3,Tr3],[Bl3,C]]).

%solution(Tl,Tr,Bl,S,C):- shape(Tl,Tl2), shape(Tr,Tr2), shape(Bl,Bl2), puzzle([[Tl2,Tr2],[Bl2,S]]), colour(Tl,Tl3), colour(Tr,Tr3), colour(Bl,Bl3), puzzle([[Tl3,Tr3],[Bl3,C]]).
solution(Tl,Tr,Bl,S,C) :- sol_col(Tl,Tr,Bl,C), sol_shape(Tl,Tr,Bl,S).

sol_col(Tl,Tr,Bl,C) :- colour(Tl,Tl2), colour(Tr,Tr2), colour(Bl,Bl2), puzzle([[Tl2,Tr2],[Bl2,C]]).

sol_shape(Tl,Tr,Bl,S) :- shape(Tl,Tl2), shape(Tr,Tr2), shape(Bl,Bl2), puzzle([[Tl2,Tr2],[Bl2,S]]).