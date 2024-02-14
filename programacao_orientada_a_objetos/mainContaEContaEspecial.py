from ContaEContaEspecial import *;

#Conta
c1=Conta(12345,"Antônio",1000)
c2=Conta(54321,"Beatriz",2000)

c1.deposito(100)
c1.saque(500)
c1.transfere(200,c2)

c1.extrato()
c2.extrato()

#Conta Especial
c3=ContaEspecial(98765,"Carla",1000,300)
c4=ContaEspecial(56789,"Daniel",2000,600)

c3.saque(1300)
c3.extrato()
c3.deposito(800)
c3.extrato()
c3.transfere(300,c4)

c3.extrato()
c4.extrato()
