nn(puzzle_net,[X],Y,[triangle,circle,square])::shape(X,Y).
nn(colour_net,[X],Y,[red,yellow,green]) :: colour(X,Y).

are_equal(A,B,C) :- shape(A,A2),shape(B,B2), shape(C,C2), equal(A2,B2,C2).
are_equal2(A,B,S) :- shape(A,A2),shape(B,B2),equal(A2,B2,S).
are_colour_equal(A,B,C):- colour(A,A2),colour(B,B2),colour(C,C2), equal(A2,B2,C2).
are_colour_equal2(A,B,S) :- colour(A,A2),colour(B,B2),equal(A2,B2,S).
equal(A,B,C) :- A=B,B=C,A=C.
unequal(A,B,C):- A\=B,B\=C,A\=C.
are_not_equal(A,B,C):- shape(A,A2), shape(B,B2), shape(C,C2),unequal(A2,B2,C2).
are_not_colour_equal(A,B,C):-colour(A,A2), colour(B,B2), colour(C,C2),unequal(A2,B2,C2).



%shape puzzle
%in case the shapes are shifted to the left
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- are_not_equal(Tl,Tm,Tr)
                                     ,are_not_equal(Tl,Ml,Bl)
                                     ,are_equal(Tr,Mm,Bl)
                                     ,are_equal(Tl,Mr,Bm)
                                     ,are_equal2(Tm, Ml, S).

% in case that the shapes are shifted to the right
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- are_not_equal(Tl,Tm,Tr)
                                     ,are_not_equal(Tl,Ml,Bl)
                                     ,are_not_equal(Tr,Mm,Bl)
                                     ,are_equal(Tm,Mr,Bl)
                                     ,are_equal(Tr,Ml,Bm)
                                     ,are_equal2(Tl,Mm,S).

%in case all of the rows are the same
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- are_not_equal(Tl,Ml,Bl)
                                     ,are_not_equal(Tm,Mm,Bm)
                                     ,are_equal(Tl,Tm,Tr)
                                     ,are_equal(Ml,Mm,Mr)
                                     ,are_equal2(Bl,Bm,S).

%in case all the column are the same
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S) :- are_not_equal(Tl,Tm,Tr)
                                     ,are_equal(Tl,Ml,Bl)
                                     ,are_equal(Tm,Mm,Bm)
                                     ,are_equal2(Tr,Mr,S).
%in case all the same
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S):- are_equal(Tl,Tm,Tr),
                                    are_equal(Tl,Ml,Bl),
                                    are_equal(Tl,Mm,Mr),
                                    are_equal2(Tl,Bm,S).


%colour puzzle
%in case the shapes are shifted to the left
colour_puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,C) :- are_not_colour_equal(Tl,Tm,Tr)
                                            ,are_not_colour_equal(Tl,Ml,Bl)
                                            ,are_colour_equal(Tr,Mm,Bl)
                                            ,are_colour_equal(Tl,Mr,Bm)
                                            ,are_colour_equal2(Tm, Ml, C).

% in case that the shapes are shifted to the right
colour_puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,C) :- are_not_colour_equal(Tl,Tm,Tr)
                                            ,are_not_colour_equal(Tl,Ml,Bl)
                                            ,are_not_colour_equal(Tr,Mm,Bl)
                                            ,are_colour_equal(Tm,Mr,Bl)
                                            ,are_colour_equal(Tr,Ml,Bm)
                                            ,are_colour_equal2(Tl,Mm,C).

%in case all of the rows are the same
colour_puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,C) :- are_not_equal(Tl,Ml,Bl)
                                            ,are_colour_equal(Tl,Tm,Tr)
                                            ,are_colour_equal(Ml,Mm,Mr)
                                            ,are_colour_equal2(Bl,Bm,C).

%in case all the column are the same
colour_puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,C) :- are_not_colour_equal(Tl,Tm,Tr)
                                            ,are_colour_equal(Tl,Ml,Bl)
                                            ,are_colour_equal(Tm,Mm,Bm)
                                            ,are_colour_equal2(Tr,Mr,C).
%in case all the same
puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,C):- are_colour_equal(Tl,Tm,Tr),
                                    are_colour_equal(Tl,Ml,Bl),
                                    are_colour_equal(Tl,Mm,Mr),
                                    are_colour_equal2(Tl,Bm,C).


solution(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S,C) :- puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,S), colour_puzzle(Tl,Tm,Tr,Ml,Mm,Mr,Bl,Bm,C).