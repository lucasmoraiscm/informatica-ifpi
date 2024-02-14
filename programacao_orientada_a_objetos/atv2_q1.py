class Data(object):
    def __init__(self,dia,mes,ano):
        self.dia=dia
        self.mes=mes
        self.ano=ano

    def __str__(self):
        return "Data: {}/{}/{}".format(self.dia,self.mes,self.ano)



d1=Data("24","8","2021")
print(d1)