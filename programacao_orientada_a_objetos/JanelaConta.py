from tkinter import *

class Conta(object):
   def __init__(self, id_conta,id_cliente,saldo,limite):
     self.id_conta=id_conta
     self.id_cliente=id_cliente
     self.saldo=saldo
     self.limite=limite
     self.debito=0

   def mostraSaldo(self):
      return " Saldo: %.2f Limite: %.2f"%(self.saldo,self.limite)
  
   def sacar(self,valor):
     if valor<=self.saldo+self.limite:
       self.saldo=self.saldo-valor
       if self.saldo<0:
          self.debito=-(self.saldo)
          self.limite=self.limite+self.saldo
          self.saldo=0
       return True
     else:
        return False


   def transferir(self,valor,c):
      if self.sacar(valor):
          c.depositar(valor)
          return True
      else:
        return False


   def depositar(self,valor):
        if self.debito>0:
            if (valor<=self.debito):
              self.debito-=valor
              self.limite+=valor
            else:
              dif=valor-self.debito
              self.saldo+=dif
              self.limite+=self.debito
              self.debito=0
        else:
            self.saldo+=valor










def btn_click0():
     global c
     if ed_saldo.get().isnumeric() and ed_limite.get().isnumeric():
        c=Conta(ed_conta.get(),ed_cli.get(),float(ed_saldo.get()),float(ed_limite
.get()))
        lb_m["text"]="Conta criada com sucesso!" + c.mostraSaldo()
     else:
        lb_m["text"]="Conta não foi criada!!"



def btn_click1():
  
    if ed_valor.get().isnumeric():
       c.depositar(float(ed_valor.get()))
       lb_m["text"]="Depósito Realizado com Sucesso" + c.mostraSaldo()
      
   
    else:
      lb_m["text"]="Valor inválido!!! Não é possível realizar a operação!!" + "Deposito não realizado"
    





def btn_click2():
  if  ed_valor.get().isnumeric: 
         
         if int(ed_valor.get())> int(c.saldo+c.limite):
            lb_m["text"]="Saque não realizado!"
         
         else:
          c.sacar(float(ed_valor.get()))
          lb_m["text"]="Saque Realizado Com Sucesso" + c.mostraSaldo()  
       
  
  else:
       lb_m["text"]="Valor inválido!!! Não é possível realizar a operação!!" + "Saque não realizado"


def btn_click3():
   lb_m["text"]=""
   lb_m["text"]=c.mostraSaldo()



janela=Tk()
janela.geometry("500x500")
janela.resizable(False,False)
ed_conta=Entry(janela,bg="white")
ed_conta.place(x=155,y=20)
ed_cli=Entry(janela,bg="white")
ed_cli.place(x=155,y=40)
ed_saldo=Entry(janela, bg="white")
ed_saldo.place(x=155,y=60)
ed_limite=Entry(janela, bg="white")
ed_limite.place(x=155,y=80)


lb=Label(janela,text="Conta:")
lb.place(x=10,y=20)
lb=Label(janela,text="Cliente:")
lb.place(x=10,y=40)
lb=Label(janela,text="Saldo:")
lb.place(x=10,y=60)
lb=Label(janela,text="Limite:")
lb.place(x=10,y=80)
lb=Label(janela, text="Valor:")
lb.place(x=10,y=150)
ed_valor=Entry(janela, bg="white")
ed_valor.place(x=155,y=150)
lb_m=Label(janela,text=" ")
lb_m.place(x=10,y=230)

janela.title("Conta")
bt0=Button(janela,text="Criar Conta",width=10,command=btn_click0)
bt0.place(x=25,y=200)
bt1=Button(janela,text="Depositar",width=10,command=btn_click1)
bt1.place(x=120,y=200)
bt2=Button(janela,text="Sacar",width=10,command=btn_click2)
bt2.place(x=220,y=200)
bt3=Button(janela,text="Saldo",width=10, command=btn_click3)
bt3.place(x=320,y=200)




janela.mainloop()




