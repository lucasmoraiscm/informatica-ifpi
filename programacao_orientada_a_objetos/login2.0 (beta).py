import sys

try:
    import tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import tkinter.ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



class Toplevel1:
    def __init__(self):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
       
        self.root=tk.Tk()
        self.root.geometry("630x594+628+164")
        self.root.minsize(120, 1)
        self.root.maxsize(1604, 881)
        self.root.resizable(1,  1)
        self.root.title("New Toplevel")
        self.root.configure(background="#9f00ff")
        self.root.configure(highlightbackground="#d9d9d9")
        self.root.configure(highlightcolor="black")
        self.root.resizable(False,False)
        self.menubar = tk.Menu(self.root,font="TkMenuFont",bg='#0026a8',fg=_fgcolor)
        self.root.configure(menu = self.menubar)

        self.FrameCadastro = tk.Frame(self.root)
        self.FrameCadastro.place(relx=0.175, rely=0.101, relheight=0.835
                , relwidth=0.697)
        self.FrameCadastro.configure(relief='groove')
        self.FrameCadastro.configure(borderwidth="2")
        self.FrameCadastro.configure(relief="groove")
        self.FrameCadastro.configure(background="#0a01a7")
        self.FrameCadastro.configure(highlightbackground="#d9d9d9")
        self.FrameCadastro.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(self.FrameCadastro)
        self.Entry1.place(relx=0.091, rely=0.3, height=20, relwidth=0.829)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        self.Entry2 = tk.Entry(self.FrameCadastro,show='*')
        self.Entry2.place(relx=0.091, rely=0.536, height=20, relwidth=0.829)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="white")

        self.Label1Cadastro = tk.Label(self.FrameCadastro)
        self.Label1Cadastro.place(relx=0.342, rely=0.044, height=49, width=134)
        self.Label1Cadastro.configure(activebackground="#f9f9f9")
        self.Label1Cadastro.configure(activeforeground="black")
        self.Label1Cadastro.configure(background="#0a01a7")
        self.Label1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro.configure(font="-family {Segoe UI} -size 20")
        self.Label1Cadastro.configure(foreground="#ffffff")
        self.Label1Cadastro.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro.configure(highlightcolor="black")
        self.Label1Cadastro.configure(text='''Login''')

        self.Label1Cadastro_1 = tk.Label(self.FrameCadastro)
        self.Label1Cadastro_1.place(relx=0.068, rely=0.194, height=49, width=134)
        self.Label1Cadastro_1.configure(activebackground="#f9f9f9")
        self.Label1Cadastro_1.configure(activeforeground="black")
        self.Label1Cadastro_1.configure(background="#0a01a7")
        self.Label1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro_1.configure(font="-family {Segoe UI} -size 20")
        self.Label1Cadastro_1.configure(foreground="#ffffff")
        self.Label1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro_1.configure(highlightcolor="black")
        self.Label1Cadastro_1.configure(text='''Usuário:''')

        self.Label1Cadastro_2 = tk.Label(self.FrameCadastro)
        self.Label1Cadastro_2.place(relx=0.023, rely=0.429, height=49, width=134)
        self.Label1Cadastro_2.configure(activebackground="#f9f9f9")
        self.Label1Cadastro_2.configure(activeforeground="black")
        self.Label1Cadastro_2.configure(background="#0a01a7")
        self.Label1Cadastro_2.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro_2.configure(font="-family {Segoe UI} -size 20")
        self.Label1Cadastro_2.configure(foreground="#ffffff")
        self.Label1Cadastro_2.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro_2.configure(highlightcolor="black")
        self.Label1Cadastro_2.configure(text='''Senha:''')

        self.Button1Cadastro = tk.Button(self.FrameCadastro,comman=self.LoginBackEnd)
        self.Button1Cadastro.place(relx=0.319, rely=0.645, height=54, width=167)
        self.Button1Cadastro.configure(activebackground="#ececec")
        self.Button1Cadastro.configure(activeforeground="#000000")
        self.Button1Cadastro.configure(background="#ffffff")
        self.Button1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Button1Cadastro.configure(font="-family {Segoe UI} -size 14")
        self.Button1Cadastro.configure(foreground="#000000")
        self.Button1Cadastro.configure(highlightbackground="#d9d9d9")
        self.Button1Cadastro.configure(highlightcolor="black")
        self.Button1Cadastro.configure(pady="0")
        self.Button1Cadastro.configure(text='''LOGAR''')

        self.Button1Cadastro_1 = tk.Button(self.FrameCadastro,command=self.cadastro)
        self.Button1Cadastro_1.place(relx=0.319, rely=0.806, height=54, width=167)
        self.Button1Cadastro_1.configure(activebackground="#ececec")
        self.Button1Cadastro_1.configure(activeforeground="#000000")
        self.Button1Cadastro_1.configure(background="#ffffff")
        self.Button1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Button1Cadastro_1.configure(font="-family {Segoe UI} -size 14")
        self.Button1Cadastro_1.configure(foreground="#000000")
        self.Button1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Button1Cadastro_1.configure(highlightcolor="black")
        self.Button1Cadastro_1.configure(pady="0")
        self.Button1Cadastro_1.configure(text='''CADASTRAR''')
        self.root.mainloop()
    
   
    
    def cadastro(self):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
       
        self.root=tk.Tk()
        self.root.geometry("630x594+628+164")
        self.root.minsize(120, 1)
        self.root.maxsize(1604, 881)
        self.root.resizable(1,  1)
        self.root.title("CADASTRO")
        self.root.configure(background="#9f00ff")
        self.root.configure(highlightbackground="#d9d9d9")
        self.root.configure(highlightcolor="black")
        self.root.resizable(False,False)
        self.menubar = tk.Menu(self.root,font="TkMenuFont",bg='#0026a8',fg=_fgcolor)
        self.root.configure(menu = self.menubar)

        self.FrameCadastro = tk.Frame(self.root)
        self.FrameCadastro.place(relx=0.175, rely=0.101, relheight=0.835
                , relwidth=0.697)
        self.FrameCadastro.configure(relief='groove')
        self.FrameCadastro.configure(borderwidth="2")
        self.FrameCadastro.configure(relief="groove")
        self.FrameCadastro.configure(background="#0a01a7")
        self.FrameCadastro.configure(highlightbackground="#d9d9d9")
        self.FrameCadastro.configure(highlightcolor="black")

        self.Entry1Cadastro = tk.Entry(self.FrameCadastro)
        self.Entry1Cadastro.place(relx=0.091, rely=0.3, height=20, relwidth=0.829)
        self.Entry1Cadastro.configure(background="white")
        self.Entry1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Entry1Cadastro.configure(font="TkFixedFont")
        self.Entry1Cadastro.configure(foreground="#000000")
        self.Entry1Cadastro.configure(highlightbackground="#d9d9d9")
        self.Entry1Cadastro.configure(highlightcolor="black")
        self.Entry1Cadastro.configure(insertbackground="black")
        self.Entry1Cadastro.configure(selectbackground="blue")
        self.Entry1Cadastro.configure(selectforeground="white")

        self.Entry2Cadastro = tk.Entry(self.FrameCadastro,show='*')
        self.Entry2Cadastro.place(relx=0.091, rely=0.536, height=20, relwidth=0.829)
        self.Entry2Cadastro.configure(background="white")
        self.Entry2Cadastro.configure(disabledforeground="#a3a3a3")
        self.Entry2Cadastro.configure(font="TkFixedFont")
        self.Entry2Cadastro.configure(foreground="#000000")
        self.Entry2Cadastro.configure(highlightbackground="#d9d9d9")
        self.Entry2Cadastro.configure(highlightcolor="black")
        self.Entry2Cadastro.configure(insertbackground="black")
        self.Entry2Cadastro.configure(selectbackground="blue")
        self.Entry2Cadastro.configure(selectforeground="white")

        self.Label1Cadastro = tk.Label(self.FrameCadastro)
        self.Label1Cadastro.place(relx=0.342, rely=0.044, height=49, width=134)
        self.Label1Cadastro.configure(activebackground="#f9f9f9")
        self.Label1Cadastro.configure(activeforeground="black")
        self.Label1Cadastro.configure(background="#0a01a7")
        self.Label1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro.configure(font="-family {Segoe UI} -size 20")
        self.Label1Cadastro.configure(foreground="#ffffff")
        self.Label1Cadastro.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro.configure(highlightcolor="black")
        self.Label1Cadastro.configure(text='''Cadastro''')
        self.Label1Cadastro.configure(width=70)

        self.Label1Cadastro_1 = tk.Label(self.FrameCadastro)
        self.Label1Cadastro_1.place(relx=0.068, rely=0.194, height=49, width=134)
        self.Label1Cadastro_1.configure(activebackground="#f9f9f9")
        self.Label1Cadastro_1.configure(activeforeground="black")
        self.Label1Cadastro_1.configure(background="#0a01a7")
        self.Label1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro_1.configure(font="-family {Segoe UI} -size 20")
        self.Label1Cadastro_1.configure(foreground="#ffffff")
        self.Label1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro_1.configure(highlightcolor="black")
        self.Label1Cadastro_1.configure(text='''Usuário:''')

        self.Label1Cadastro_2 = tk.Label(self.FrameCadastro)
        self.Label1Cadastro_2.place(relx=0.023, rely=0.429, height=49, width=134)
        self.Label1Cadastro_2.configure(activebackground="#f9f9f9")
        self.Label1Cadastro_2.configure(activeforeground="black")
        self.Label1Cadastro_2.configure(background="#0a01a7")
        self.Label1Cadastro_2.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro_2.configure(font="-family {Segoe UI} -size 20")
        self.Label1Cadastro_2.configure(foreground="#ffffff")
        self.Label1Cadastro_2.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro_2.configure(highlightcolor="black")
        self.Label1Cadastro_2.configure(text='''Senha:''')

       

        self.Button1Cadastro_1 = tk.Button(self.FrameCadastro,command=self.CadastrarBackEnd)
        self.Button1Cadastro_1.place(relx=0.319, rely=0.806, height=54, width=167)
        self.Button1Cadastro_1.configure(activebackground="#ececec")
        self.Button1Cadastro_1.configure(activeforeground="#000000")
        self.Button1Cadastro_1.configure(background="#ffffff")
        self.Button1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Button1Cadastro_1.configure(font="-family {Segoe UI} -size 14")
        self.Button1Cadastro_1.configure(foreground="#000000")
        self.Button1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Button1Cadastro_1.configure(highlightcolor="black")
        self.Button1Cadastro_1.configure(pady="0")
        self.Button1Cadastro_1.configure(text='''CADASTRAR''')
        self.root.mainloop()

    def CadastrarBackEnd(self):
       try:
            with open('usuarios.txt','a') as ArquivoUsuário:
                ArquivoUsuário.write(self.Entry1Cadastro.get()+"\n")
            with open('senhas.txt','a') as ArquivoUsuário:
                ArquivoUsuário.write(self.Entry2Cadastro.get()+"\n")
            self.root.destroy()
       except:
            print("Ocorreu um erro !")
            
    def LoginBackEnd(self):
          with open('usuarios.txt','r') as ArquivoUsuário:
             usuarios=ArquivoUsuário.readlines()
        
          with open('senhas.txt','r') as ArquivoUsuário:
             senhas=ArquivoUsuário.readlines()
          usuarios=list(map(lambda x : x.replace("\n",""),usuarios ))
          senhas=list(map(lambda x : x.replace("\n",""),senhas ))

          usuario=self.Entry1.get()
          senha=self.Entry2.get()
          Logado=False
          for x in range(len(usuarios)):
              if usuario==usuarios[x] and senha==senhas[x]:
                  print("USUÁRIO LOGADO")
                  self.root.destroy()
                  Logado=True
          if not Logado:
              print("Usuário ou Senha Incorreto ")
              self.root.destroy()
         
       

             

             


        


Toplevel1()




