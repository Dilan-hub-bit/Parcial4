import tkinter as tk
from tkinter import messagebox
from Usuario import Usuario
from .Registro import Registro
from .Dashboard import Dashboard

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x180")

        tk.Label(self, text="Nickname:").pack()
        self.txt_nickname = tk.Entry(self)
        self.txt_nickname.pack()

        tk.Label(self, text="Clave:").pack()
        self.txt_clave = tk.Entry(self, show="*")
        self.txt_clave.pack()

        tk.Button(self, text="Ingresar", command=self.ingresar).pack(pady=5)
        tk.Button(self, text="Registrar Usuario", command=self.abrir_registro).pack()

    def ingresar(self):
        nickname = self.txt_nickname.get()
        clave = self.txt_clave.get()
        usuario = Usuario.validarUsuario(nickname, clave)
        if usuario:
            messagebox.showinfo("Bienvenido", f"Hola {usuario.nombre} {usuario.apellidos}")
            self.destroy()
            Dashboard(usuario)
        else:
            messagebox.showerror("Error", "Usuario o clave incorrectos.")

    def abrir_registro(self):
        Registro()
