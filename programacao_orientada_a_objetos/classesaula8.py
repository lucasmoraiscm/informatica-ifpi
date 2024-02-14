class Televisão:
    def __init__(self,ligada=False):
        self.__ligada=ligada
    
    @property
    def ligada(self):
        return self.__ligada
    
    def ligarTv():
        self.__ligada=True
        print("TV ligada!")
    
    def desligarTv():
        self.__ligada=False
        print("TV desligada!")
    

class ControleRemoto:
    def __init__(self,ligado=False):
        self.__ligado=ligado

    @property
    def ligado(self):
        return self.__ligado

    def ligar():
        self.__ligado=True
        print("Controle remoto ligado!")

    def desligar():
        self.__ligado=False
        print("Controle remoto desligado!")