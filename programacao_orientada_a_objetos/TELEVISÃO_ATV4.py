class Televisão:

    def __init__(self,volume_min=1,volume_max=100):
        self.ligada=False
        self.canal=None
        self.canal_min=1
        self.canal_max=100
        self.volume=None
        self.volume_min=volume_min
        self.volume_max=volume_max
    
    def ligar(self):
        self.ligada=True
        self.volume=self.volume_min
        self.canal=self.canal_min
        print("TV ligada!")

    def desligar(self):
        self.ligada=False
        print("TV desligada!")
    
    def mudar_canal(self,valor):
        if self.ligada:
            if valor in range(self.canal_min,self.canal_max+1):
                self.canal=valor
                print("Canal atual:",self.canal)
            else:
                print("Canal inválido!")
        else:
            print("Operação não realizada. A TV está desligada!")
    
    def aumentar_canal(self,valor=1):
        if self.ligada:
            if self.canal+1 in range(self.canal_min,self.canal_max+1):
                self.canal+=valor
                print("Canal atual:",self.canal)
            else:
                print("Canal inválido!")
        else:
            print("Operação não realizada. A TV está deligada!")
    
    def diminuir_canal(self,valor=1):
        if self.ligada:
            if self.canal-1 in range(self.canal_min,self.canal_max+1):
                self.canal-=valor
                print("Canal atual:",self.canal)
            else:
                print("Canal inválido!")
        else:
            print("Operação não realizada. A TV está desligada!")
    
    def mudar_volume(self,valor):
        if self.ligada:
            if valor in range(self.volume_min,self.volume_max+1):
                self.volume=valor
                print("Volume atual:",self.volume)
            else:
                print("Volume inválidade!")
        else:
            print("Operação não realizada. A TV está desligada!")

    def aumentar_volume(self,valor=1):
        if self.ligada:
            if self.volume+1 in range(self.volume_min,self.volume_max+1):
                self.volume+=valor
                print("Volume atual:",self.volume)
            else:
                print("Volume inválido!")
        else:
            print("Operação não realizada. A TV está desligada!")
    
    def diminuir_volume(self,valor=1):
        if self.ligada:
            if self.volume-1 in range(self.volume_min,self.volume_max+1):
                self.volume-=valor
                print("Volume atual:",self.volume)
            else:
                print("Volume inválido!")
        else:
            print("Operação não realizada. A TV está desligada!")

televisão1=Televisão(1,50)
televisão1.ligar()
televisão1.aumentar_canal(23)
televisão1.diminuir_canal()
televisão1.diminuir_canal(5)
televisão1.aumentar_volume(47)
televisão1.diminuir_volume(10)
televisão1.desligar()

print("")

televisão2=Televisão()
televisão2.aumentar_canal(13)
televisão2.ligar()
televisão2.diminuir_volume(30)
televisão2.aumentar_canal(55)
televisão2.aumentar_volume(88)
televisão2.diminuir_volume(28)
televisão2.desligar()