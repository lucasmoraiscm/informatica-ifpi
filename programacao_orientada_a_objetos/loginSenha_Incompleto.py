#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Nov 23, 2021 09:08:26 AM -03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



class Toplevel1:


    #completar o código de testeLogin
    #verifique se login e senha já estão cadastrados.. só permita entrar no sistema se sim
    #senao imprima a mensagem que o login não existe e saia do programa
    #substitua a linha print("login nao cadastrado!!") colocando a mesma
    #mensagem em uma label que apareça na própria janela
    def testeLogin(self):
        
        with open('usuario.txt','r')as Usuarios:
            usu = Usuarios.readlines()       
        

        with open('senha.txt','r')as Senhas:
            sen = Senhas.readlines()
       

        encontrou = False
        for i in range(len(usu)):
            if self.Entry1.get()+'\n'==usu[i]:
                
                encontrou = True
                break
        if not(encontrou):
            self.Label3['text']="login não cadastrado!!"
            print("login nao cadastrado!!")          
                
            

        
    #    self.top.destroy()
            

    def cadastroBackEnd(self):
        with open('usuario.txt','a')as arquivoUsuario:
            arquivoUsuario.write(self.Et1.get()+'\n')

        with open('senha.txt','a')as arquivoSenha:
            arquivoSenha.write(self.Et2.get()+'\n')
            
    def janela2(self):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.root=tk.Tk()
        self.root.geometry("600x450+365+186")
        self.root.minsize(124, 1)
        self.root.maxsize(1362, 741)
        self.root.resizable(1,  1)
        self.root.title("Janela de CADASTRO DE LOGIN")
        self.root.configure(background="#d9d9d9")
        self.root.configure(highlightbackground="#d9d9d9")
        self.root.configure(highlightcolor="black")

        self.FrameCadastro = tk.Frame(self.root)
        self.FrameCadastro.place(relx=0.25, rely=0.178, relheight=0.5, relwidth=0.492)
        self.FrameCadastro.configure(relief='groove')
        self.FrameCadastro.configure(borderwidth="2")
        self.FrameCadastro.configure(relief="groove")
        self.FrameCadastro.configure(background="#d9d9d9")
        self.FrameCadastro.configure(highlightbackground="#d9d9d9")
        self.FrameCadastro.configure(highlightcolor="black")

        '''self.Bt1 = tk.Button(self.FrameCadastro)
        self.Bt1.place(relx=0.169, rely=0.756, height=24, width=47)
        self.Bt1.configure(activebackground="#ececec")
        self.Bt1.configure(activeforeground="#000000")
        self.Bt1.configure(background="#d9d9d9")
        self.Bt1.configure(disabledforeground="#a3a3a3")
        self.Bt1.configure(foreground="#000000")
        self.Bt1.configure(highlightbackground="#d9d9d9")
        self.Bt1.configure(highlightcolor="black")
        self.Bt1.configure(pady="0")
        self.Bt1.configure(text="Login")'''

        self.Bt2 = tk.Button(self.FrameCadastro,command=self.cadastroBackEnd)
        self.Bt2.place(relx=0.61, rely=0.756, height=24, width=60)
        self.Bt2.configure(activebackground="#ececec")
        self.Bt2.configure(activeforeground="#000000")
        self.Bt2.configure(background="#d9d9d9")
        self.Bt2.configure(disabledforeground="#a3a3a3")
        self.Bt2.configure(foreground="#000000")
        self.Bt2.configure(highlightbackground="#d9d9d9")
        self.Bt2.configure(highlightcolor="black")
        self.Bt2.configure(pady="0")
        self.Bt2.configure(text='''Cadastrar''')

        self.Lb1 = tk.Label(self.FrameCadastro)
        self.Lb1.place(relx=0.136, rely=0.222, height=31, width=74)
        self.Lb1.configure(activebackground="#f9f9f9")
        self.Lb1.configure(activeforeground="black")
        self.Lb1.configure(background="#d9d9d9")
        self.Lb1.configure(disabledforeground="#a3a3a3")
        self.Lb1.configure(foreground="#000000")
        self.Lb1.configure(highlightbackground="#d9d9d9")
        self.Lb1.configure(highlightcolor="black")
        self.Lb1.configure(text='''Usuário:''')

        self.Lb2 = tk.Label(self.FrameCadastro)
        self.Lb2.place(relx=0.142, rely=0.4, height=31, width=74)
        self.Lb2.configure(activebackground="#f9f9f9")
        self.Lb2.configure(activeforeground="black")
        self.Lb2.configure(background="#d9d9d9")
        self.Lb2.configure(disabledforeground="#a3a3a3")
        self.Lb2.configure(foreground="#000000")
        self.Lb2.configure(highlightbackground="#d9d9d9")
        self.Lb2.configure(highlightcolor="black")
        self.Lb2.configure(text='''Senha:''')

        self.Et1 = tk.Entry(self.FrameCadastro)
        self.Et1.place(relx=0.373, rely=0.267, height=20, relwidth=0.285)
        self.Et1.configure(background="white")
        self.Et1.configure(disabledforeground="#a3a3a3")
        self.Et1.configure(font="TkFixedFont")
        self.Et1.configure(foreground="#000000")
        self.Et1.configure(highlightbackground="#d9d9d9")
        self.Et1.configure(highlightcolor="black")
        self.Et1.configure(insertbackground="black")
        self.Et1.configure(selectbackground="blue")
        self.Et1.configure(selectforeground="white")

        self.Et2 = tk.Entry(self.FrameCadastro)
        self.Et2.place(relx=0.373, rely=0.444, height=20, relwidth=0.285)
        self.Et2.configure(background="white")
        self.Et2.configure(disabledforeground="#a3a3a3")
        self.Et2.configure(font="TkFixedFont")
        self.Et2.configure(foreground="#000000")
        self.Et2.configure(highlightbackground="#d9d9d9")
        self.Et2.configure(highlightcolor="black")
        self.Et2.configure(insertbackground="black")
        self.Et2.configure(selectbackground="blue")
        self.Et2.configure(selectforeground="white")

        self.TSeparator1 = ttk.Separator(self.FrameCadastro)
        self.TSeparator1.place(relx=0.475, rely=0.711,  relheight=0.164)
        self.TSeparator1.configure(orient="vertical")
        self.root.mainloop()

        
        
    def __init__(self,top=tk.Tk()):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.top=top
        self.top.geometry("600x450+365+186")
        self.top.minsize(124, 1)
        self.top.maxsize(1362, 741)
        self.top.resizable(1,  1)
        self.top.title("Janela de Login")
        self.top.configure(background="#d9d9d9")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.25, rely=0.178, relheight=0.5, relwidth=0.492)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Button1 = tk.Button(self.Frame1,command=self.testeLogin)
        self.Button1.place(relx=0.169, rely=0.756, height=24, width=47)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Login''')

        self.Button2 = tk.Button(self.Frame1,command=self.janela2)
        self.Button2.place(relx=0.61, rely=0.756, height=24, width=60)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Cadastrar''')

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.136, rely=0.222, height=31, width=74)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Usuário:''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.142, rely=0.4, height=31, width=74)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Senha:''')

        
        
        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.15, rely=0.880, height=16, width=214)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Label3.configure(text='''''')
  



        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.373, rely=0.267, height=20, relwidth=0.285)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        self.Entry2 = tk.Entry(self.Frame1,show="*")
        self.Entry2.place(relx=0.373, rely=0.444, height=20, relwidth=0.285)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="white")
        
        
  
        self.TSeparator1 = ttk.Separator(self.Frame1)
        self.TSeparator1.place(relx=0.475, rely=0.711,  relheight=0.164)
        self.TSeparator1.configure(orient="vertical")
        self.top.mainloop()


Toplevel1()