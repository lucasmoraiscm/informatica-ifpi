class ContaCorrente():
    def __init__(self,num,saldo):
        self.num=num
        self._saldo=saldo
    
    def creditar(self,valor):
        self._saldo+=valor
        print("Ação realizada! O valor foi creditado")

    def debitar(self,valor):
        if valor<=self._saldo:
            self._saldo-=valor
            print("Ação realizada! O valor foi debitado")
        else:
            print("Ação não realizada! Saldo indisponível")

    @property
    def saldo(self):
        return self._saldo
   
    def transferir(self,valor,conta):
        if valor<=self._saldo:
            if type(conta)==ContaCorrente or type(conta)==ContaPoupança:
                print("Transferência em andamento! Aguarde um instante...")
                self.debitar(valor)
                conta.creditar(valor)
                print("Transferência realizada! O valor foi transferido")
            else:
                print("Ação não realizada! Conta destino não encontrada")
        else:
            print("Ação não realizada! Saldo indisponínel")
    
    def __str__(self):
        return "Número da conta: {}\nSaldo: {} R$".format(self.num,round(self._saldo,2))

class ContaPoupança(ContaCorrente):
    def __init__(self,num,saldo,taxaJuros):
        super().__init__(num,saldo)
        self.taxaJuros=taxaJuros

    def renderJuros(self):
        self._saldo+=self._saldo*(self.taxaJuros/100)
        print("Os juros renderam!")

    def __str__(self):
        return super().__str__()+"\nTaxa de juros: {} %".format(self.taxaJuros)

class ContaImposto(ContaCorrente):
    def __init__(self,num,saldo,percentual):
        super().__init__(num,saldo)
        self.percentualImposto=percentual
    
    def calculaImposto(self):
        self._saldo-=self._saldo*(self.percentualImposto/100)
        print("O imposto foi calculado!")

    def __str__(self):
        return super().__str__()+"\nPercentual de impostos: {} %\n".format(self.percentualImposto)
