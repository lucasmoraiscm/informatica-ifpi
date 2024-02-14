class Conta(object):

    def __init__(self, id_conta,id_cliente,saldo):
        self.id_conta=id_conta
        self.id_cliente=id_cliente
        self.saldo=saldo

    def sacar(self,valor):
        if valor<=self.saldo:
            self.saldo-=valor
            return True
        return False

    def transferir(self,valor,conta):
        if valor<=self.saldo:
            self.sacar(valor)
            conta.depositar(valor)
            return True
        return False

    def depositar(self,valor):
        self.saldo+=valor

    def __str__(self):
        return "No.DaConta:%d Saldo: %.2f"%(self.id_conta,self.saldo)



c1=Conta(12345,543321,500)
c2=Conta(84634,67932,200)
c1.sacar(300)
c1.depositar(150)
c1.transferir(200,c2)
print(c1)
print(c2)