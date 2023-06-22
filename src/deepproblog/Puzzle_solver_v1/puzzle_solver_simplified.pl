nn(puzzle_net,[X],Y,[triangle,circle,hexagon,pentagon,square,right_triangle,trapeze,rhombus,kite])::shape(X,Y).

are_equal(A,B,C) :- shape(A,A2),shape(B,B2), shape(C,C2), equal(A2,B2,C2).
are_equal2(A,B,S) :- shape(A,A2),shape(B,B2),equal(A2,B2,S).
equal(A,A,A).

%in case the shapes are shifted to the left
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- are_equal2(Tm, Ml, S).

% in case that the shapes are shifted to the right
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- are_equal2(Tl,Mm,S).

%in case all of the rows are the same
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- are_equal2(Bl,Bm,S).

%in case all the column are the same
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- are_equal2(Tr,Mr,S).

solution(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S).