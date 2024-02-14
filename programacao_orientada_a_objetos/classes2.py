class Bateria:
    def __init__(self,codigo,capacidade,percentual_carga=0):
        self.__codigo=codigo
        self.__capacidade=capacidade
        self.__percentual_carga=percentual_carga
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def capacidade(self):
        return self.__capacidade
    
    @property
    def percentual_carga(self):
        return self.__percentual_carga
    
    def carregar(self,valor):
        if self.__percentual_carga<=100:
            if self.__percentual_carga+valor<=100:
                self.__percentual_carga+=valor
                print("Bateria carregada! Percentual atual:",self.__percentual_carga)
            else:
                print("Operação não realizada! O valor excede o limite(100).")
        else:
            print("Operação não realizada! A bateria está completamente carregada.")

    def descarregar(self,valor):
        if self.__percentual_carga>=0:
            if self.__percentual_carga-valor>=0:
                self.__percentual_carga-=valor
                print("Bateria descarregada! Percentual atual:",self.__percentual_carga)
            else:
                print("Operação não realizada! O valor excede o limite(0).")
        else:
            print("Operação não realizada! A bateria está completamente vazia.")

class Celular:
    def __init__(self,mei,wifi="desligado"):
        self.__mei=mei
        self.__wifi=wifi
        self.__bateria=None
        self.__ligado=False
    
    @property
    def bateria(self):
        return self.__bateria
    
    def colocarBateria(self,bateria):
        if self.__bateria==None:
            if type(bateria)==Bateria:
                self.__bateria=bateria
                print("A bateria",self.__bateria,"foi colocada no celular!")
            else:
                print("Operação não realizada! Bateria inexistente.")
        else:
            print("Operação não realizada! O celular está com bateria!")

    def retirarBateria(self):
        if self.__bateria!=None:
            self.__bateria=None
            self.__ligado=False
            print("Bateria retirada!")
        else:
            print("Operação não realizada! O celular está sem bateria.")

    @property
    def mei(self):
        return self.__mei
    
    @property
    def wifi(self):
        return self.__wifi
    
    def ligarDesligarWifi(self):
        if self.__bateria!=None:
            if self.__ligado==True:
                if self.__wifi=="ligado":
                    self.__wifi="desligado"
                    print("Wifi desligado!")
                else:
                    self.__wifi="ligado"
                    print("Wifi ligado!")
            else:
                print("Operação não realizada! O celular está desligado.")
        else:
            print("Operação não realizada! O celular está sem bateria.")
    
    @property
    def ligado(self):
        return self.__ligado
    
    def ligarDesligar(self):
        if self.__bateria!=None:
            if self.bateria.percentual_carga!=0:
                if self.__ligado==True:
                    self.__ligado=False
                    if self.__wifi=="ligado":
                        self.__wifi="desligado"
                    print("Celular desligado!")
                else:
                    self.__ligado=True
                    print("Celular ligado!")
            else:
                print("Operação não realizada. A bateria está descarregada.")
        else:
            print("Operação não realizada! O celular está sem bateria.")
    
    def assistirVideo(self,tempo):
        if self.__wifi=="ligado":
            if self.bateria.percentual_carga-(tempo*5)>=0:
                self.bateria.descarregar(tempo*5)
                print("Video assistido!")
            else:
                print("Operação não realizada! Bateria insuficiente.")
        else:
            print("Operação não realizada! O wifi está desligado.")

    def carregar(self,valor):
        if self.bateria!=None:
            self.bateria.carregar(valor)
        else:
            print("Operação não realizada! O celular está sem bateria.")
    
    def descarregar(self,valor):
        if self.bateria!=None:
            if self.__ligado==True:
                self.bateria.descarregar(valor)
            else:
                print("Operação não realizada! O celular está desligado.")
        else:
            print("Operação não realizada! O celular está sem bateria.")