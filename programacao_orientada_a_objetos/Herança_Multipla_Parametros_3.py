"""class Primeiro():
    def __init__(self,primeiro,**dicionario):
        print("Primeiro...")
        self.primeiro = primeiro
        super().__init__(**dicionario)    

class Segundo():
    def __init__(self,segundo,**dicionario):    
        print("Segundo...")
        self.segundo = segundo
        super().__init__(**dicionario)       

class Terceiro(Primeiro,Segundo):
    def __init__(self):        
        super(Terceiro,self).__init__(primeiro,segundo)     
        print("terceiro...")

obj = Terceiro(1,2)
print(Terceiro.mro())"""

class Primeiro():
    def __init__(self,primeiro,**dicionario):
        print("Primeiro...")
        self.primeiro = primeiro
        super().__init__(**dicionario)    

class Segundo():
    def __init__(self,segundo,**dicionario):    
        print("Segundo...")
        self.segundo = segundo
        super().__init__(**dicionario)       

class Terceiro(Primeiro,Segundo):
    def __init__(self,primeiro,segundo): #        
        super(Terceiro,self).__init__(primeiro=primeiro,segundo=segundo) #     
        print("terceiro...")

obj = Terceiro(1,2)
print(Terceiro.mro())