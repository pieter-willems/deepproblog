nn(puzzle_net,[X],Y,[triangle,circle,hexagon,pentagon,square,right_triangle,trapeze,rhombus,kite])::shape(X,Y).

same([]).   % You only need this one if you want the empty list to succeed
same([_]).
same([X,X|T]) :- same([X|T]).

shifted_right([[A,B,C],[C,A,B],[B,C,A]]).
shifted_left([[A,B,C],[B,C,A],[C,A,B]]).

are_equal(A,B,C) :- shape(A, A2), shape(B, B2), shape(C, C2), equal(A2,B2,C2).
are_equal2(A,B,S) :- shape(A, A2), shape(B, B2), S, equal(A2,B2,S).
equal(A,A,A).
puzzle(Rows):-same(Rows).

puzzle(Rows):-shifted_right(Rows).

puzzle(Rows):-shifted_left(Rows).


%solution(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S):- shape(Tl,Tl2),shape(Tm,Tm2),shape(Tr,Tr2),
%                                      shape(Ml,Ml2),shape(Mm,Mm2),shape(Mr,Mr2),
%                                      shape(Bl,Bl2),shape(Bm,Bm2),
%                                      puzzle([[Tl2,Tm2,Tr2],[Ml2,Mm2,Mr2],[Bl2,Bm2,S]]).

solution(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- are_equal(Tl, Mr, Bm),
                                       are_equal(Tr, Mm, Bl),
                                       are_equal2(Tm, Ml, S).
                                       %are_equal(shape(Tr, Tr2), shape(Mm, Mm2), shape(Bl, Bl2)),
                                       %shape(Ml,Ml2), shape(Mm,Mm2), shape(Mr,Mr2),
                                       %shape(Bl,Bl2), shape(Bm,Bm2),
                                       %shape(Tl, Y), Y = S.
