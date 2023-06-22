nn(puzzle_net,[X],Y,[triangle,circle,hexagon,pentagon,square,right_triangle,trapeze,rhombus,kite])::shape(X,Y).

same([]).   % You only need this one if you want the empty list to succeed
same([_]).
same([X,X|T]) :- same([X|T]).

shifted_right([[A,B,C],[C,A,B],[B,C,A]]).
shifted_left([[A,B,C],[B,C,A],[C,A,B]]).

are_equal(A,B,C) :- row(A,B,C,A2,B2,C2), same([A2,B2,C2]).
are_equal2(A,B,S) :- bottomrow(A,B,A2,B2),same([A2,B2,S]).
equal(A,A,A).

%puzzle(Rows):-same(Rows).

%puzzle(Rows):-shifted_right(Rows).

%puzzle(Rows):-shifted_left(Rows).

row(A,B,C,X,Y,Z):- shape(A,X),shape(B,Y),shape(C,Z).
bottomrow(A,B,X,Y):-shape(A,X),shape(B,Y).

%in case the shapes are shifted to the left
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- are_equal(Tl, Mr, Bm),
                                     are_equal(Tr, Mm, Bl),
                                     are_equal2(Tm, Ml, S).

% in case that the shapes are shifted to the right
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :-   are_equal(Tm,Mr,Bl),
                                       are_equal(Tr,Ml,Bm),
                                       are_equal2(Tl,Mm,S).

%in case all of the rows are the same
%puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :-   are_equal(Tl,Tm,Tr),
%                                       are_equal(Ml,Mm,Mr),
%                                       are_equal2(Bl,Bm,S).

%in case all the column are the same
%puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :-   are_equal(Tl,Ml,Bl),
%                                       are_equal(Tm,Mm,Bm),
%                                       are_equal2(Tr,Mr,S).



%solution(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S):- shape(Tl,Tl2),shape(Tm,Tm2),shape(Tr,Tr2),
%                                      shape(Ml,Ml2),shape(Mm,Mm2),shape(Mr,Mr2),
%                                      shape(Bl,Bl2),shape(Bm,Bm2),
%                                      puzzle([[Tl2,Tm2,Tr2],[Ml2,Mm2,Mr2],[Bl2,Bm2,S]]).

%solution(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- are_equal(Tl, Mr, Bm),
%                                       are_equal(Tr, Mm, Bl),
%                                       are_equal2(Tm, Ml, S).
                                       %are_equal(shape(Tr, Tr2), shape(Mm, Mm2), shape(Bl, Bl2)),
                                       %shape(Ml,Ml2), shape(Mm,Mm2), shape(Mr,Mr2),
                                       %shape(Bl,Bl2), shape(Bm,Bm2),
                                       %shape(Tl, Y), Y = S.

solution(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S).

%antineural(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,Tl2,Tm2,Tr2,Ml2,Mm2,Mr2,Bl2,Bm2):- row(Tl,Tm,Tr,Tl2,Tm2,Tr2),row(Ml,Mm,Mr,Ml2,Mm2,Mr2),bottomrow(Bl,Bm,Bl2,Bm2).

%solution(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S):- row(Tl,Tm,Tr,Tl2,Tm2,Tr2),row(Ml,Mm,Mr,Ml2,Mm2,Mr2),
%                                      Tm2=S.
