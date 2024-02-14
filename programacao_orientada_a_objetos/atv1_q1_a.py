class Mamiferos():
    def __init__(self,nome,idade):
        self.__nome=nome
        self.idade=idade

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        return "Nome: {}\nIdade: {}".format(self.nome,self.idade)

class Cachorro(Mamiferos):
    def __init__(self,nome,idade,late,raca):
        super().__init__(nome,idade)
        self.late=late
        self.__raca=raca
    
    @property
    def raca(self):
        return self.__raca
    
    def __str__(self):
        return super().__str__()+"\nLate: {}\nRaça: {}\n".format(self.late,self.raca)

class Macaco(Mamiferos):
    def __init__(self,nome,idade,sobe_Em_Arvores,raca):
        super().__init__(nome,idade)
        self.sobe_Em_Arvores=sobe_Em_Arvores
        self.__raca=raca

    @property
    def raca(self):
        return self.__raca

    def __str__(self):
        return super().__str__()+"\nSobe em árvores: {}\nRaca: {}\n".format(self.sobe_Em_Arvores,self.raca)

class Homem(Mamiferos):
    def __init__(self,nome,idade,fala):
        super().__init__(nome,idade)
        self.fala=fala

    def __str__(self):
        return super().__str__()+"\nFala: {}\n".format(self.fala)

tom=Cachorro("Tom",3,"Au au","Pug")
print(tom)

dudu=Macaco("Dudu",5,"Sobe a bananeira","Macaco-prego")
print(dudu)

jose=Homem("José",37,"Olá, tudo bem?")
print(jose)