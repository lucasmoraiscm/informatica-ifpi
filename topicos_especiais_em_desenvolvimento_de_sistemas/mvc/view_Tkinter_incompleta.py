from tkinter import *
#from controller import *
from controllerAtv5 import*

class AlunoView:
    @classmethod
    def salvamento(cls):
        nome = tr1.get()
        idade = int(tr2.get())
        cpf = tr3.get()
        if AlunoController.salvar(nome, idade, cpf):
            lb4['text'] = 'Aluno(a) salvo(a) com sucesso!'
            AlunoController.ler()
        else:
            lb4['text'] = 'Dados inválidos! Tente novamente!'

    #Esse método está incompleto, ainda não consegue imprimir todos os aluno no tkinter
    @classmethod
    def leitura(cls):
        #l = AlunoDao.ler()
        #for i in l:
            #lb5['text'] = "Nome: "+i.nome+" - Idade: "+str(i.idade)+" - CPF: "+i.cpf
        lb5['text'] = AlunoController.ler()

###
def salvamento():
    lb4["text"] = AlunoController.cadastrar(tr1.get(), tr2.get(), tr3.get())

def leitura():
    lb5["text"] = AlunoController.visualizar()
###

#janela
janela = Tk()
janela.geometry('500x500')
janela.title('Salvamento De Alunos(as)')

#introdução
lb0 = Label(janela, text = 'DADOS DO(A) ALUNO(A)')
lb0['font'] = ('bold')
lb0.place(x = 155, y = 10)

#nome
lb1 = Label(janela, text = 'Nome:')
lb1.place(x = 90, y = 70)

tr1 = Entry(janela)
tr1.place(x = 190, y = 70)

#idade
lb2 = Label(janela, text = 'Idade:')
lb2.place(x = 90, y = 100)

tr2 = Entry(janela)
tr2.place(x = 190, y = 100)

#cpf
lb3 = Label(janela, text = 'CPF:')
lb3.place(x = 90, y = 130)

tr3 = Entry(janela)
tr3.place(x = 190, y = 130)

btn1 = Button(janela, text = 'Salvar', command = AlunoView.salvamento)
btn1 = Button(janela, text = 'Salvar', command = leitura)
btn1.place(x = 230, y = 155)

#resultado salvamento
lb4 = Label(janela, text = '')
lb4.place(x = 90, y = 185)

btn2 = Button(janela, text = 'Alunos(as) salvos(as)', command = AlunoView.leitura)
btn2 = Button(janela, text = 'Alunos(as) salvos(as)', command = salvamento)
btn2.place(x = 190, y = 210)

#resultado leitura
lb5 = Label(janela, text = '')
lb5.place(x = 90, y = 250)

janela.mainloop()
