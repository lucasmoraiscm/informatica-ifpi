from dao import *

class AlunoController:
    @classmethod
    def salvar(cls, nome, idade, cpf):
        if len(nome) > 2 and (idade > 0 and idade < 150) and len(cpf) == 11:
            aluno1 = Aluno(nome, idade, cpf)
            AlunoDao.salvar(aluno1)
            return True
        else:
            return False
    
    @classmethod
    def ler(cls):
        l = AlunoDao.ler()
        for i in l:
            print("Nome:"+i.nome+" - Idade:"+str(i.idade)+" - CPF:"+i.cpf)
