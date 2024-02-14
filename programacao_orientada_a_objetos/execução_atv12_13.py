from classes_atv12_13 import*;
joao=Cliente(12345678901,"João")
maria=Cliente(10987654321,"Maria")
madalena=Cliente(52451546325,"Madalena")

c1=Conta(12345,joao,100)
c2=Conta(54321,maria,5000)
c3=Conta(52643,maria,0)
c4=Conta(73264,madalena,46500)
c5=Conta(29378,joao,0)
c6=Conta(38584,joao,15000)

b1=Banco("Caixa")
b2=Banco("Banco do Brasil")
b3=Banco("Bradesco")

b1.adicionar(c1)
c1.depositar(500)
c1.sacar(10000)
print(c1)

b2.adicionar(c2)
c2.sacar(740)
b2.remover(c2)
print(c2)

b3.adicionar(c3)
b3.remover(c3)
print(c3)

b3.adicionar(c4)
c4.sacar(10000)
c4.depositar(2500)
print(c4)

b1.adicionar(c5)
c5.depositar(8000)
print(c5)

b2.adicionar(c6)
c6.sacar(500)
c6.sacar(4000)
print(c6)

print(b1)
print(b2)
print(b3)

#print(b1.contas)