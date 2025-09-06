import tkinter as tk

class Dashboard(tk.Toplevel): 
    def __init__(self, usuario):
        super().__init__()
        self.title("Dashboard")
        self.geometry("300x150")

        mensaje = f"Bienvenido {usuario.nombre} {usuario.apellidos}"
        tk.Label(self, text=mensaje, font=("Arial", 14)).pack(pady=40)