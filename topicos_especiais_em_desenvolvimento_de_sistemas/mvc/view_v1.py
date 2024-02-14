from model_v1 import Aluno
from dao_v1 import AlunoDao

while True:
    try:
        opc = int(input("\n1-Salvar aluno(a)\n2-Ver alunos(as) salvos(as)\n3-Sair\nDigite a opção desejada:"))

        if opc == 1:
            nome = input("\nDigite o nome do(a) aluno(a):")
            idade = int(input("Digite a idade do(a) aluno(a):"))
            cpf =input("Digite o CPF do(a) aluno(a):")

            if len(nome) > 2 and (idade > 0 and idade < 150) and len(cpf) == 11:
                aluno1 = Aluno(nome,idade,cpf)
                AlunoDao.salvar(aluno1)
            else:
                print("Dados inválidos!\nVerifique os dados e tente novamente!")

        if opc == 2:
            AlunoDao.ler()

        if opc == 3:
            break
    except:
        print("Ação inaválido!\nTente novamente!")
