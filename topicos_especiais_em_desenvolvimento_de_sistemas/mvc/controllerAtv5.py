from dao import*

class AlunoController:
    @classmethod
    def cadastrar(cls, nome, idade, cpf):
        if len(nome) > 2 and 0 < int(idade) < 180 and len(cpf) == 11:
            try:
                AlunoDao.salvar(Aluno(nome, idade, cpf))
                return "Operação realizada com sucesso"
            except:
                return "Não foi possível efetuar a gravação dos dados"
        if len(nome) < 2:
            return "Valor de nome inválido"
        if int(idade) < 0 or int(idade) > 180:
            return "Valor de idade inválido"
        if len(cpf) != 11:
            return "Valor de CPF inválido"

    @classmethod
    def visualizar(cls):
        l = AlunoDao.ler()
        for i in l:
            print("Nome:" + i.nome + " - Idade:" + str(i.idade) + " - CPF:" + i.cpf)
