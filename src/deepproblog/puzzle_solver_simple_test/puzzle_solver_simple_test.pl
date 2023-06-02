nn(puzzle_net,[X],Y,[triangle,circle,hexagon,pentagon,square,right_triangle,trapeze,rhombus,kite])::shape(X,Y).


solution(Tl,Tr,Bl,Tls,Trs,Bls) :- shape(Tl,Tl2),shape(Tr,Tr2),shape(Bl,Bl2), Tl2 = Tls, Tr2=Trs, Bl2=Bls.