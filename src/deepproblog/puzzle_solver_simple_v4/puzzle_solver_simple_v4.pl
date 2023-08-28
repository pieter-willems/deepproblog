nn(puzzle_net,[X],Y,[triangle,circle,square,rhombus]) :: shape(X,Y).
nn(colour_net,[X],Y,[red,yellow,green,blue]) :: colour(X,Y).


same([[A,B],[A,B]]).
same([[A,A],[A,A]]).
shifted([[A,B],[B,A]]).

puzzle(Rows) :- same(Rows).
puzzle(Rows) :- shifted(Rows).

colour_shape_combined(red,triangle,red_triangle).
colour_shape_combined(red,circle,red_circle).
colour_shape_combined(red,square,red_square).
colour_shape_combined(red,rhombus,red_rhombus).

colour_shape_combined(yellow,triangle,yellow_triangle).
colour_shape_combined(yellow,circle,yellow_circle).
colour_shape_combined(yellow,square,yellow_square).
colour_shape_combined(yellow,rhombus,yellow_rhombus).

colour_shape_combined(green,triangle,green_triangle).
colour_shape_combined(green,circle,green_circle).
colour_shape_combined(green,square,green_square).
colour_shape_combined(green,rhombus,green_rhombus).

colour_shape_combined(blue,triangle,blue_triangle).
colour_shape_combined(blue,circle,blue_circle).
colour_shape_combined(blue,square,blue_square).
colour_shape_combined(blue,rhombus,blue_rhombus).

solution(Tl,Tr,Bl,O) :- sol_col(Tl,Tr,Bl,C), sol_shape(Tl,Tr,Bl,S),colour_shape_combined(C,S,O).

sol_col(Tl,Tr,Bl,C) :- colour(Tl,Tl2), colour(Tr,Tr2), colour(Bl,Bl2), puzzle([[Tl2,Tr2],[Bl2,C]]).

sol_shape(Tl,Tr,Bl,S) :- shape(Tl,Tl3), shape(Tr,Tr3), shape(Bl,Bl3), puzzle([[Tl3,Tr3],[Bl3,S]]).