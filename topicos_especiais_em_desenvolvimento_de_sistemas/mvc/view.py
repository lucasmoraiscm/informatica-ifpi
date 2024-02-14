from controller import *

while True:
    try:
        opc = int(input("\n1-Salvar aluno(a)\n2-Ver alunos(as) salvos(as)\n3-Sair\nDigite a opção desejada:"))
        if opc == 1:
            nome = input("\nDigite o nome do(a) aluno(a):")
            idade = int(input("Digite a idade do(a) aluno(a):"))
            cpf = input("Digite o CPF do(a) aluno(a):")
            if AlunoController.salvar(nome, idade, cpf):
               print("Aluno(a) cadastrado(a) com sucesso!")
            else:
               print("Dados inválidos!\nTente novamente!")

        if opc == 2:
            AlunoController.ler()

        if opc == 3:
            break
    except:
        print("Ação inaválida!\nTente novamente!")
