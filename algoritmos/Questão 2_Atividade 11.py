dados={}
while True:
    nome=input("Digite o nome:")
    idade=input("Digite a idade:")
    telefone=input("Digite o telefone:")
    dados[nome]=nome,idade,telefone
    resp1=input("Deseja continuar? (S)-Continuar (N)-Sair:")
    if resp1.upper()=="N":
        while True:
            verificação=input("Digite o nome a ser verificado:")
            if verificação in dados:
                print(dados[verificação])
                resp2=input("Tem certeza que quer apagar essa informação? (S)-Sim (N)-Não:")
                if resp2.upper()=="S":
                    del dados[verificação]
                    print("As informações foram apagadas!")
            else:
                print("O nome não existe na lista!")