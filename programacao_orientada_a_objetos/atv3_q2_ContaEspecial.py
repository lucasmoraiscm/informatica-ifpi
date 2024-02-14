class Conta(object):
   
    def __init__(self, id_conta,id_cliente,saldo=0):
        self.id_conta=id_conta
        self.id_cliente=id_cliente
        self.saldo=saldo
        self.operacoes=[]

    def sacar(self,valor):
        if valor<=self.saldo:
            self.saldo-=valor
            self.operacoes.append(["Saque",valor])
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
        self.operacoes.append(["Depósito",valor])
    
    def extrato(self):
        print("Extrato CC Nº %s" % self.id_conta)
        for op in self.operacoes:
            print("%10s %10.2f" % (op[0],op[1]))
        print("%10s %10.2f\n" % ("Saldo=",self.saldo))

    def __str__(self):
        return "No.DaConta:%d Saldo: %.2f \n"%(self.id_conta,self.saldo)

class ContaEspecial(Conta):

    def __init__(self,id_conta,id_cliente,saldo,limite):
        super().__init__(id_conta,id_cliente,saldo)
        self.limite = limite
        self.debito=0

    def sacar(self,valor):
        if valor<=(self.saldo+self.limite):
            self.saldo-=valor
            if self.saldo<0:
                self.debito-=self.saldo
                self.limite+=self.saldo
                self.saldo=0
            self.operacoes.append(["Saque",valor])
            return True
        else:
            return False

    def transferir(self, valor, conta):
        if self.sacar(valor):
            conta.depositar(valor)
            return True
        else:
            return False

    def depositar(self, valor):
        if self.debito>0:
            if valor<=self.debito:
                self.debito-=valor
                self.limite+=valor
            else:
                dif=valor-self.debito
                self.saldo+=dif
                self.limite+=self.debito
                self.debito=0
        else:
            self.saldo+=valor
        self.operacoes.append(["Depósito",valor])

    def extrato(self):
        print("Extrato CC Nº %s" % self.id_conta)
        for op in self.operacoes:
            print("%10s %10.2f" % (op[0],op[1]))
        print("%10s %10.2f\n %10s %10.2f\n" % ("Saldo=",self.saldo,"Limite=",self.limite))

    def __str__(self):
        return "No.DaConta:%d Saldo: %.2f Limite: %.2f\n"%(self.id_conta,self.saldo,self.limite)
