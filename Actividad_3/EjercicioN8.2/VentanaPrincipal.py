import tkinter as tk
from tkinter import messagebox
from Notas import Notas


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self._inicio()
        self.title("Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"+{x}+{y}")

    def _inicio(self):
        self.nota1 = tk.Label(self, text="Nota 1:")
        self.nota1.place(x=20, y=20, width=135, height=23)

        self.campo_nota1 = tk.Entry(self)
        self.campo_nota1.place(x=105, y=20, width=135, height=23)

        self.nota2 = tk.Label(self, text="Nota 2:")
        self.nota2.place(x=20, y=50, width=135, height=23)

        self.campo_nota2 = tk.Entry(self)
        self.campo_nota2.place(x=105, y=50, width=135, height=23)

        self.nota3 = tk.Label(self, text="Nota 3:")
        self.nota3.place(x=20, y=80, width=135, height=23)

        self.campo_nota3 = tk.Entry(self)
        self.campo_nota3.place(x=105, y=80, width=135, height=23)

        self.nota4 = tk.Label(self, text="Nota 4:")
        self.nota4.place(x=20, y=110, width=135, height=23)

        self.campo_nota4 = tk.Entry(self)
        self.campo_nota4.place(x=105, y=110, width=135, height=23)

        self.nota5 = tk.Label(self, text="Nota 5:")
        self.nota5.place(x=20, y=140, width=135, height=23)

        self.campo_nota5 = tk.Entry(self)
        self.campo_nota5.place(x=105, y=140, width=135, height=23)

        self.calcular = tk.Button(self, text="Calcular",
                                    command=self._accion_calcular)
        self.calcular.place(x=20, y=170, width=100, height=23)

        self.limpiar = tk.Button(self, text="Limpiar",
                                    command=self._accion_limpiar)
        self.limpiar.place(x=125, y=170, width=80, height=23)
        self.promedio = tk.Label(self, text="Promedio = ")
        self.promedio.place(x=20, y=210, width=230, height=23)

        self.desviacion = tk.Label(self, text="Desviación = ")
        self.desviacion.place(x=20, y=240, width=230, height=23)

        self.mayor = tk.Label(self, text="Nota mayor = ")
        self.mayor.place(x=20, y=270, width=230, height=23)

        self.menor = tk.Label(self, text="Nota menor = ")
        self.menor.place(x=20, y=300, width=230, height=23)

    def _accion_calcular(self):

        campos = [
            ("Nota 1", self.campo_nota1),
            ("Nota 2", self.campo_nota2),
            ("Nota 3", self.campo_nota3),
            ("Nota 4", self.campo_nota4),
            ("Nota 5", self.campo_nota5),
        ]

        for nombre, campo in campos:
            if campo.get().strip() == "":
                messagebox.showwarning(
                    "Campo vacio",
                    f"Es obligatorio ingresar {nombre}.\n"
                    "Por favor complete todas las notas."
                )
                campo.focus_set()
                return

        valores = []
        for nombre, campo in campos:
            try:
                valor = float(campo.get().strip())
                valores.append(valor)
            except ValueError:
                messagebox.showerror(
                    "Dato invalido",
                    f"{nombre}: \"{campo.get()}\" no es un numero valido.\n"
                    "Por favor ingrese solo valores numericos."
                )
                campo.focus_set()
                return

        notas = Notas()
        notas.lista_notas[0] = valores[0]
        notas.lista_notas[1] = valores[1]
        notas.lista_notas[2] = valores[2]
        notas.lista_notas[3] = valores[3]
        notas.lista_notas[4] = valores[4]

        notas.calcular_promedio()   
        notas.calcular_desviacion() 
        self.promedio.config(
            text=f"Promedio = {notas.calcular_promedio():.2f}"
        )
        desv = notas.calcular_desviacion()
        self.desviacion.config(
            text=f"Desviación estándar = {desv:.2f}"
        )
        self.mayor.config(
            text=f"Valor mayor = {notas.calcular_mayor()}"
        )
        self.menor.config(
            text=f"Valor menor = {notas.calcular_menor()}"
        )

    def _accion_limpiar(self):
        self.campo_nota1.delete(0, tk.END)
        self.campo_nota2.delete(0, tk.END)
        self.campo_nota3.delete(0, tk.END)
        self.campo_nota4.delete(0, tk.END)
        self.campo_nota5.delete(0, tk.END)

        self.promedio.config(text="Promedio = ")
        self.desviacion.config(text="Desviación = ")
        self.mayor.config(text="Nota mayor = ")
        self.menor.config(text="Nota menor = ")