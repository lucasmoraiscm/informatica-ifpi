class Pessoa:

    def __init__(self,nome):
        self.__nome=nome

    def getnome(self):
        return self.__nome #Método para visualizar o nome (getter)
    
    def setnome(self,nome): #Método para alterar o nome (setter)
        self.__nome=nome
    
    @property
    def nome(self):
        return self.__nome #getter
    
    @nome.setter
    def nome(self,nome):
        self.__nome=nome #setter (ñ obrigatório)

maria=Pessoa("Maria")
print(maria.getnome())
maria.setnome("Eric")
print(maria.getnome())
print(maria.nome)
maria.nome="Ricardo"
print(maria.nome)
print(maria.getnome())