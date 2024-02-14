class Radio:
    def __init__(self,nome,marca,volume,faixas_FM):
        if type(faixas_FM)==Estações_FM:
            self.__nome=nome
            self.__marca=marca
            self.__status="OFF"
            self.__volume=volume
            self.__faixas_FM=faixas_FM
            self.__faixa_atual=None
        else:
            raise ValueError

    @property
    def nome(self):
        return self.__nome
    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def status(self):
        return self.__status
    
    @property
    def volume(self):
        return self.__volume
    
    @property
    def faixas_FM(self):
        return self.__faixas_FM
    
    @property
    def faixa_atual(self):
        return self.__faixa_atual
    
    def ligar_Desligar(self):
        if self.status=="OFF":
            self.__status="ON"
            print("Ação realizada! O rádio está ligado")
        else:
            self.__status="OFF"
            print("Ação realizada! O rádio está desligado")
    
    def ajustar_Volume(self,valor):
        if valor>=0 and valor<=100:
            self.__volume=valor
            print("Ação realizada! Volume atual:",self.volume)
        else:
            print("Ação não realizada! Volume inválido")

    def sintonizar_Freq(self,frequencia=None):
        if frequencia!=None:
            if type(self.__faixas_FM.consultar_FM(frequencia))==Estação_FM:
                self.__faixa_atual=self.__faixas_FM.consultar_FM(frequencia)
                print("Ação realizada! Estação sintonizada")
        else:
            self.__faixa_atual=self.__faixas_FM.FMs[0]

    def sintonizar_Estilo(self,estilo):
        for i in self.__faixas_FM.FMs:
            if i.estilo_Musica==estilo:
                self.__faixa_atual=i
                print("Ação realizada! Estação sintonizada")
            else:
                print("Estilo não encontrado!")

    def __str__(self):
        if self.status=="ON":
            return "Nome: {}\nMarca: {}\nStatus: {}\nVolume: {}\nFaixa sintonizada: {}\n".format(self.nome,self.marca,self.status,self.volume,self.faixa_atual)
        else:
            print("Ação não realizada! O rádio está desligado")

class Estações_FM:
    def __init__(self):
        self.__FMs=[]

    @property
    def FMs(self):
        return self.__FMs

    def cadastrar_FM(self,FM):
        if type(FM)==Estação_FM:
            self.__FMs.append(FM)
            print("Ação realizada! A rádio foi cadastrada")
        else:
            print("Ação não realizada! Estação inexistente")
    
    def excluir_FM(self,FM):
        for i in self.__FMs:
            if i==FM:
                self.__FMs.remove(FM)
                print("Ação realizada! A rádio foi excluida")
            else:
                print("Ação não realizada! A rádio não foi encontrada")
    
    def consultar_FM(self,estação_freq_FM):
        for i in self.__FMs:
            if i.nome==estação_freq_FM or i.frequencia==estação_freq_FM:
                return i
            else:
                return None

    def atualizar_FM(self,estação_freq_FM,musica,estilo):
        for i in self.__FMs:
            if i.nome==estação_freq_FM or i.frequencia==estação_freq_FM:
                i.__musica_Atual=musica
                i.__estilo_Musica=estilo
                print("Ação realizada! A rádio foi atualizada")
            else:
                print("Ação não realizada! A rádio não foi cadastrada")
    
class Estação_FM:
    def __init__(self,frequencia,nome,musica_Atual=None,estilo_Musica=None):
        self.__frequencia=frequencia
        self.__nome=nome
        self.__status="OFF"
        self.__musica_Atual=musica_Atual
        self.__estilo_Musica=estilo_Musica

    @property
    def frequencia(self):
        return self.__frequencia

    @property
    def nome(self):
        return self.__nome
    
    @property
    def status(self):
        return self.__status

    @property
    def musica_Atual(self):
        return self.__musica_Atual

    @property
    def estilo_Musica(self):
        return self.__estilo_Musica
    
    def atualiza_Musica(self,musica,estilo):
        self.__musica_Atual=musica
        self.__estilo_Musica=estilo
        print("Ação realizada! Música atualizada")
    
    def sair_do_Ar(self):
        self.__status="OFF"
        print("Ação realizada! A rádio saiu do ar")
    
    def entrar_no_Ar(self):
        self.__status="ON"
        print("Ação realizada! A rádio entrou no ar")

    def __str__(self):
        return "Nome: {}\nFrequência: {}\nStatus: {}\nMúsica: {}\nEstilo: {}".format(self.nome,self.frequencia,self.status,self.musica_Atual,self.estilo_Musica)
