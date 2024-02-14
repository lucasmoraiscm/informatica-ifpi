from dao import*

cpf = input("cpf:")

def verificar():
    v = AlunoDao.ler()
    for x in v:
        if x.cpf == cpf:
            return("CPF encontrado")
        else:
            return("CPF não encontrado")

print(verificar())