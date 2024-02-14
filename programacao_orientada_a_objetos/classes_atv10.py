class Porta:
    def __init__(self,cor,tipo,altura,largura):
        self.__cor=cor
        self.__tipo=tipo
        self.__altura=altura
        self.__largura=largura
        self.__esta_fechada=False
        self.__esta_trancada=False
    
    @property
    def cor(self):
        return self.__cor

    @property
    def tipo(self):
        return self.__tipo

    @property
    def altura(self):
        return self.__altura
    
    @property
    def largura(self):
        return self.__largura
    
    @property
    def esta_fechada(self):
        return self.__esta_fechada

    @property
    def esta_trancada(self):
        return self.__esta_trancada
    
    def __str__(self):
        return "Cor:{}\nTipo:{}\nAltura:{}\nLargura:{}\nFechada:{}\nTrancada:{}".format(self.__cor,self.__tipo,self.__altura,self.__largura,self.__esta_fechada,self.__esta_trancada)
    
    def abrir(self):
        if self.__esta_fechada==True:
            if self.__esta_trancada==False:
                self.__esta_fechada=False
                print("A porta foi aberta!")
            else:
                print("Ação não realizada! A porta está trancada")
        else:
            print("Ação não realizada! A porta já está aberta")
    
    def fechar(self):
        if self.__esta_fechada==False:
            if self.__esta_trancada==False:
                self.__esta_fechada=True
                print("A porta foi fechada!")
            else:
                print("Ação não realizada! A porta está trancada")
        else:
            print("Ação não realizada! A porta já está fechada")
    
    def trancar(self):
        if self.__esta_fechada==True:
            if self.__esta_trancada==False:
                self.__esta_trancada=True
                print("A porta foi trancada!")
            else:
                print("Ação não realizada! A porta já está trancada")
        else:
            print("Ação não realizada! A porta está aberta")
    
    def destrancar(self):
        if self.__esta_fechada==True:
            if self.__esta_trancada==True:
                self.__esta_trancada=False
                print("A porta foi destrancada!")
            else:
                print("Ação não realizada! A porta já está destrancada")
        else:
            print("Ação não realizada! A porta está aberta")

class Casa:
    def __init__(self,localizacao,area_total,area_construida):
        self.__localizacao=localizacao
        self.__area_total=area_total
        self.__area_construida=area_construida
        self.__porta_frente=None
        self.__porta_fundo=None

    @property
    def localizacao(self):
        return self.__localizacao

    @property
    def area_total(self):
        return self.__area_total
    
    @property
    def area_construida(self):
        return self.__area_construida
    
    @property
    def porta_frente(self):
        return self.__porta_frente
    
    @property
    def porta_fundo(self):
        return self.__porta_fundo
    
    def __str__(self):
        return "Localização:{}\nArea total:{}\nArea construida:{}\nPorta da frente:{}\nPorta do fundo:{}".format(self.__localizacao,self.__area_total,self.__area_construida,self.__porta_frente,self.__porta_fundo)

    def trocarPorta_frente(self,porta=None):
        if type(porta)==Porta:
            self.__porta_frente=porta
            print("A porta da frente foi trocada!")
        else:
            self.__porta_frente=None
            print("Sem porta da frente!")

    def trocarPorta_fundo(self,porta=None):
        if type(porta)==Porta:
            self.__porta_fundo=porta
            print("A porta do fundo foi trocada!")
        else:
            self.__porta_fundo=None
            print("Sem porta do fundo!")

    def abrirPorta_frente(self):
        if self.__porta_frente!=None:
            self.porta_frente.abrir()
        else:
            print("Ação não realizada! A casa não tem porta da frente")

    def abrirPorta_fundo(self):
        if self.__porta_fundo!=None:
            self.porta_fundo.abrir()
        else:
            print("Ação não realizada! A casa não tem porta do fundo")
    
    def fecharPorta_frente(self):
        if self.__porta_frente!=None:
            self.porta_frente.fechar()
        else:
            print("Ação não realizada! A casa não tem porta da frente")
    
    def fecharPorta_fundo(self):
        if self.__porta_fundo!=None:
            self.porta_fundo.fechar()
        else:
            print("Ação não realizada! A casa não tem porta do fundo")
    
    def trancarPorta_frente(self):
        if self.__porta_frente!=None:
            self.porta_frente.trancar()
        else:
            print("Ação não realizada! A casa não tem porta da frente")

    def trancarPorta_fundo(self):
        if self.__porta_fundo!=None:
            self.porta_fundo.trancar()
        else:
            print("Ação não realizada! A casa não tem porta do fundo")
    
    def destrancarPorta_frente(self):
        if self.__porta_frente!=None:
            self.porta_frente.destrancar()
        else:
            print("Ação não realizada! A casa não tem porta da frente")
    
    def destrancarPorta_fundo(self):
        if self.__porta_fundo!=None:
            self.porta_fundo.destrancar()
        else:
            print("Ação não realizada! A casa não tem porta do fundo")