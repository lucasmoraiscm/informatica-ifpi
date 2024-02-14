class Conta(object):
   
    def __init__(self, id_conta,id_cliente,saldo):
        self.id_conta=id_conta
        self.id_cliente=id_cliente
        self.saldo=saldo

    def saque(self,valor):
        if valor<=self.saldo:
            self.saldo-=valor
            return True        
        return False    

    def transferir(self,valor,conta):  
        if valor<=self.saldo:          
            self.saque(valor)
            conta.depositar(valor)
            return True
        return False

    def depositar(self,valor):
        self.saldo+=valor      
  
    def __str__(self):
        return "No.DaConta:%d Saldo: %.2f "%(self.id_conta,self.saldo)

class ContaEspecial(Conta):

    def __init__(self,id_conta,id_cliente,saldo,limite):
        super().__init__(id_conta,id_cliente,saldo)
        self.limite = limite

    def saque(self,valor):
        if valor<=(self.saldo+self.limite):
            self.saldo-=valor
            return True        
        return False

    def depositar(self, valor):
        return super().depositar(valor)

    def transferir(self, valor, conta):
        if valor<=(self.saldo+self.limite):          
            self.saque(valor)
            conta.depositar(valor)
            return True
        return False

    def __str__(self):
        return "No.DaConta:%d Saldo: %.2f Limite: %.2f"%(self.id_conta,self.saldo,self.limite)
     
    
    
c1 = Conta(1,1,100.00)
print(c1)
c2 = ContaEspecial(2,2,500.00,500.00)
print(c2.saque(600))
print(c2)