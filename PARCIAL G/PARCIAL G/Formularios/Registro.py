import tkinter as tk
from tkinter import messagebox
from Clases.Usuario import Usuario

class Registro(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Registrar Usuario")
        self.geometry("300x280")

        tk.Label(self, text="Nombre:").pack()
        self.txt_nombre = tk.Entry(self)
        self.txt_nombre.pack()

        tk.Label(self, text="Apellidos:").pack()
        self.txt_apellidos = tk.Entry(self)
        self.txt_apellidos.pack()

        tk.Label(self, text="Email:").pack()
        self.txt_email = tk.Entry(self)
        self.txt_email.pack()

        tk.Label(self, text="Nickname:").pack()
        self.txt_nickname = tk.Entry(self)
        self.txt_nickname.pack()

        tk.Label(self, text="Clave:").pack()
        self.txt_clave = tk.Entry(self, show="*")
        self.txt_clave.pack()

        tk.Button(self, text="Guardar", command=self.guardar).pack(pady=10)

    def guardar(self):
        nombre = self.txt_nombre.get()
        apellidos = self.txt_apellidos.get()
        email = self.txt_email.get()
        nickname = self.txt_nickname.get()
        clave = self.txt_clave.get()

        if not (nombre and apellidos and email and nickname and clave):
            messagebox.showwarning("Atención", "Por favor complete todos los campos")
            return

        Usuario.guardarUsuario(nombre, apellidos, email, nickname, clave)
        messagebox.showinfo("Registro", "Usuario guardado con éxito")
        self.destroy()
