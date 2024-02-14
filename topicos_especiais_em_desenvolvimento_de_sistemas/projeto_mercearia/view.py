from controller import *

while True:
    try:
        opc = int(input("\n1-Salvar Produto\n2-Salvar Cliente\n3-Sair\nDigite a opção desejada:"))
        if opc == 1:
            nome = input("\nDigite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quant = int(input("Digite a quantidade do produto: "))
            id = input("Digite o ID do produto: ")
            if ProdutoController.salvar(nome, preco, quant, id):
                print("Produto salvo com sucesso!")
            else:
                print("Dados inválidos!\nTente novamente!")
        
        if opc == 2:
            nome = input("\nDigite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            num = input("Digite o número do cliente: ")
            if ClienteController.salvar(nome, cpf, num):
                print("Cliente salvo(a) com sucesso!")
            else:
                print("Dados inválidos!\nTente novamente!")
        
        if opc == 3:
            break
    except:
        print("Ação inválida!\nTente novamente!")
