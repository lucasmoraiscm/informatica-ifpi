class Pessoa:

    def __init__(self,nome,idade,peso,altura,sexo,estado="Vivo",estado_civil="Solteiro(a)",conjuge=None):
        self.__nome=nome
        self.__idade=idade
        self.__peso=peso
        self.__altura=altura
        self.__sexo=sexo
        self.__estado=estado
        self.__estado_civil=estado_civil
        self.__conjuge=conjuge

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        if self.__estado=="Vivo":
            return self.__idade
        else:
            print(self.__nome,"está morto(a).")

    @idade.setter
    def idade(self,idade=1):
        if idade==self.__idade:
            self.__idade=idade
        else:
            print("Sem permissão.")

    def envelhecer(self):
        if self.__estado=="Vivo":
            self.__idade+=1
            if self.__idade<21:
                self.__altura+=0.5
            print(self.__nome,"está com",self.__idade,"anos e",self.__altura,"cm de altura.")
        else:
            print(self.__nome,"está morto(a).")

    @property
    def peso(self):
        return self.__peso

    def engordar(self,valor=1):
        if self.__estado=="Vivo":
            self.__peso+=valor
            print("Peso atual:",self.__peso)
        else:
            print("Operação não realizada.",self.__nome,"está morta.")
    
    def emagrecer(self,valor=1):
        if self.__estado=="Vivo":
            self.__peso-=valor
            print("Peso atual:",self.__peso)
        else:
            print(self.__nome,"está morto(a).")

    @property
    def altura(self):
        return self.__altura
    
    def crescer(self,valor=1):
        if self.__estado=="Vivo":
            if self.__idade<=21:
                self.__altura+=valor
                print(self.__nome,"está com",self.__altura,"de altura.")
            else:
                print(self.__nome,"não pode mais crescer pois está com 21 anos ou mais.")
        else:
            print(self.__nome,"está morto(a).")

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def morrer(self,valor="Morto"):
        self.__estado=valor
        print(self.__nome,"Morreu.")
        if self.__estado_civil=="Casado(a)":
            nome_conjuge=self.__conjuge
            nome_conjuge.__estado_civil=="Viúvo(a)"
            nome_conjuge.__conjuge=None
            self.__estado_civil=None
            self.__conjuge=None

    @property
    def estado_civil(self):
        return self.__estado_civil

    def casar(self,nome_conjuge):
        if self.__estado=="Vivo":
            if self.__estado_civil=="Solteiro(a)" or self.__estado_civil=="Viúvo(a)":
                if self.__idade>=18:
                    if nome_conjuge.estado=="Vivo":
                        if nome_conjuge.estado_civil=="Solteiro(a)" or nome_conjuge.estado_civil=="Viúvo(a)":
                            if nome_conjuge.idade>=18:
                                self.__estado_civil=="Casado(a)"
                                self.__conjuge=nome_conjuge
                                print(self.__nome,"está casado(a) com",nome_conjuge.__nome)
                            else:
                                print("Casamento não permitido.",nome_conjuge.__nome,"é de menor.")
                        else:
                            ("Casamento não realizado",nome_conjuge.__nome,"está casado(a).")
                    else:
                        print("Casamento não realizado.",nome_conjuge.__nome,"está morto(a).")
                else:
                    print("Casamento não peritido.",self.__nome,"é de menor.")
            else:
                print("Casamento não realizado.",self.__nome,"é casado.")
        else:
            print("Casamento não realizado.",self.__nome,"está morto(a).")

    @property
    def conjuge(self):
        return self.__conjuge

maria=Pessoa("Maria",5,20,100,"F")
joão=Pessoa("João",12,40,140,"M")
pedro=Pessoa("Pedro",22,65,170,"M")
bia=Pessoa("Bia",18,55,160,"F")
julia=Pessoa("Júlia",30,65,170,"F")
carlos=Pessoa("Carlos",2,11,80,"M")
jonas=Pessoa("Jonas",34,70,180,"M")

maria.idade=10 #a)
maria.envelhecer() #b)
pedro.crescer(2) #c)
bia.casar(carlos) #d)
pedro.casar(maria) #e)
pedro.casar(julia) #f)
pedro.casar(bia) #g)
maria.morrer=() #h)
maria.engordar() #i)
bia.casar(jonas) #j)
bia.morrer=() #k)
pedro.morrer=() #l)
jonas.casar(julia) #m)
pedro.casar(bia) #n)
print(pedro.idade) #o)
joão.idade=50 #p)