#Dicionario de cpf's e nome de seus referentes donos, fazer a verificação e apagar o cpf#
dados={}
while True:
    cpf=input("Digite o CPF:")
    nome=input("Digite o nome:")
    dados[cpf]=nome
    resp=input("Deseja continuar? (S)-Continuar (N)-Sair:")
    if resp.upper()=="N":
        while True:
            verificação=input("Digite o CPF a ser verificado:")
            if verificação in dados:
                del dados[verificação]
                print("O CPF foi apagado!")
            else:
                print("O CPF não existe na lista!")