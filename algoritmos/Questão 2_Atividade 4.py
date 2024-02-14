#leer 10 nombres y edades y imprimir las mayores de 18 años (si no tenga  ninguna, imprimir "Nenhuma maior de 18 anos.")
maior18=" "
seta="--> "
com=" com "
for i in range(10):
    nome=input("Digite o nome:")
    idade=int(input("Digite idade:"))
    if idade>18:
        maior18=maior18+seta+nome+com+str(idade)
        print("Tem mais de 18 anos",maior18)
    if idade<18 and maior18!=" ":
        print("Tem mais de 18 anos",maior18)
    if maior18==" ":
        print("Nenhum maior de 18 anos.")