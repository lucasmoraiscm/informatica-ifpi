""" ORIGINAL

turma={}
while True:
    nome=input("Digite o nome:")
    sexo=input("F-feminino M-Masculino").upper()
    nota=float(input("Nota:"))
    if sexo=="F":
        turma[0].append([nome,nota])
    elif sexo=="M":
        turma[1].append([nome,nota])
    else:
        print("Sexo inválido!!..",end=" ")
    resp=input("Deseja continuar (S-sim N-não)?")
    if resp.upper()=="N":
        break

"""

turma=[]
meninas=[]
meninos=[]

while True:
    nome=input("Digite o nome:")
    sexo=input("F-Feminino M-Masculino:").upper()
    nota=float(input("Nota:"))
    if sexo=="F":
        meninas.append([nome,nota])
    elif sexo=="M":
        meninos.append([nome,nota])
    else:
        print("Sexo inválido!!..",end=" ")
    resp=input("Deseja continuar (S-Sim N-Não)?:")
    if resp.upper()=="N":
        break

turma.append(meninas)
turma.append(meninos)
print(turma)
print(meninas)
print(meninos)