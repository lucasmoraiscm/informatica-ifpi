class Seguro:
    def __init__(self,num,proprietario):
        self._num_apolice=num
        if type(proprietario)==Cliente:
            self._proprietario=proprietario
        else:
            raise ValueError
    
    def calculaValor(self):
        pass

    def calculaPremio(self):
        pass

    def __str__(self):
        return "Número da apólice: {}\nProprietario: {}\nValor: {}\nPrêmio: {}".format(self._num_apolice,self._proprietario.nome,self.calculaValor(),self.calculaPremio())

class SeguroVida(Seguro):
    def __init__(self,num,proprietario,nome):
        super().__init__(num,proprietario)
        self._nome_Beneficiario=nome

    @property
    def nome_Beneficiario(self):
        return self._nome_Beneficiario
    
    def calculaValor(self):
        if self._proprietario.idade<=30:
            return 800
        elif self._proprietario.idade>30 and self._proprietario.idade<=50:
            return 1300
        elif self._proprietario.idade>50:
            return 1600

    def calculaPremio(self):
        if self._proprietario.idade<=30:
            return 50000
        elif self._proprietario.idade>30 and self._proprietario.idade<=50:
            return 30000
        elif self._proprietario.idade>50:
            return 20000

    def __str__(self):
        return super().__str__()+"\nNome do beneficiário: {}\n".format(self.nome_Beneficiario)

class SeguroAutomóvel(Seguro):
    def __init__(self,num,proprietario,num_licenca,nome,ano,valorAutomovel):
        super().__init__(num,proprietario)
        self._num_Licenca=num_licenca
        self._nome_Modelo=nome
        self._ano=ano
        self._valorAutomovel=valorAutomovel
    
    @property
    def num_Licenca(self):
        return self._num_Licenca

    @property
    def nome_Modelo(self):
        return self._nome_Modelo
    
    @property
    def ano(self):
        return self._ano
    
    @property
    def valorAutomovel(self):
        return self._valorAutomovel

    def calculaValor(self):
        return self.valorAutomovel*0.03

    def calculaPremio(self):
        return self.valorAutomovel*0.8

    def calculaFranquia(self):
        return self.calculaValor()*0.4

    def __str__(self):
        return super().__str__()+"\nNúmero da licença: {}\nNome do modelo: {}\nAno: {}\nValor do automóvel: {}\nFranquia: {}\n".format(self.num_Licenca,self.nome_Modelo,self.ano,self.valorAutomovel,self.calculaFranquia())

class Cliente:
    def __init__(self,cpf,nome,idade):
        self.__cpf=cpf
        self.__nome=nome
        self.__idade=idade

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade
