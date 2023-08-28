nn(puzzle_net,[X],Y,[triangle,circle,hexagon])::shape(X,Y).

are_equal(A,B,C) :- shape(A,A2),shape(B,B2), shape(C,C2), equal(A2,B2,C2).
are_equal2(A,B,S) :- shape(A,A2),shape(B,B2),equal(A2,B2,S).
equal(A,A,A).



%shape puzzle
%in case the shapes are shifted to the left
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- not(are_equal(Tl,Tm,Tr))
                                     ,not(are_equal(Tl,Ml,Bl))
                                     ,are_equal(Tr,Mm,Bl)
                                     ,are_equal(Tl,Mr,Bm)
                                     ,are_equal2(Tm, Ml, S).

% in case that the shapes are shifted to the right
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- not(are_equal(Tl,Tm,Tr))
                                     ,not(are_equal(Tl,Ml,Bl))
                                     ,not(are_equal(Tr,Mm,Bl))
                                     ,are_equal(Tm,Mr,Bl)
                                     ,are_equal(Tr,Ml,Bm)
                                     ,are_equal2(Tl,Mm,S).

%in case all of the rows are the same
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- are_equal(Tl,Tm,Tr)
                                     ,are_equal(Ml,Mm,Mr)
                                     ,are_equal2(Bl,Bm,S).

%in case all the column are the same
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- not(are_equal(Tl,Tm,Tr))
                                     ,are_equal(Tl,Ml,Bl)
                                     ,are_equal(Tm,Mm,Bm)
                                     ,are_equal2(Tr,Mr,S).


solution(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S).