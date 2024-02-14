class Conta:
    def __init__(self,numero,cli,saldo=0):
        self.numero=numero
        self.cli=cli
        self.saldo=saldo
        self.operacoes=[]

    def deposito(self,valor):
        self.saldo+=valor
        self.operacoes.append(["Depósito",valor])

    def saque(self,valor):
        if valor<=self.saldo:
            self.saldo-=valor
            self.operacoes.append(["Saque",valor])        
            return True
        return False

    def transfere(self,valor,conta):
        if self.saque(valor):
            conta.deposito(valor)
            return True
        return False

    def extrato(self):
        print("Extrato CC Nº %s" % self.numero)
        for op in self.operacoes:
            print("%10s %10.2f" % (op[0],op[1]))
        print("%10s %10.2f\n" % ("Saldo=",self.saldo))

class ContaEspecial(Conta):
    def __init__(self,numero,cli,saldo=0,limite=0):
        super().__init__(numero,cli,saldo)
        self.limite=limite
        self.__lt=limite
        self.debito=0

    def saque(self,valor):
        if (self.saldo+self.limite)>=valor:
            op=self.saldo-valor
            if op>=0:
                self.saldo=op
                self.operacoes.append(["Saque",valor])             
                return True
            else:
                self.saldo=0
                self.limite+=op
                self.debito=op*-1
                self.operacoes.append(["Saque",valor])
                return True
        else:
            return False

    def deposito(self,valor):
        if self.limite==self.__lt:
            super().deposito(valor)
            return True
        else:              
            if valor<=self.debito:
                self.debito-=valor
                self.limite+=valor
                self.operacoes.append(["Depósito",valor])
                return True
            else:
                dif=valor-self.__lt
                self.limite=self.__lt
                self.debito=0
                self.saldo=dif
                self.operacoes.append(["Depósito",valor])
                return True

    def transfere(self, valor, conta):
        if self.saque(valor):
            conta.deposito(valor)
            return True
        return False
