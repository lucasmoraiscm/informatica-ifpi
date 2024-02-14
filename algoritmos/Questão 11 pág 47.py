#Ler as notas de um aluno e calcular a média(imprimir média e maior nota)#
for i in range(1,2):
    nota1=float(input("Digite sua nota:"))
    nota2=float(input("Digite sua nota:"))
    maiorNota=nota1
    media=nota1+nota2
    m=2
    d=3
    if nota2>maiorNota:
        maiorNota=nota2
    if nota1>=0 and nota2>=0:
        media=media/2
    if nota1<0:
        media=nota2
    if nota2<0:
        media=nota1
    if nota1<0 and nota2<0:
        media=0
    print("Sua média á",media)
    print("Sua maior nota é",maiorNota)
while True:
    notaAtual=float(input("Digite sua nota:"))
    if notaAtual>maiorNota:
        maiorNota=notaAtual
    if notaAtual>=0 and notaAtual<=10:
        media=media*m
        media=media+notaAtual
        media=media/d
    if nota1<0 or nota2<0:
        media=media*(m-1)
        media=media+notaAtual
        media=media/(d-1)
    if nota1<0 and nota2<0:
        media=0
        media=media+notaAtual
        media=media/(d-2)
    if notaAtual<0:
        media=media*(m-1)
        media=nota1+nota2
        media=media/(d-1)
    print("Sua média é",media)
    print("Sua maior nota é",maiorNota)
    m+=1
    d+=1
