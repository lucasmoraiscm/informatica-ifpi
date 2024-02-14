from tkinter import *

class Ip:
    def __init__(self,ip):
        self.ip=ip
                
    def validar(self):
        ip=tr1.get()
        ip=ip.split(".")
        if len(ip)==4:
            ok=True
            for byte in ip:
                if int(byte)>255:
                    ok=False
                    return False
        else:
            ok=False
            return False
        if ok==True:
            return True

    def testar():
        ip=tr1.get()
        ip=ip.split(".")
        if len(ip)==4:
            ok=True
            for byte in ip:
                if int(byte)>255:
                    lb2["text"]="Inválido"
                    ok=False
                    break
        else:
            ok=False
            lb2["text"]="Inválido"
        if ok==True:
            lb2["text"]="Válido"

janela = Tk()
janela.geometry("500x500")

lb1=Label(janela, text='DIGITE O IP:')
lb1.pack()

tr1=Entry(janela)
tr1.pack()

bt1=Button(janela,text="VALIDAR",command=Ip.testar)
bt1.pack()

lb2=Label(janela, text="")
lb2.pack()

janela.mainloop()
