class Cachorro():
    def __init__(self):
        pass

    def Latir(self):
        print("Au au!")

class Pitbull(Cachorro):
    def __init__(self):
        super().__init__()

    def latir(self):
        super().Latir()
    
class Poodle(Cachorro):
    def __init__(self):
        super().__init__()

    def latir(self):
        super().Latir()

c1=Pitbull()
c1.latir()

c2=Poodle()
c2.latir()