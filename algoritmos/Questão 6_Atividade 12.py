n1=int(input("Digite o primeiro número:"))
n2=int(input("Digite o segundo número:"))
def maior(n1,n2):
    if n1>n2:
        print("O número", n1,"é maior!")
    elif n2>n1:
        print("O número", n2,"é maior!")
    else:
        print("Os números são iguais!")
maior(n1,n2)