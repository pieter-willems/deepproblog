nn(toy_net,[X],Y,[0,1,2,3,4]) :: color(X,Y).

thesame(A, A).

check_color(X,Y) :- color(X,C), thesame(C, Y).