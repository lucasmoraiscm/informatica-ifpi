while True:
    numero=int(input("Digite um número:"))
    if numero>0:
        res=numero**0.5
        print(res)
    elif numero<0:
        print("Digite um número positivo!!!")
    else:
        break
    
