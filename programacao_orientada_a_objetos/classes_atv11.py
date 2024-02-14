from datetime import date
data_atual=date.today()

class Vacina_covid19:
	def __init__(self,numero_registro,local,tipo):
		self.__numero_registro=numero_registro
		self.__local=local
		self.__tipo=tipo
		self.__data_1a_dose=None
		self.__data_2a_dose=None
	
	@property
	def numero_registro(self):
		return self.__numero_registro
	
	@property
	def local(self):
		return self.__local
	
	@property
	def tipo(self):
		return self.__tipo
		
	@property
	def data_1a_dose(self):
		return self.__data_1a_dose
	
	def atualizar_data_1a_dose(self):
		self.__data_1a_dose=data_atual

	@property
	def data_2a_dose(self):
		return self.__data_2a_dose
	
	def atualizar_data_2a_dose(self,ano,mes,dia):
		self.__data_2a_dose=date(ano,mes,dia)
	
	def __str__(self):
		return "Número de registro:{}\nLocal:{}\nTipo:{}\nData 1a dose:{}\nData 2a dose:{}".format(self.__numero_registro,self.__local,self.__tipo,self.__data_1a_dose,self.__data_2a_dose)

class Pessoa:
	def __init__(self,cpf,nome,dia,mes,ano,possui_comorbidade=False,descricao_comorbidade=None,vacinaCovid=None):
		self.__cpf=cpf
		self.__nome=nome
		self.__data_nascimento=date(ano,mes,dia)
		self.__possui_comorbidade=possui_comorbidade
		self.__descricao_comorbidade=descricao_comorbidade
		self.__vacinaCovid=vacinaCovid
		self.__idade=None

	@property
	def cpf(self):
		return self.__cpf
			
	@property
	def nome(self):
		return self.__nome
			
	@property
	def data_nascimento(self):
		return self.__data_nascimento
			
	@property
	def possui_comorbidade(self):
		return self.__possui_comorbidade
			
	@property
	def descricao_comorbidade(self):
		return self.__descricao_comorbidade
			
	@property
	def vacinaCovid(self):
		return self.__vacinaCovid
	
	@property
	def idade(self):
		return self.__idade

	def getidade(self):
		self.__idade=data_atual.year-self.data_nascimento.year-((data_atual.month,data_atual.day)<(self.data_nascimento.month,self.data_nascimento.day))

	def vacinar1aDose(self,vacina):
		self.getidade()
		if self.__idade>=60 or self.__idade>=18 and self.__possui_comorbidade==True:
			if vacina.data_1a_dose==None:
				if type(vacina)==Vacina_covid19:
					self.__vacinaCovid=vacina
					vacina.atualizar_data_1a_dose()
					print("A pessoa foi vacinada com a 1a dose!")
				else:
					print("Ação não realizada! Vacina inválida")
			else:
				print("Ação não realizada! A pessoa não pode tomar a 1a dose dessa vacina")
		else:
			print("Ação não realizada! A pessoa não faz parte do grupo de prioridades ou não possui comorbidade")
	
	def vacinar2aDose(self,vacina,dia,mes,ano):
		self.getidade()
		if self.__vacinaCovid!=None:
			if vacina.data_2a_dose==None:
				if type(vacina)==Vacina_covid19:
					vacina.atualizar_data_2a_dose(ano,mes,dia)
					print("A pessoa foi vacinada com a 2a dose!")
				else:
					print("Ação não realizada! Vacina inválida")
			else:
				print("Ação não realizada! A pessoa não pode tomar a 2a dose dessa vacina")
		else:
			print("Ação não realizada! A pessoa precisa ainda tomar a 1a dose")

	def __str__(self):
		return "CPF:{}\nNome:{}\nData de nascimento:{}\nPossui comorbidade:{}\nDescrição comorbidade:{}\nVacina covid-19:{}".format(self.__cpf,self.__nome,self.__data_nascimento,self.__possui_comorbidade,self.__descricao_comorbidade,self.__vacinaCovid)