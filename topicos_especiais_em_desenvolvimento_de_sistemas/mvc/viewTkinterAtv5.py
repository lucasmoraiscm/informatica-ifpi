from tkinter import*
from controllerAtv5 import*

def btn_click1():     
    if ed_ida.get().isnumeric() and ed_cpf.get().isnumeric():   	 	
        lb_m["text"] = AlunoController.cadastrar(ed_nome.get(), ed_ida.get(), ed_cpf.get())

#janela
janela = Tk()
janela.geometry("500x500+300+300")
janela.title("Aluno")

#nome
lb = Label(janela,text = "Nome:")
lb.place(x = 10,y = 20)
ed_nome = Entry(janela, bg = "white")
ed_nome.place(x = 100,y = 20)

#idade
lb = Label(janela, text = "Idade:")
lb.place(x = 10, y = 50)
ed_ida = Entry(janela, bg = "white")
ed_ida.place(x = 100, y = 50)

#cpf
lb = Label(janela, text = "CPF:")
lb.place(x = 10,y = 80)
ed_cpf = Entry(janela, bg = "white")
ed_cpf.place(x = 100, y = 80)

#label para imprimir as operaçoes
lb_m = Label(janela, text = "")
lb_m.place(x = 10, y = 110)

#botao   
bt1 = Button(janela, text = "Cadastrar", width = 10, command = btn_click1)
bt1.place(x = 85, y = 150)

janela.mainloop()
