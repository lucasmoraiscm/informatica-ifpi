import sys

try:
    import tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3=False
except ImportError:
    import tkinter.ttk as ttk
    py3=True

class Toplevel1:
    def __init__(self):
        _bgcolor='#d9d9d9'
        _fgcolor='#000000'
        _compcolor='#d9d9d9'
        _ana1color='#d9d9d9'
        _ana2color='#ececec'
        font10="-family Simsun -size 20 -weight normal -slant roman " \
            "-underline 0 -overstrike 0"
        self.style=ttk.Style()
        if sys.platform=="win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected',_compcolor), ('active',_ana2color)])

        self.root=tk.Tk()
        self.root.geometry("600x606+647+284")
        self.root.title("New Toplevel")
        self.root.configure(background="#39007a")

        self.frameCadastro=tk.Frame(self.root)
        self.frameCadastro.place(relx=0.217, rely=0.182, relheight=0.668
                , relwidth=0.575)
        self.frameCadastro.configure(relief='flat')
        self.frameCadastro.configure(borderwidth="2")
        self.frameCadastro.configure(background="#0d1f42")

        self.Entry1=tk.Entry(self.frameCadastro)
        self.Entry1.place(relx=0.116, rely=0.272,height=20, relwidth=0.736)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2=tk.Entry(self.frameCadastro, show='*')
        self.Entry2.place(relx=0.116, rely=0.494,height=20, relwidth=0.736)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label1Cadastro=tk.Label(self.frameCadastro)
        self.Label1Cadastro.place(relx=0.377, rely=0.049, height=31, width=76)
        self.Label1Cadastro.configure(background="#0d1f42")
        self.Label1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro.configure(font=font10)
        self.Label1Cadastro.configure(foreground="#ffffff")
        self.Label1Cadastro.configure(text='''Login''')

        self.Label1Cadastro_1=tk.Label(self.frameCadastro)
        self.Label1Cadastro_1.place(relx=0.116, rely=0.173, height=31, width=106)
        self.Label1Cadastro_1.configure(activebackground="#f9f9f9")
        self.Label1Cadastro_1.configure(activeforeground="black")
        self.Label1Cadastro_1.configure(background="#0d1f42")
        self.Label1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro_1.configure(font="-family {Simsun} -size 20")
        self.Label1Cadastro_1.configure(foreground="#ffffff")
        self.Label1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro_1.configure(highlightcolor="black")
        self.Label1Cadastro_1.configure(text='''Usuario''')

        self.Label1Cadastro_2=tk.Label(self.frameCadastro)
        self.Label1Cadastro_2.place(relx=0.087, rely=0.395, height=31, width=106)
        self.Label1Cadastro_2.configure(activebackground="#f9f9f9")
        self.Label1Cadastro_2.configure(activeforeground="black")
        self.Label1Cadastro_2.configure(background="#0d1f42")
        self.Label1Cadastro_2.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro_2.configure(font="-family {Simsun} -size 20")
        self.Label1Cadastro_2.configure(foreground="#ffffff")
        self.Label1Cadastro_2.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro_2.configure(highlightcolor="black")
        self.Label1Cadastro_2.configure(text='''Senha''')

        self.Button1Cadastro=tk.Button(self.frameCadastro, command=self.LoginBackEnd)
        self.Button1Cadastro.place(relx=0.087, rely=0.593, height=54, width=117)
        self.Button1Cadastro.configure(activebackground="#ececec")
        self.Button1Cadastro.configure(activeforeground="#000000")
        self.Button1Cadastro.configure(background="#d8a0c5")
        self.Button1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Button1Cadastro.configure(foreground="#000000")
        self.Button1Cadastro.configure(highlightbackground="#d9d9d9")
        self.Button1Cadastro.configure(highlightcolor="black")
        self.Button1Cadastro.configure(pady="0")
        self.Button1Cadastro.configure(text='''Logar''')

        self.Button1Cadastro_3=tk.Button(self.frameCadastro, command=self.Cadastro)
        self.Button1Cadastro_3.place(relx=0.58, rely=0.593, height=54, width=117)
        self.Button1Cadastro_3.configure(activebackground="#ececec")
        self.Button1Cadastro_3.configure(activeforeground="#000000")
        self.Button1Cadastro_3.configure(background="#d8a0c5")
        self.Button1Cadastro_3.configure(disabledforeground="#a3a3a3")
        self.Button1Cadastro_3.configure(foreground="#000000")
        self.Button1Cadastro_3.configure(highlightbackground="#d9d9d9")
        self.Button1Cadastro_3.configure(highlightcolor="black")
        self.Button1Cadastro_3.configure(pady="0")
        self.Button1Cadastro_3.configure(text='''Cadastrar''')

        self.TSeparator1=ttk.Separator(self.frameCadastro)
        self.TSeparator1.place(relx=0.493, rely=0.568, relheight=0.148)
        self.TSeparator1.configure(orient="vertical")
        self.root.mainloop()

    def Cadastro(self):
        _bgcolor='#d9d9d9'
        _fgcolor='#000000'
        _compcolor='#d9d9d9'
        _ana1color='#d9d9d9'
        _ana2color='#ececec'
        font10="-family Simsun -size 20 -weight normal -slant roman " \
            "-underline 0 -overstrike 0"
        self.style=ttk.Style()
        if sys.platform=="win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected',_compcolor), ('active',_ana2color)])

        self.root=tk.Tk()
        self.root.geometry("600x606+647+284")
        self.root.title("Cadastro")
        self.root.configure(background="#39007a")

        self.frameCadastro=tk.Frame(self.root)
        self.frameCadastro.place(relx=0.217, rely=0.182, relheight=0.668
                , relwidth=0.575)
        self.frameCadastro.configure(relief='flat')
        self.frameCadastro.configure(borderwidth="2")
        self.frameCadastro.configure(background="#0d1f42")

        self.Entry1Cadastro=tk.Entry(self.frameCadastro)
        self.Entry1Cadastro.place(relx=0.116, rely=0.272,height=20, relwidth=0.736)
        self.Entry1Cadastro.configure(background="white")
        self.Entry1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Entry1Cadastro.configure(font="TkFixedFont")
        self.Entry1Cadastro.configure(foreground="#000000")
        self.Entry1Cadastro.configure(insertbackground="black")

        self.Entry2Cadastro=tk.Entry(self.frameCadastro, show='*')
        self.Entry2Cadastro.place(relx=0.116, rely=0.494,height=20, relwidth=0.736)
        self.Entry2Cadastro.configure(background="white")
        self.Entry2Cadastro.configure(disabledforeground="#a3a3a3")
        self.Entry2Cadastro.configure(font="TkFixedFont")
        self.Entry2Cadastro.configure(foreground="#000000")
        self.Entry2Cadastro.configure(insertbackground="black")

        self.Label1Cadastro=tk.Label(self.frameCadastro)
        self.Label1Cadastro.place(relx=0.377, rely=0.049, height=31, width=76)
        self.Label1Cadastro.configure(background="#0d1f42")
        self.Label1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro.configure(font=font10)
        self.Label1Cadastro.configure(foreground="#ffffff")
        self.Label1Cadastro.configure(text='''Cadastro''')

        self.Label1Cadastro_1=tk.Label(self.frameCadastro)
        self.Label1Cadastro_1.place(relx=0.116, rely=0.173, height=31, width=106)
        self.Label1Cadastro_1.configure(activebackground="#f9f9f9")
        self.Label1Cadastro_1.configure(activeforeground="black")
        self.Label1Cadastro_1.configure(background="#0d1f42")
        self.Label1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro_1.configure(font="-family {Simsun} -size 20")
        self.Label1Cadastro_1.configure(foreground="#ffffff")
        self.Label1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro_1.configure(highlightcolor="black")
        self.Label1Cadastro_1.configure(text='''Usuario''')

        self.Label1Cadastro_2=tk.Label(self.frameCadastro)
        self.Label1Cadastro_2.place(relx=0.087, rely=0.395, height=31, width=106)
        self.Label1Cadastro_2.configure(activebackground="#f9f9f9")
        self.Label1Cadastro_2.configure(activeforeground="black")
        self.Label1Cadastro_2.configure(background="#0d1f42")
        self.Label1Cadastro_2.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro_2.configure(font="-family {Simsun} -size 20")
        self.Label1Cadastro_2.configure(foreground="#ffffff")
        self.Label1Cadastro_2.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro_2.configure(highlightcolor="black")
        self.Label1Cadastro_2.configure(text='''Senha''')

        self.Button1Cadastro_3=tk.Button(self.frameCadastro, command=self.CadastrarBackEnd)
        self.Button1Cadastro_3.place(relx=0.58, rely=0.593, height=54, width=117)
        self.Button1Cadastro_3.configure(activebackground="#ececec")
        self.Button1Cadastro_3.configure(activeforeground="#000000")
        self.Button1Cadastro_3.configure(background="#d8a0c5")
        self.Button1Cadastro_3.configure(disabledforeground="#a3a3a3")
        self.Button1Cadastro_3.configure(foreground="#000000")
        self.Button1Cadastro_3.configure(highlightbackground="#d9d9d9")
        self.Button1Cadastro_3.configure(highlightcolor="black")
        self.Button1Cadastro_3.configure(pady="0")
        self.Button1Cadastro_3.configure(text='''Cadastrar''')

        self.TSeparator1=ttk.Separator(self.frameCadastro)
        self.TSeparator1.place(relx=0.493, rely=0.568, relheight=0.148)
        self.TSeparator1.configure(orient="vertical")
        self.root.mainloop()

    def CadastrarBackEnd(self):
        try:
            with open('usuarios.txt','a') as arquivoUsuario:
                arquivoUsuario.write(self.Entry1Cadastro.get()+'\n')

            with open('senhas.txt','a') as arquivoSenhas:
                arquivoSenhas.write(self.Entry2Cadastro.get()+'\n')
            self.root.destroy()
        except:
            print("houve um erro")

    def LoginBackEnd(self):
        with open('usuarios.txt','r') as arquivoUsuario:
            usuarios=arquivoUsuario.readlines()

        with open('senhas.txt','r') as arquivoUsuario:
            senhas=arquivoUsuario.readlines()

        usuarios=list(map(lambda x: x.replace('\n', ''), usuarios))

        senhas=list(map(lambda x: x.replace('\n', ''), senhas))

        usuario=self.Entry1.get()
        senha=self.Entry2.get()

        logado=False

        for i in range(len(usuarios)):
            if usuario==usuarios[i] and senha==senhas[i]:
                print("usuario logado")
                self.root.destroy()
                logado=True
        
        if not logado:
            print('usuario ou senha incorreto')
            self.root.destroy()
        
Toplevel1()
