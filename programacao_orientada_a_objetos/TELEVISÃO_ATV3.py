class Televisão:

    def __init__(self,volume_min,volume_max):
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
    
    def aumentar_canal(self):
        if self.ligada:
            if self.canal+1 in range(self.canal_min,self.canal_max+1):
                self.canal+=1
                print("Canal atual:",self.canal)
            else:
                print("Canal inválido!")
        else:
            print("Operação não realizada. A TV está deligada!")
    
    def diminuir_canal(self):
        if self.ligada:
            if self.canal-1 in range(self.canal_min,self.canal_max+1):
                self.canal-=1
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

    def aumentar_volume(self):
        if self.ligada:
            if self.volume+1 in range(self.volume_min,self.volume_max+1):
                self.volume+=1
                print("Volume atual:",self.volume)
            else:
                print("Volume inválido!")
        else:
            print("Operação não realizada. A TV está desligada!")
    
    def diminuir_volume(self):
        if self.ligada:
            if self.volume-1 in range(self.volume_min,self.volume_max+1):
                self.volume-=1
                print("Volume atual:",self.volume)
            else:
                print("Volume inválido!")
        else:
            print("Operação não realizada. A TV está desligada!")

tv_da_sala=Televisão(1,100) #a)
tv_do_quarto=Televisão(1,100) #a)
tv_da_sala.ligar() #b)
tv_do_quarto.ligar() #b)
tv_da_sala.mudar_canal(7) #c)
tv_da_sala.mudar_volume(10) #c)
tv_do_quarto.mudar_canal(13) #d)
tv_do_quarto.mudar_volume(50) #d)
for i in range(2): #e)
    tv_da_sala.aumentar_volume()
tv_do_quarto.diminuir_canal() #f)
for i in range(3): #g)
    tv_do_quarto.diminuir_volume
tv_da_sala.mudar_canal(120) #h)
tv_do_quarto.desligar() #i)
tv_do_quarto.aumentar_canal() #j)
tv_do_quarto.aumentar_canal() #j)
for i in range(15): #k)
    tv_da_sala.diminuir_volume()
tv_da_sala.desligar() #l)