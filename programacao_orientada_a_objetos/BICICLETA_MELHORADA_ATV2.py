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
    if veloc_atual>=0 and veloc_atual<20:
        def pedalar(self):
            self.veloc_atual+=1
            print("velocidade atual:",self.veloc_atual)

        def frear(self):
            self.veloc_atual-=1
            print("velocidade atual:",self.veloc_atual)
    else:
        print("Velocidade máxima: 20 KM/h e velocidade mínima: 0 KM/h!")

    def regular_cela(self,valor):
        if valor>=0 and valor<=15:
            self.altura_cela=valor
            print("altura atual da cela: {} cm".format(self.altura_cela))
        else:
            print("Altura máxima: 15 cm!")

    def calibrar_pneus(self,valor):
        if valor>=20 and valor<=40:
            self.calibragem_pneus=valor
            print("calibragem atual dos pneus: {} libras".format(self.calibragem_pneus))
        else:
            print("calibragem mínima: 20 libras e calibragem máxima: 40 libras!")

    if veloc_atual==0:
        def levantar_cela(self):
            self.altura_cela+=1
            print("altura atual da cela: {} cm".format(self.altura_cela))

        def baixar_cela(self):
            self.altura_cela-=1
            print("altura atual da cela: {} cm".format(self.altura_cela))
        
        def aumentar_calibragem(self):
            self.calibragem_pneus+=1
            print("calibragem atual dos pneus: {} libras".format(self.calibragem_pneus))
        
        def diminuir_calibragem(self):
            self.calibragem_pneus-=1
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
minha_bicicleta.levantar_cela()
minha_bicicleta.levantar_cela()
minha_bicicleta.baixar_cela()
minha_bicicleta.diminuir_calibragem()
minha_bicicleta.diminuir_calibragem()
minha_bicicleta.aumentar_calibragem()
print("Cor:",minha_bicicleta.cor)
print("Aro:",minha_bicicleta.aro)