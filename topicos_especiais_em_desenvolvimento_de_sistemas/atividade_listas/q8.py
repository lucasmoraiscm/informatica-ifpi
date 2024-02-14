idade = []
altura = []
for i in range(5):
    ida = int(input("Digite a idade da pessoa:"))
    alt = float(input("Digite a altura da pessoa:"))
    idade.append(ida)
    altura.append(alt)
idade.reverse()
altura.reverse()
print(idade, "\n", altura)