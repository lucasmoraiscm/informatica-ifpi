perg = [
    ["Telefonou para a vítima?"],
    ["Esteve no local do crime?"],
    ["Mora perto da vítima?"],
    ["Devia para a vítima?"],
    ["Já trabalhou com a vítima?"]
]
resp = []
p = 0
c = 0

for i in range(5):
    print(perg[p])
    p += 1
    r = str(input("Digite S para sim e N para não:"))
    resp.append(r)

for v in resp:
    if v == "S":
        c += 1
    
if c == 2:
    print("Suspeita")
elif c == 3 or c == 4:
    print("Cúmplice")
elif c == 5:
    print("Assassino")
else:
    print("Inocente")
