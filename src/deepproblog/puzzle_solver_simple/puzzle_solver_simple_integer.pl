nn(puzzle_net,[X],Y,[0,1,2,3,4,5,6,7,8])::shape(X,Y).

same([]).   % You only need this one if you want the empty list to succeed
same([_]).
same([X,X|T]) :- same([X|T]).

shifted([[A,B],[B,A]]).

shapename_int(triangle,0).
shapename_int(circle,1).
shapename_int(hexagon,2).
shapename_int(pentagon,3).
shapename_int(square,4).
shapename_int(right_triangle,5).
shapename_int(trapeze,6).
shapename_int(rhombus,7).
shapename_int(kite,8).

puzzle(Rows):-same(Rows).
puzzle(Rows):- shifted(Rows).

solution(Tl,Tr,Bl,S) :- shape(Tl,Tl2),shape(Tr,Tr2),shape(Bl,Bl2), puzzle([[Tl2,Tr2],[Bl2,X]]), S is Y.