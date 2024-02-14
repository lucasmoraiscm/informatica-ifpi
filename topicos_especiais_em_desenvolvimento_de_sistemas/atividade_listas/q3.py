from tracemalloc import Snapshot


t = []
sn = 0
for i in range(4):
    n =float(input("Digite a nota:"))
    t.append(n)
    sn += n
    m = sn/4
print(t, '\n', m)