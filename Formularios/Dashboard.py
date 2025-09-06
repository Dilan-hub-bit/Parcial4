import tkinter as tk

class Dashboard(tk.Tk):
    def __init__(self, usuario):
        super().__init__()
        self.title("Dashboard")
        self.geometry("400x200")

        tk.Label(self, text=f"Bienvenido {usuario.nombre} {usuario.apellidos}").pack(pady=10)

        
        self.img_label = tk.Label(self, text="[Imagen por defecto]")
        self.img_label.pack()
