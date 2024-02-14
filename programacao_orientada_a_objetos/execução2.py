from classes2 import *;
b1=Bateria(554756346,4000,100)
b2=Bateria(365265273,3000,10)
b3=Bateria(847584384,2500,50)

c1=Celular(987654321)
c2=Celular(643543473,"ligado")
c3=Celular(564959864)

c1.colocarBateria(b1)
c2.colocarBateria(b2)
c3.colocarBateria(b3)

c1.ligarDesligar()
c1.ligarDesligarWifi()
c1.assistirVideo(20)
c1.descarregar(50)

c2.ligarDesligar()
c2.carregar(80)
c2.assistirVideo(10)
c2.carregar(50)

c3.assistirVideo(10)
c3.descarregar(20)
c3.retirarBateria()