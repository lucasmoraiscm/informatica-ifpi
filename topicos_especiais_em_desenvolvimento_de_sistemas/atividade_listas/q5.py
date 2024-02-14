t = []
p = []
i = []
for x in range(20):
    n = int(input("Digite o número:"))
    t.append(n)
    if n%2 == 0:
        p.append(n)
    else:
        i.append(n)
print(t, '\n', p, '\n', i)