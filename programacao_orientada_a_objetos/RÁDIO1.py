class Radio:
    #Atributos
    cor=None
    estação_atual:1
    volume_atual:0
    estado=None

    #Métodos
    def ligar(self):
        self.estado='ligado'
        print("estado atual:",self.estado)
    
    def desligar(self):
        self.estado='desligado'
        print("estado atual:",self.estado)

    def próxima_estação(self):
        self.estação_atual+=1
        print("estação atual:",self.estação_atual)
    
    def voltar_estação(self):
        self.estação_atual-=1
        print("estação atual",self.estação_atual)
    
    def aumentar_volume(self):
        self.volume_atual+=1
        print("volume atual:",self.volume_atual)

    def diminuir_volume(self):
        self.volume_atual-=1
        print("volume atual:",self.volume_atual)

#Criação de objetos

meu_radio=Radio()
meu_radio.cor='preto'
meu_radio.ligar()
meu_radio.próxima_estação()
meu_radio.voltar_estação()
meu_radio.aumentar_volume()
meu_radio.desligar()
print("cor:",meu_radio.cor)