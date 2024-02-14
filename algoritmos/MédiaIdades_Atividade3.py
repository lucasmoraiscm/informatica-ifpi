#receber idades, imprimir a média e perguntar se o usuário deseja continuar#
idade=int(input("Digite a idade:"))
contIdades=1
somaIdades=idade
while True:
    media=somaIdades/contIdades
    if media>40:
        print("Média acima de 40 anos")
    elif media>25 and media<=40:
        print("Média entre 25 e 40 anos")
    elif media<=25:
        print("Média menor ou igual a 25 anos")
    resp=int(input("""Deseja continuar?
1-Sim   2-Não:"""))
    if resp==1:
        contIdades+=1
        idade=int(input("Digite a idade:"))
        somaIdades=somaIdades+idade
    else:
        break
