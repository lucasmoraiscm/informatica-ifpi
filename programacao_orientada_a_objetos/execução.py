from classes import *;
tv1=Televisão()
tv2=Televisão()
tv3=Televisão()

c1=ControleRemoto()
c2=ControleRemoto()
c3=ControleRemoto()

c1.ligarDesligar()
c2.ligarDesligar()
c3.ligarDesligar()

c1.vincularTv(tv1)
c2.vincularTv(tv2)

c1.ligarTv()
c1.mudarCanal(4)
c1.aumentarVolume(20)

c2.ligarTv()
c2.aumentarVolume()
c2.desvincularTv()

c3.mudarCanal(13)
c3.aumentarVolume(45)
c3.ligarDesligar()