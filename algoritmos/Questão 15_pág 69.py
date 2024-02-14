matriz=[]
cont=11
for i in range(3):
    matriz.append([])    
    for j in range(4):
        matriz[i].append(cont)
        cont=cont+1
    
for i in range(3):
    print("\n")
    for j in range(4):
        print(matriz[i][j],end=" ")