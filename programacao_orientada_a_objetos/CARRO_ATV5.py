class Carro:
    
    def __init__(self,nome,ano,cor,veloc_max=100):
        self.__ligado=False
        self.__nome=nome
        self.__ano=ano
        self.__cor=cor
        self.__veloc_min=0
        self.__veloc_max=veloc_max
        self.__veloc_atual=0

    @property
    def ligado(self):
        return self.__ligado

    def ligar(self):
        self.__ligado=True
        self.__veloc_atual=self.__veloc_min
        print("O carro está ligado!")
    
    def desligar(self):
        self.__ligado=False
        print("O carro está desligado!")

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano

    @property
    def cor(self):
        return self.__cor

    @property
    def veloc_min(self):
        return self.__veloc_min

    @property
    def veloc_max(self):
        return self.__veloc_max
    
    @property
    def veloc_atual(self):
        return self.__veloc_atual

    def acelerar(self,valor=1):
        if self.__ligado:
            if self.__veloc_atual+1 in range(self.__veloc_min,self.__veloc_max+1):
                self.__veloc_atual+=valor
                print("Velocidade atual:",self.__veloc_atual)
            else:
                print("Velocidade inválida!")
        else:
            print("Operação não realizada. O carro está desligado!")

    def parar(self,valor=1):
        if self.__ligado:
            if self.__veloc_atual-1 in range(self.__veloc_min,self.__veloc_max+1):
                self.__veloc_atual-=valor
                print("Velocidade atual:",self.__veloc_atual)
            else:
                print("Velocidade inválida!")
        else:
            print("Operação não realizada. O carro está desligado!")

ferrari=Carro("Ferrari F8 Tributo",2020,"Vermelha",340)
chevette=Carro("Chevette L 1.6/S",1993,"Prata",160)
print(ferrari.nome)
print(ferrari.ano)
print(ferrari.cor)
ferrari.ligar()
ferrari.acelerar(280)
ferrari.acelerar()
ferrari.parar(112)
ferrari.desligar()
print(chevette.nome)
print(chevette.ano)
print(chevette.cor)
chevette.ligar()
chevette.acelerar(120)
chevette.parar()
chevette.parar(50)
chevette.desligar()