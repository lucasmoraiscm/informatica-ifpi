from classes_Seguro import*;

class ControleDeSeguros:
    def __init__(self):
        self.seguros=[]
        self.valorTotal=0
        self.totalSegurosVida=0
        self.totalSegurosAutomóveis=0

    def cadastrarSeguro(self,seguro):
        if isinstance(seguro,Seguro):
            self.seguros.append(seguro)
            self.valorTotal+=seguro.calculaValor()
            if type(seguro)==SeguroVida:
                self.totalSegurosVida+=1
            elif type(seguro)==SeguroAutomóvel:
                self.totalSegurosAutomóveis+=1
            print("Seguro cadastrado com sucesso!")
        else:
            print("Ação não realizada! Seguro inválido")
    
    def relatorio(self):
        for i in self.seguros:
            print(i)
        print("Seguros de vida:",self.totalSegurosVida)
        print("Seguros de automóveis:",self.totalSegurosAutomóveis)
        print("Total dos valores:",self.valorTotal)
