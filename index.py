from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

jan = Tk()
jan.title("Página Login - Anninha")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
#jan.iconbitmap(default="arquivo") #tam 35x35

logo = PhotoImage(file="icons/logo_anna2.png") #carregarimagem dps 250x250

LeftFrame = Frame(jan, width=200, height=300, bg="#3c1a7d", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="#3c1a7d", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="#3c1a7d")
LogoLabel.place(x=18, y=100)

UserLabel = Label(RightFrame, text="Username: ", font=("Century Gothic",18), bg="#3c1a7d", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=140, y=111)

PassLabel = Label(RightFrame, text="Password: ", font=("Century Gothic",18), bg="#3c1a7d", fg="white")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show=".")
PassEntry.place(x=140, y=161)

def Login():
    DataBaser.cursor.execute("""
    SELECT (*) FROM Users
    WHERE (User = ? and Password = ?)                      
    """, (User, Pass))
    print("Selecionou")
    Verifylogin = DataBaser.cursor.fetchone()

    try:
        if (User in Verifylogin and Pass in Verifylogin):
            messagebox.showinfo(title="Login Info", message="Acesso confirmado")
    except:   
        messagebox.showinfo(title="login Info", message="Acesso negado")

LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 18), bg="#3c1a7d", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=140, y=15)

    EmailLabel = Label(RightFrame, text="E-mail:", font=("Century Gothic", 18), bg="#3c1a7d", fg="white")
    EmailLabel.place(x=5, y=50)

    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=140, y=59)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        
        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="Preencha Todos os Campos")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES (?, ?, ?, ?)                
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta Criada com Sucesso")      
    
    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)

    def BackToLogin():
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)  
        Register.place(x=5000)
        Back.place(x=5000)

        LoginButton.place(x=100)
        RegisterButton.place(x=133)

    Back = ttk.Button(RightFrame, text="Back", width=18, command=BackToLogin)
    Back.place(x=133, y=260) 

RegisterButton = ttk.Button(RightFrame, text="Register", width=18, command=Register)
RegisterButton.place(x=133, y=260)

jan.mainloop()