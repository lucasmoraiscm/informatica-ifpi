matriz=[[0,0],[0,0]]
lista=[]
for l in range(0,2):
    for c in range(0,2):
        matriz[l][c]=float(input(f'Digite um número para [{l},{c}]:'))
        v=matriz[l][c]
        lista.append(v)

v1=lista[0]
v2=lista[1]
v3=lista[2]
v4=lista[3]

matriz2=[[(v1/v4),(v2/v3)],[(v3/v2),(v4/v1)]]
for l2 in range(0,2):
    print(matriz2[l2])