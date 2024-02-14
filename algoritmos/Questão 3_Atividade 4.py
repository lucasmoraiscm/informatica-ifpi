#leer varias edades y imprimir el nombre y edad igual o mayores que 40. (Si haber ninguna imprimir:"Nenhuma idade igual ou maior a 40 anos.".)
maiorIgual40=" "
seta="--> "
com=" com "
while True:
    nome=input("Digite o nome:")
    idade=int(input("Digite a idade:"))
    if idade>=40:
        maiorIgual40=maiorIgual40+seta+nome+com+str(idade)
        print("Tem 40 anos ou mais",maiorIgual40)
    if idade<40 and maiorIgual40!=" ":
        print("Tem 40 anos ou mais",maiorIgual40)
    if maiorIgual40==" ":
        print("Nenhuma idade igual ou maior a 40 anos.")
    opc=input("""Deseja continuar?
S-Sim   N-Não:""")
    if opc.upper()=="N":
        break