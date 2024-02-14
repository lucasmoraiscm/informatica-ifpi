class Bicicleta:

    def __init__(self,peso,altura,cor,aro,veloc_atual=0,altura_cela=0,calibragem_pneus=20):
        self.peso=peso
        self.altura=altura
        self.cor=cor
        self.aro=aro
        self.veloc_atual=veloc_atual
        self.veloc_min=0
        self.veloc_max=40
        self.altura_cela=altura_cela
        self.altura_cela_min=5
        self.altura_cela_max=15
        self.calibragem_pneus=calibragem_pneus
        self.calibragem_pneus_min=20
        self.calibragem_pneus_max=40

    def pedalar(self):
        if self.veloc_atual+1 in range(self.veloc_min,self.veloc_max+1):
            self.veloc_atual+=1
            print("Velocidade atual:",self.veloc_atual)
        else:
            print("Velocidade máxima:",self.veloc_max)

    def frear(self):
        if self.veloc_atual-1 in range(self.veloc_min,self.veloc_max+1):
            self.veloc_atual-=1
            print("Velocidade atual:",self.veloc_atual)
        else:
            print("A bicicleta está parada!")
    
    def regular_cela(self,valor):
        if self.veloc_atual==self.veloc_min:
            if valor in range(self.altura_cela_min,self.altura_cela_max+1):
                self.altura_cela=valor
                print("Altura atual da cela:",self.altura_cela)
            else:
                print("Altura inválida!")
        else:
            print("A bicicleta está em movimento!")

    def regular_pneus(self,valor):
        if self.veloc_atual==self.veloc_min:
            if valor in range(self.calibragem_pneus_min,self.calibragem_pneus_max+1):
                self.calibragem_pneus=valor
                print("Calibragem atual dos pneus:",self.calibragem_pneus)
            else:
                print("Calibragem inválida!")
        else:
            print("A bicicleta está em movimento!")

minha_bicicleta=Bicicleta(10,100,'Vermelha',20)
print("Peso:",minha_bicicleta.peso)
print("Altura:",minha_bicicleta.altura)
print("Cor:",minha_bicicleta.cor)
print("Aro:",minha_bicicleta.aro)
minha_bicicleta.pedalar()
minha_bicicleta.frear()
minha_bicicleta.regular_cela(11)
minha_bicicleta.regular_pneus(30)

print("")

bicicleta_irmão=Bicicleta(7,75,'Preta',15,2,12,25)
print("Peso:",bicicleta_irmão.peso)
print("Altura:",bicicleta_irmão.altura)
print("Cor:",bicicleta_irmão.cor)
print("Aro:",bicicleta_irmão.aro)
bicicleta_irmão.frear()
bicicleta_irmão.frear()
bicicleta_irmão.regular_pneus(26)
bicicleta_irmão.regular_pneus(22)
bicicleta_irmão.pedalar()
bicicleta_irmão.pedalar()
bicicleta_irmão.frear()
bicicleta_irmão.frear()
bicicleta_irmão.regular_cela(6)
bicicleta_irmão.regular_cela(15)