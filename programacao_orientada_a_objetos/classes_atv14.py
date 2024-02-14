from datetime import *
class Pessoa:
    def __init__(self,cpf,nome,data,comorbidades=None,descrição_comorbidade=None):
        self.__cpf = cpf
        self.nome = nome
        self.__data_nascimento = datetime.strptime(data,"%d/%m/%Y")
        self.__comorbidades=[]
        self.__descriçãoComorbidade=[]
        encontrou=False
        for i in Comorbidade.comorbidade:
            if i==comorbidades:
                encontrou=True
                self.__comorbidades.append(comorbidades)
                self.__descriçãoComorbidade.append(descrição_comorbidade)
        if encontrou==False:
            self.__comorbidades=None
            raise ValueError

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_nascimento(self):
        return  self.__data_nascimento

    @property
    def comorbidades(self):
        return self.__comorbidades
    
    @property
    def descriçãoComorbidade(self):
        return self.__descriçãoComorbidade

    def getIdade(self):
        hoje = date.today()
        y = hoje.year - self.__data_nascimento.year
        if hoje.month < self.__data_nascimento.month or hoje.month == self.__data_nascimento.month and hoje.day < self.__data_nascimento.day:
            y -= 1
        return y
    
    def novaComorbidade(self,comorbidades,descrição_comobidade):
        encontrou=False
        for i in Comorbidade.comorbidade:
            if i==comorbidades:
                encontrou=True
                self.__comorbidades.append(comorbidades)
                self.__descriçãoComorbidade.append(descrição_comobidade)
        if encontrou==False:
            self.__comorbidades=None
            return "Ação não realizada! Comorbidade inválida"

    def __str__(self):
        return "CPF:{}\nNome:{}\nData de nascimento:{}\nComorbidades:{}\nDescrição da comorbidade:{}".format(self.cpf,self.nome,self.data_nascimento,self.comorbidades,self.descriçãoComorbidade)

class VacinaCovid:
    def __init__(self,numero,local,tipo,data_dose1,pessoa):
        self.__num_registro = numero
        self.local = local
        self.tipo = tipo
        self.__data_dose1 = data_dose1
        self.__data_dose2 = None
        if type(pessoa)==Pessoa:
            self.__pessoa = pessoa
            RelatorioVacinação.vacinados.append(pessoa)
            idade=pessoa.getIdade()
            if idade>40:
                RelatorioVacinação.vacinadosComorbidade40.append(pessoa)
        else:
            raise ValueError

    @property
    def num_registro(self):
        return self.__num_registro

    @property
    def data_dose1(self):
        return self.__data_dose1

    @property
    def data_dose2(self):
        return self.__data_dose2
    
    @property
    def pessoa(self):
        return self.__pessoa

    def vacinar2dose(self,data):
        data=datetime.strptime(data,"%d/%m/%Y")
        data_dose1=datetime.strptime(self.data_dose1,"%d/%m/%Y")
        m=data.month-data_dose1.month
        if m==2 and data.day==data_dose1.day:
            self.__data_dose2=data
            print("2a dose cadastrada com sucesso!")
        else:
            print("Ação não realizada! Data diferente da data prevista para 2a dose")
    
    def __str__(self):
        return "Número de registro:{}\nLocal:{}\nTipo:{}\nData 1a dose:{}\nData 2a dose:{}".format(self.num_registro,self.local,self.tipo,self.data_dose1,self.data_dose2)

class ControleVacina:
    def __init__(self):
        self.registroDeVacinas = []

    def incluirVacina(self,vacina):
        if type(vacina)==VacinaCovid:
            self.registroDeVacinas.append(vacina)
            print("Registro de Vacina cadastrado com sucesso!")
        else:
            print("Erro! Não foi possível cadastrar a informação.")

    def incluir2doseVacina(self,num_registro,data):
        achou = False
        for i in self.registroDeVacinas:
            if i.num_registro == num_registro:
                achou=True
                i.vacinar2dose(data)
            else:
                print("Ação não realizada! Data diferente da data prevista para 2a dose")
        if achou==False:
            print("Registro com a 1a vacinação não encontrada!")

class Comorbidade:
    comorbidade=["Diabetes","Hipertensão","Pneumopatia","Imunossuprimido","Síndrome de Down","Obesidade mórbida","Cirrose hepática","Transplantado","Doença neurológica crônica","Doença cerebrovascular","Doença renal crônica",]

class RelatorioVacinação:
    vacinados=[]
    vacinadosComorbidade40=[]
    
    def relatorioComorbidade40(self):
        t40=len(self.vacinadosComorbidade40)
        t=len(self.vacinados)
        tporcentagem=(t40*100)/t
        print("Total de vacinados com comorbidades:",t)
        print("Total de vacinados com comorbidades acima de 40 anos:",t40)
        print("Porcentagem de vacinados com comorbidade acima de 40 anos: {}%".format(round(tporcentagem,2)))