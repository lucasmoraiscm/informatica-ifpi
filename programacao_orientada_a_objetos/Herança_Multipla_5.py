class Primeiro():
    def __init__(self):
        print("Primeiro...")

class Segundo():
    def __init__(self):
        print("Segundo...")
        super().__init__()

class Terceiro(Segundo,Primeiro):
    def __init__(self):
        print("terceiro...")
        super(Terceiro,self).__init__()

obj5 = Terceiro()