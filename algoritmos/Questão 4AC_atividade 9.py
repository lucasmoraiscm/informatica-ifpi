#mostrar os dados das meninas e dos meninos#

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
print("Nota dos meninas:",meninas)
print("Nota dos meninos:",meninos)