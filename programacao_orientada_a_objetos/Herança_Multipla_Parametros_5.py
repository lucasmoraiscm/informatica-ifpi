"""class Primeiro():
    def __init__(self,primeiro,*lista**dicionario):
        print("Primeiro...")
        self.primeiro = primeiro
        super().__init__(*lista,**dicionario)    

class Segundo():
    def __init__(self,segundo,*lista,**dicionario):    
        print("Segundo...")
        self.segundo = segundo
        super().__init__(*lista,**dicionario)       

class Terceiro(Primeiro,Segundo):
    def __init__(self):        
        super(Terceiro,self).__init__(primeiro,segundo)     
        print("terceiro...")

obj = Terceiro(1,2)
print(Terceiro.mro())"""

class Primeiro():
    def __init__(self,primeiro,*lista,**dicionario): #
        print("Primeiro...")
        self.primeiro = primeiro
        super().__init__(*lista,**dicionario)    

class Segundo():
    def __init__(self,segundo,*lista,**dicionario):    
        print("Segundo...")
        self.segundo = segundo
        super().__init__(*lista,**dicionario)       

class Terceiro(Primeiro,Segundo):
    def __init__(self,primeiro,segundo): #        
        super(Terceiro,self).__init__(primeiro,segundo)     
        print("terceiro...")

obj = Terceiro(1,2)
print(Terceiro.mro())