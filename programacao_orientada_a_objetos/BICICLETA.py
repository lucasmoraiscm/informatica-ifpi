class Bicicleta:
    #Atributos
    peso=None
    altura=None
    veloc_atual=0
    cor=None
    aro=None
    altura_cela=0
    calibragem_pneus=0

    #Métodos
    def pedalar(self):
        self.veloc_atual+=1
        print("velocidade atual:",self.veloc_atual)
    
    def frear(self):
        self.veloc_atual-=1
        print("velocidade atual:",self.veloc_atual)

    def regular_cela(self,valor):
        self.altura_cela=valor
        print("altura atual da cela: {} cm".format(self.altura_cela))

    def calibrar_pneus(self,valor):
        self.calibragem_pneus=valor
        print("calibragem atual dos pneus: {} libras".format(self.calibragem_pneus))

#Criação de objetos

minha_bicicleta = Bicicleta()
minha_bicicleta.peso=10
minha_bicicleta.altura=100
minha_bicicleta.cor='amarela'
minha_bicicleta.aro=29
minha_bicicleta.regular_cela(5)
minha_bicicleta.calibrar_pneus(25)
minha_bicicleta.pedalar()
minha_bicicleta.pedalar()
minha_bicicleta.frear()
minha_bicicleta.frear()
print("Cor:",minha_bicicleta.cor)
print("Aro:",minha_bicicleta.aro)