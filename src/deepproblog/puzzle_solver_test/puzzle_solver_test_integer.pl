nn(puzzle_net,[X],Y,[0,1,2,3,4,5,6,7,8])::shape(X,Y).

shapename_int(triangle,0).
shapename_int(circle,1).
shapename_int(hexagon,2).
shapename_int(pentagon,3).
shapename_int(square,4).
shapename_int(right_triangle,5).
shapename_int(trapeze,6).
shapename_int(rhombus,7).
shapename_int(kite,8).

is_equal(A,A).

solution(TL,S) :- shape(TL,Y), shapename_int(S,Y).