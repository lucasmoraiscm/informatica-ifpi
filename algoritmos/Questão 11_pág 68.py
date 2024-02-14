#Ler 20 números, depois receber a entrada de um número e informar se ele está na lista(se estiver, dizer a quantidade)
lista=[]
for x in range(20):
    n=int(input("Digite o número:"))
    lista.append(n)
while True:
    ver=int(input("Digite o número a ser verificado:"))
    if lista.count(ver)==1:
        q=lista.count(ver)
        print("O número está na lista",q,"vez")
    elif lista.count(ver)>1:
        q=lista.count(ver)
        print("O número está na lista",q,"vezes")
    else:
        print("O número não está na lista")