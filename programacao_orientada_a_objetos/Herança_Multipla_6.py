class Primeiro():
    def __init__(self):
        super().__init__()
        print("Primeiro...")

class Segundo():
    def __init__(self):
        super().__init__()
        print("Segundo...")

class Terceiro(Segundo,Primeiro):
    def __init__(self):
        super(Terceiro,self).__init__()
        print("terceiro...")

obj6 = Terceiro()