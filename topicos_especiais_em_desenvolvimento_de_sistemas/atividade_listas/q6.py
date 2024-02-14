media = []
quant = 0
for i in range(10):
    notas = str(input("Digite as 4 notas do aluno (ex: 7-7-7-7):"))
    n = notas.split("-")
    n1 = n[0]
    n2 = n[1]
    n3 = n[2]
    n4 = n[3]
    calc = (float(n1) + float(n2) + float(n3) + float(n4)) / 4
    media.append(calc)
    if calc >= 7:
        quant += 1
print(quant)