class Televisão:
    def __init__(self,volume_min=0,volume_max=100,canal_min=1,canal_max=100):
        self.ligada=False
        self.canal=None
        self.canal_min=canal_min
        self.canal_max=canal_max
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
                print("Canal alterado! Canal atual:",self.canal)
            else:
                print("Operação não realizada. Canal inválido!")
        else:
            print("Operação não realizada. A TV está desligada!")

    def aumentar_volume(self,valor=1):
        if self.ligada:
            if self.volume+1 in range(self.volume_min,self.volume_max+1):
                self.volume+=valor
                print("Volume aumentado! Volume atual:",self.volume)
            else:
                print("Operação não realizada. Volume inválido!")
        else:
            print("Operação não realizada. A TV está desligada!")
    
    def diminuir_volume(self,valor=1):
        if self.ligada:
            if self.volume-1 in range(self.volume_min,self.volume_max+1):
                self.volume-=valor
                print("Volume diminuido! Volume atual:",self.volume)
            else:
                print("Operação não realizada. Volume inválido!")
        else:
            print("Operação não realizada. A TV está desligada!")

class ControleRemoto:
    def __init__(self,ligado=False):
        self.__ligado=ligado
        self.__tv=None

    @property
    def ligado(self):
        return self.__ligado
    
    def ligarDesligar(self):
        if self.__ligado==False:
            self.__ligado=True
            print("O controle remoto está ligado!")
        else:
            self.__ligado=False
            print("O controle remoto está desligado!")
        
    @property
    def tv(self):
        return self.__tv
    
    def vincularTv(self,tv):
        if self.__ligado==True:
            if type(tv)==Televisão:
                self.__tv=tv
                print("O controle remoto foi vinculado a tv:",self.__tv)
            else:
                print("Operação não realizada. TV não encontrada!")
        else:
            print("Operação não realizada. Controle remoto desligado!")
    
    def desvincularTv(self):
        if self.__ligado==True:
            self.__tv==None
            print("O controle remoto foi desvinculado da tv:",self.__tv)
        else:
            print("Operação não realizada. Controle remoto desligado!")

    def ligarTv(self):
        if self.__ligado==True:
            if self.__tv!=None:
                self.tv.ligar()
            else:
                print("Operação não realizada! O controle remoto não está vinculada a tv")
        else:
            print("Operação não realizada. O controle remoto está desligado!")
    
    def desligarTv(self):
        if self.__ligado==True:
            if self.__tv!=None:
                self.tv.desligar()
            else:
                print("Operação não realizada! O controle remoto não está vinculada a tv")
        else:
            print("Operação não realizada. O controle remoto está desligado!")
    
    def mudarCanal(self,valor):
        if self.__ligado==True:
            if self.__tv!=None:
                self.tv.mudar_canal(valor)
            else:
                print("Operação não realizada. O controle remoto não está vinculada a tv!")
        else:
            print("Operação não realizada. O controle remoto está desligado!")
    
    def aumentarVolume(self,valor=1):
        if self.__ligado==True:
            if self.__tv!=None:
                self.tv.aumentar_volume(valor)
            else:
                print("Operação não realizada. O controle remoto não está vinculada a tv!")
        else:
            print("Operação não realizada. O controle remoto está desligado!")
    
    def diminuirVolume(self,valor=1):
        if self.__ligado==True:
            if self.__tv!=None:
                self.tv.diminuir_volume(valor)
            else:
                print("Operação não realizada. O controle remoto não está vinculada a tv!")
        else:
            print("Operação não realizada. O controle remoto está desligado!")