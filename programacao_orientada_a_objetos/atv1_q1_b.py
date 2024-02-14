class Cliente():
    def __init__(self,cod,end):
        self.__cod=cod
        self.end=end

    @property
    def cod(self):
        return self.__cod
    
    def localizarEndereco(self):
        print("Endereço:",self.end)

    def __str__(self):
        return "Código: {}\nEndereço: {}".format(self.cod,self.end)

class ClienteFisico(Cliente):
    def __init__(self,cod,end,nome,cpf):
        super().__init__(cod,end)
        self.__nome=nome
        self.__cpf=cpf
    
    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    def verificarCpf(self):
        print("CPF:",self.cpf)
    
    def __str__(self):
        return super().__str__()+"\nNome: {}\nCPF: {}\n".format(self.nome,self.cpf)
    
class ClienteJuridico(Cliente):
    def __init__(self,cod,end,cnpj,razaoSocial):
        super().__init__(cod,end)
        self.__cnpj=cnpj
        self.__razaoSocial=razaoSocial
    
    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def razaoSocial(self):
        return self.__razaoSocial

    def verificarCnpj(self):
        print("CNPJ:",self.cnpj)

    def __str__(self):
        return super().__str__()+"\nCNPJ: {}\nRazão Social: {}\n".format(self.cnpj,self.razaoSocial)

Antonio=ClienteFisico(84932,"Rua 7 de setembro","Antônio",123456789012)
Antonio.localizarEndereco()
Antonio.verificarCpf()
print(Antonio)

Maria=ClienteJuridico(24869,"Rua 10 de outubro",12345678000143,"Maria Comércio Ltda")
Maria.localizarEndereco()
Maria.verificarCnpj()
print(Maria)