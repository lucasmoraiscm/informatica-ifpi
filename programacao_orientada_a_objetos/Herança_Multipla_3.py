class Primeiro():
    def __init__(self):
        print("Primeiro...")
        super().__init__()

class Segundo():
    def __init__(self):
        print("Segundo...")
        super().__init__()

class Terceiro(Segundo,Primeiro):
    def __init__(self):
        print("terceiro...")

obj3 = Terceiro()