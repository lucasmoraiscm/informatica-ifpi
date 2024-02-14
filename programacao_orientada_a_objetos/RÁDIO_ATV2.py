class Radio:
    cor=None
    frequencia=None
    volume_atual=0
    estado=None

    def ligar(self):
        self.estado="ligado"
        print("estado atual:",self.estado)

    def desligar(self):
        self.estado="desligado"
        print("estado atual:",self.estado)

    def frequencia(self,valor):
        self.frequencia=valor
        print("frequência atual:",self.frequencia,"MHz")

    def aumentar(self):
        self.volume_atual+=1
        print("volume atual:",self.volume_atual,"dB")

    def diminuir(self):
        self.volume_atual-=1
        print("volume atual:",self.volume_atual,"dB")

meu_radio=Radio()
meu_radio.cor='preto'
print("cor:",meu_radio.cor)
meu_radio.ligar()
meu_radio.frequencia(101.1)
meu_radio.aumentar()
meu_radio.aumentar()
meu_radio.diminuir()
meu_radio.desligar()

print("")

vizinho_radio=Radio()
vizinho_radio.cor='cinza'
print("cor:",vizinho_radio.cor)
vizinho_radio.ligar()
vizinho_radio.frequencia(105.7)
vizinho_radio.aumentar()
vizinho_radio.diminuir()
vizinho_radio.desligar()