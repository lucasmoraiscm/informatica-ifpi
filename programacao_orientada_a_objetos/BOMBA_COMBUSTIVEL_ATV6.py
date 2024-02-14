class BombaCombustível:

    def __init__(self,numero,valorLitro,capacidadeBomba,quantidadeCombustivel,tipoCombustivel=1):
        self.__numero=numero
        self.__valorLitro=valorLitro
        self.__capacidadeBomba=capacidadeBomba
        self.__quantidadeCombustivel=quantidadeCombustivel
        self.__tipoCombustivel=tipoCombustivel
        self.__valor_faturado=0
        self.__quantidade_vendida=0
    
    @property
    def numero(self):
        return self.__numero

    @property
    def valorLitro(self):
        return round(self.__valorLitro,2)

    @valorLitro.setter
    def valorLitro(self,valor):
        self.__valorLitro=valor
        print("O valor do combustível foi alterado para:",round(self.__valorLitro,2),"R$.")
    
    @property
    def capacidadeBomba(self):
        return round(self.__capacidadeBomba,3)
    
    @property
    def quantidadeCombustivel(self):
        return round(self.__quantidadeCombustivel,3)

    @property
    def tipoCombustivel(self):
        return self.__tipoCombustivel

    @property
    def valor_faturado(self):
        return round(self.__valor_faturado,2)

    @property
    def quantidade_vendida(self):
        return round(self.__quantidade_vendida,3)

    def abastecerBomba(self,valor):
        if valor<=self.__capacidadeBomba:
            self.__quantidadeCombustivel+=valor
            print("Quantidade atual de combustível:",round(self.__quantidadeCombustivel,3))
        else:
            print("Operação não realizada. Capacidade máxima atingida!")
    
    def abastecerVeiculoPorValor(self,valor):
        if valor/self.__valorLitro<=self.__quantidadeCombustivel:
            self.__quantidadeCombustivel-=round(valor/self.__valorLitro,3)
            self.__valor_faturado+=valor
            self.__quantidade_vendida+=round(valor/self.__valorLitro,3)
            print("O veículo foi abastecido com:",round(valor/self.__valorLitro,3),"litros => Valor:",valor,"R$.")
        else:
            print("Operação não realizada. Quantidade de combustível indisponível!")
    
    def abastecerVeiculoPorLitro(self,valor):
        if valor<=self.__quantidadeCombustivel:
            self.__quantidadeCombustivel-=valor
            self.__valor_faturado+=round(valor*self.__valorLitro,2)
            self.__quantidade_vendida+=valor
            print("O veículo foi abastecido com:",valor,"litros => Valor:",round(valor*self.__valorLitro,2),"R$.")
        else:
            print("Operação não realizada. Quantidade de combustível indisponível!")

    def __str__(self):
        return "Quantidade atual de litros da bomba:{} litros\nQuantidade de litros vendida:{} litros\nValor total faturado:{} R$".format(round(self.__quantidadeCombustivel,3),round(self.__quantidade_vendida,3),round(self.__valor_faturado,3))

bomba134=BombaCombustível(134,3.76,500,234.657)
bomba564=BombaCombustível(564,5.34,250,100,4)
bomba752=BombaCombustível(752,2.55,100,30,2)
bomba386=BombaCombustível(386,4.23,1000,750,3)

bomba134.abastecerVeiculoPorLitro(3)
bomba134.abastecerVeiculoPorValor(10.75)
bomba134.valorLitro=2.38
bomba134.abastecerVeiculoPorValor(5)
bomba134.abastecerVeiculoPorLitro(7.5)
print(bomba134)

bomba564.abastecerVeiculoPorLitro(12)
bomba564.abastecerBomba(120)
bomba564.valorLitro=4.88
bomba564.abastecerVeiculoPorValor(134)
bomba564.abastecerBomba(500)
print(bomba564)

bomba752.abastecerVeiculoPorLitro(33)
bomba752.abastecerVeiculoPorValor(50)
bomba752.abastecerVeiculoPorValor(400)
bomba752.abastecerBomba(50)
bomba752.abastecerVeiculoPorLitro(5.5)
print(bomba752)

bomba386.abastecerBomba(100)
bomba386.valorLitro=4
bomba386.abastecerVeiculoPorValor(40)
bomba386.abastecerVeiculoPorLitro(25)
bomba386.abastecerVeiculoPorLitro(12.5)
bomba386.abastecerVeiculoPorValor(250)
bomba386.abastecerVeiculoPorValor(52.5)
print(bomba386)