class Televisão:

    def __init__(self,volume_min,volume_max):  # construtor da classe
        self.ligada=False
        self.canal=None
        self.canal_min=2
        self.canal_max=99
        self.volume=None
        self.volume_min=volume_min
        self.volume_max=volume_max


    def ligar(self):
        self.ligada=True
        self.volume=self.volume_min
        self.canal=self.canal_min

    def desligar(self):
        self.ligada=False

    def mudar_canal(self,valor):
        if self.ligada:  #self.ligada==True
           if valor in range(self.canal_min,self.canal_max+1):
               self.canal=valor
               print("canal mudado para o valor:",self.canal)
           else:
               print("canal inválido!")
        else:
            print("Operação não realizada. Tv está desligada!")

    def aumentar_canal(self):
        if self.ligada:  #self.ligada==True
           if self.canal+1 in range(self.canal_min,self.canal_max+1):
               self.canal+=1 # self.canal=self.canal+1
               print("canal mudado para o valor:",self.canal)
           else:
               print("canal inválido!")
        else:
            print("Operação não realizada. Tv está desligada!")

    def diminuir_canal(self):
        if self.ligada:  #self.ligada==True
           if self.canal-1 in range(self.canal_min,self.canal_max+1):
               self.canal-=1 # self.canal=self.canal-1
               print("canal mudado para o valor:",self.canal)
           else:
               print("canal inválido!")
        else:
            print("Operação não realizada. Tv está desligada!")

    def aumentar_volume(self):
        if self.ligada:  #self.ligada==True
           if self.volume+1 in range(self.volume_min,self.volume_max+1):
               self.volume+=1 # self.canal=self.volume+1
               print("volume mudado para o valor:",self.volume)
           else:
               print("volume inválido!")
        else:
            print("Operação não realizada. Tv está desligada!")

    def diminuir_volume(self):
        if self.ligada:  #self.ligada==True
           if self.volume-1 in range(self.volume_min,self.volume_max+1):
               self.volume-=1 # self.canal=self.volume-1
               print("volume mudado para o valor:",self.volume)
           else:
               print("volume inválido!")
        else:
            print("Operação não realizada. Tv está desligada!")



tv1 = Televisão(1,10)
tv2 = Televisão(1,50)
tv1.ligar()
tv1.mudar_canal(101)
tv2.ligar()
for i in range(3):
    tv2.aumentar_volume()