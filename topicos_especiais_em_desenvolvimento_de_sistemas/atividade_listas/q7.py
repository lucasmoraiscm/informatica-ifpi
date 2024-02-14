t = []
s = []
m = []
for i in range(5):
    n = int(input("Digite o número:"))
    t.append(n)
calcs = t[0] + t[1] + t[2] + t[3] + t[4]
s.append(calcs)
calcm = t[0] * t[1] * t[2] * t[3] * t[4]
m.append(calcm)
print(s, '\n', m, '\n', t)