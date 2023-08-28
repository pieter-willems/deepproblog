nn(puzzle_net,[X],Y,[triangle,circle,hexagon,pentagon,square,right_triangle,trapeze,rhombus,kite]) :: shape(X,Y).

are_equal(A,B):- shape(A,A2),shape(B,B2),A2=B2.
are_not_equal(A,B) :- shape(A,A2),shape(B,B2),A2\=B2.
are_equal2(A,S):- shape(A,A2), A2=S.

%in case all rows are the same
puzzle(Tl,Tr,Bl,S):-   are_not_equal(Tl,Bl),
                    are_equal(Tl,Tr),
                    are_equal2(Bl,S).

%in case all of the columns are the same
puzzle(Tl,Tr,Bl,S):- are_not_equal(Tl,Tr),
                    are_equal(Tl,Bl),
                    are_equal2(Tr,S).

%in case everything is the same
puzzle(Tl,Tr,Bl,S):- are_equal(Tl,Tr),
                    are_equal(Tl,Bl),
                     are_equal2(Tl,S).

%in case they are shifted
puzzle(Tl,Tr,Bl,S):- are_not_equal(Tl,Bl),
                      are_not_equal(Tl,Tr),
                      are_equal(Tr,Bl),
                      are_equal2(Tl,S).


solution(Tl,Tr,Bl,S) :- puzzle(Tl,Tr,Bl,S).