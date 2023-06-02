nn(puzzle_net,[X],Y,[triangle,circle,hexagon,pentagon,square,right_triangle,trapeze,rhombus,kite]) :: shape(X,Y).

% same([]).   % You only need this one if you want the empty list to succeed
% same([_]).
% same([X,X|T]) :- same([X|T]).

same([[A,B],[A,B]]).
same([[A,A],[A,A]]).
shifted([[A,B],[B,A]]).

puzzle(Rows) :- same(Rows).
puzzle(Rows) :- shifted(Rows).

solution(Tl,Tr,Bl,S) :- shape(Tl,Tl2), shape(Tr,Tr2), shape(Bl,Bl2), puzzle([[Tl2,Tr2],[Bl2,S]]).
