"ler o nome de 10 pessoas e depois verificar se a pessoa informda pelo usuário estar presente na grupo"
pessoa=[]
for i in range(10):
	nome=input("Digite o nome da pessoa (máx. 10 letras):")
	pessoa.append(nome)
while True:
	nomeVeri=input("Qual o nome da pessoa a ser verificada:")
	if pessoa.count(nomeVeri)>0:
		print("A pessoa está incluída no grupo")
	else:
		print("A pessoa não está incluída no grupo")