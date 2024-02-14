#Dicionario de cpf's e nome de seus referentes donos#
dados={}
while True:
    cpf=input("Digite o CPF:")
    nome=input("Digite o nome:")
    dados[cpf]=nome
    resp=input("Deseja continuar? (S)-Continuar (N)-Sair:")
    if resp.upper()=="N":
        break