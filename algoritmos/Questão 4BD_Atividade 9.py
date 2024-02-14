#Mostrar as meninas e os meninos aprovados#

"""
turma=[]
meninas=[]
meninasAprovadas=[]
meninos=[]
meninosAprovados=[]
alunosAprovados=[]

while True:
    nome=input("Digite o nome:")
    sexo=input("F-Feminino M-Masculino:").upper()
    nota=float(input("Nota:"))
    if sexo=="F":
        meninas.append([nome,nota])
        if nota>=7:
            meninasAprovadas.append([nome,nota])
    elif sexo=="M":
        meninos.append([nome,nota])
        if nota>=7:
            meninosAprovados.append([nome,nota])
    else:
        print("Sexo inválido!!..",end=" ")
    resp=input("Deseja continuar (S-Sim N-Não)?:")
    if resp.upper()=="N":
        break

turma.append(meninas)
turma.append(meninos)
alunosAprovados.append(meninasAprovadas)
alunosAprovados.append(meninosAprovados)

print("Nota de todos os alunos:",turma)
print("Nota das meninas:",meninas)
print("Nota dos meninos:",meninos)
print("Todos os alunos aprovados:",alunosAprovados)
print("Meninas aprovadas:",meninasAprovadas)
print("Meninos aprovadas:",meninosAprovados)
"""

turma=[]
meninas=[]
meninasAprovadas=[]
meninos=[]

while True:
    nome=input("Digite o nome:")
    sexo=input("F-Feminino M-Masculino:").upper()
    nota=float(input("Nota:"))
    if sexo=="F":
        meninas.append([nome,nota])
        if nota>=7:
            meninasAprovadas.append([nome,nota])
    elif sexo=="M":
        meninos.append([nome,nota])
    else:
        print("Sexo inválido!!..",end=" ")
    resp=input("Deseja continuar (S-Sim N-Não)?:")
    if resp.upper()=="N":
        break

turma.append(meninas)
turma.append(meninos)

print("Meninas aprovadas:",meninasAprovadas)