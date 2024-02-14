l1 = []
l2 = []
l3 = []
l4 = []
n = 0
for i in range(10):
    v1 = input("Digite o elemento do vetor 1: ")
    v2 = input("Digite o elemento do vetor 2: ")
    v3 = input("Digite o elemento do vetor 3: ")
    l1.append(v1)
    l2.append(v2)
    l3.append(v3)
    l4.append(l1[n])
    l4.append(l2[n])
    l4.append(l3[n])
    n += 1
print(l1, '\n', l2, '\n', l3, '\n', l4)