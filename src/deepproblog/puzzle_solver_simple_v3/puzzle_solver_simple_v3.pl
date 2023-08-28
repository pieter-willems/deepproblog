nn(colour_net,[X],Y,[red,yellow,green,cyan,blue,magenta]) :: colour(X,Y).


same([[A,B],[A,B]]).
same([[A,A],[A,A]]).
same([[A,A],[B,B]]).
shifted([[A,B],[B,A]]).

puzzle(Rows) :- same(Rows).
puzzle(Rows) :- shifted(Rows).

solution(Tl,Tr,Bl,C) :-  colour(Tl,Tl3), colour(Tr,Tr3), colour(Bl,Bl3), puzzle([[Tl3,Tr3],[Bl3,C]]).
