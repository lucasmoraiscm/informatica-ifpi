class Cliente:
    def __init__(self,cpf,nome):
        self.__cpf=cpf
        self.__nome=nome

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    def __str__(self):
        return "Nome:{}\nCPF:{}".format(self.__nome,self.__cpf)

class Conta:
    def __init__(self,numero,titular,saldo=0):
        if type(titular)==Cliente:
            self.__titular=titular
            self.__numero=numero
            self.__saldo=saldo
        else:
            print("Criação da conta não realizada! Cliente não encontrado")
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def saldo(self):
        return self.__saldo

    def depositar(self,valor):
        self.__saldo+=valor
        print("Deposito realizado com sucesso!")
    
    def sacar(self,valor):
        if valor<=self.__saldo:
            self.__saldo-=valor
            print("Saque realizada com sucesso!")
        else:
            print("Saque não realizada! Saldo indisponível")
    
    def __str__(self):
        return "Número da conta:{}\nSaldo:{}".format(self.__numero,self.__saldo)

class Banco:
    def __init__(self,nome):
        self.__nome=nome
        self.__contas=[]
        self.__valorTotal=0

    @property
    def nome(self):
        return self.__nome
    
    @property
    def valorTotal(self):
        return self.__valorTotal
    
    #@property
    #def contas(self):
    #    return self.__contas

    def adicionar(self,conta):
        if type(conta)==Conta:
            self.__contas.append(conta)
            self.__valorTotal+=conta.saldo
            print("Conta adicionada com sucesso!")
        else:
            print("Adição da conta não realizada! Conta inexistente")

    def remover(self,conta):
        if type(conta)==Conta:
            if conta.saldo==0:
                self.__contas.remove(conta)
                self.__valorTotal-=conta.saldo
                print("Conta removida realizada com sucesso!")
            else:
                print("Remoção da conta não realizada! A conta ainda possui saldo")
        else:
            print("Remoção da conta não realizada! Conta inexistente")

    def __str__(self):
        return "Nome do banco:{}\nValor total depositado:{}".format(self.__nome,self.__valorTotal)