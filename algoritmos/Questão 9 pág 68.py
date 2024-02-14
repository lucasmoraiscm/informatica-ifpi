"ler notas de 10 alunos e imprimir a nota da sala"
nota=[]
for i in range(10):
    notaAluno=int(input("Digite a nota:"))
    nota.append(notaAluno)
somaNotas=nota[0]+nota[1]+nota[2]+nota[3]+nota[4]+nota[5]+nota[6]+nota[7]+nota[8]+nota[9]
notaSala=somaNotas/10
print("A nota da sala é",notaSala)