class Primeiro():
    def __init__(self):
        print("Primeiro...")
        super().__init__()

class Segundo():
    def __init__(self):
        print("Segundo...")
        super().__init__()

class Terceiro(Primeiro,Segundo):
    def __init__(self):
        print("Terceiro...")
        super(Terceiro,self).__init__()

obj = Terceiro()