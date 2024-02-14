from controllerAtv5 import AlunoController
from controllerAtv5 import *

while True:
    try: 
        x = int(input('Digite: 1 - Cadastrar  2 - Visualizar  3 - Sair: '))
        if x == 1:
            nome = input("Digite o nome do aluno:")
            idade = int(input("Digite a idade do aluno:"))
            cpf =input("Digite o cpf do aluno:")
            print(AlunoController.cadastrar(nome, idade, cpf))
        if x == 2:
            AlunoController.visualizar()
        if x == 3:
            break
    except:
        print("Ação inválida! Tente novamente")
