class Funcionario():
    def __init__(self,nome,cpf,salario):
        self.__nome=nome
        self.__cpf=cpf
        self.salario=salario
    
    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    def __str__(self):
        return "Nome: {}\nCPF: {}\nSalário: {}".format(self.nome,self.cpf,self.salario)
    
class Gerente(Funcionario):
    def __init__(self,nome,cpf,salario,departamento,gratificacao):
        super().__init__(nome,cpf,salario)
        self.qualdepartamento=departamento
        self.gratificacao=gratificacao

    def __str__(self):
        return super().__str__()+"\nQual departamento: {}\nGratificação: {}\n".format(self.qualdepartamento,self.gratificacao)

class Secretaria(Funcionario):
    def __init__(self,nome,cpf,salario,escritorio):
        super().__init__(nome,cpf,salario)
        self.qualescritorio=escritorio

    def __str__(self):
        return super().__str__()+"\nQual escritório: {}\n".format(self.qualescritorio)

Carla=Gerente("Carla",12345678901,3000,"Financeiro",1000)
print(Carla)

Gabriela=Secretaria("Gabriela",10987654321,2500,12)
print(Gabriela)