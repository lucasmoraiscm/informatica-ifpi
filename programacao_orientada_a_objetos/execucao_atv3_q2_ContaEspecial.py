from atv3_q2_ContaEspecial import*;

c1=Conta(1,12345678901,3000)
c1.sacar(170)
c1.depositar(500)
c1.extrato()

c2=ContaEspecial(2,10987654321,2000,1000)
c2.sacar(2550)
c2.transferir(200,c1)
c2.extrato()

c1.extrato()

c2.depositar(1500)
c2.extrato()