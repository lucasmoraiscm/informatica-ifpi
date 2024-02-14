#Ler e adicionar ao dicionario nome, idade e telefone. Ler até quando o usuário desejar. Procurar e imprimir o nome no dicionario.#
dados={}
while True:
    nome=input("Digite o nome:")
    idade=input("Digite a idade:")
    telefone=input("Digite o telefone:")
    dados[nome]=nome,idade,telefone
    resp=input("Deseja continuar? (S)-Continuar (N)-Sair:")
    if resp.upper()=="N":
        while True:
            verificação=input("Digite o nome a ser verificado:")
            if verificação in dados:
                print(dados[verificação])
            else:
                print("O nome não existe na lista!")