#Lê 3 idades, fazer a média delas e imprimir uma mensagem de acordo com a senguinte tabela:#
#M>40, 25<M<=40 e M<=25#
idade1=int(input("Digite a idade:"))
somaIdades=idade1
for i in range(2):
    idades2e3=int(input("Digite a idade:"))
    somaIdades=somaIdades+idades2e3
    media=somaIdades/3
if media>40:
    print("Média acima de 40 anos")
elif media>25 and media<=40:
    print("Média entre 25 e 40 anos")
elif media<=25:
    print("Média menor ou igual a 25 anos")
