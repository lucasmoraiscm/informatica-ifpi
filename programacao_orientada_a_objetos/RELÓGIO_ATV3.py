class Relógio:

    def __init__(self):
        self.bateria=False
        self.ligado=False
        self.horas=0
        self.horas_min=0
        self.horas_max=23
        self.minutos=0
        self.minutos_min=0
        self.minutos_max=59
    
    def colocar_bateria(self):
        self.bateria=True
        print("O relógio está com bateria!")
    
    def retirar_bateria(self):
        self.bateria=False
        print("O relógio está sem bateria!")
    
    def ligar(self):
        if self.bateria:
            self.ligado=True
            print("O relógio está ligado!")
        else:
            print("Operação não realizada. O relógio está sem bateria!")
    
    def desligar(self):
        self.ligado=False
        print("O relógio está desligado!")

    def alterar_horas(self,valor):
        if self.bateria:
            if self.ligado:
                if valor in range(self.horas_min,self.horas_max+1):
                    self.horas=valor
                    print("Horas alterada para:",self.horas,"horas")
                else:
                    print("Operação não realizada. Horas inválidas!")
            else:
                print("Operação não realizada. O relógio está desligado!")
        else:
            print("Operação não realizada. O relógio está sem bateria!")
    
    def alterar_minutos(self,valor):
        if self.bateria:
            if self.ligado:
                if valor in range(self.minutos_min,self.minutos_max+1):
                    self.minutos=valor
                    print("Minutos alterados para:",self.minutos,"minutos")
                else:
                    print("Operação não realizada. Minutos inválidos!")
            else:
                print("Operação não realizada. O relógio está desligado!")
        else:
            print("Operação não realizada. O relógio está sem bateria!")
    
    def mostrar_horario(self):
        if self.bateria:
            if self.ligado:
                print("Horário:",self.horas,":",self.minutos)
            else:
                print("Operação não realizada. O relógio está desligado!")
        else:
            print("Operação não realizada. O relógio está sem bateria!")

relogio1=Relógio()
relogio1.colocar_bateria()
relogio1.ligar()
relogio1.mostrar_horario()
relogio1.alterar_horas(20)
relogio1.alterar_minutos(22)
relogio1.mostrar_horario()

print("")

relogio2=Relógio()
relogio2.alterar_horas(12)
relogio2.colocar_bateria()
relogio2.alterar_minutos(55)
relogio2.ligar()
relogio2.mostrar_horario()
relogio2.alterar_horas(25)
relogio2.alterar_horas(8)
relogio2.alterar_minutos(77)
relogio2.alterar_minutos(43)
relogio2.mostrar_horario()
relogio2.desligar()
relogio2.retirar_bateria()