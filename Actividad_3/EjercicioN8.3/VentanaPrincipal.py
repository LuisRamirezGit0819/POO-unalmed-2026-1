import tkinter as tk
from VentanasFigura import (
    VentanaCilindro, VentanaEsfera, VentanaPiramide,
    VentanaCubo, VentanaPrisma
)


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self._inicio()
        self.title("Figuras")
        self.geometry("400x160")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.winfo_width() // 2)
        y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")

    def _inicio(self):

        self._btn_cilindro = tk.Button(self, text="Cilindro",
                                        command=self._abrir_cilindro)
        self._btn_cilindro.place(x=20, y=50, width=80, height=23)

        self._btn_esfera = tk.Button(self, text="Esfera",
                                        command=self._abrir_esfera)
        self._btn_esfera.place(x=110, y=50, width=80, height=23)

        self._btn_piramide = tk.Button(self, text="Piramide",
                                        command=self._abrir_piramide)
        self._btn_piramide.place(x=200, y=50, width=90, height=23)

        self._btn_cubo = tk.Button(self, text="Cubo",
                                    command=self._abrir_cubo)
        self._btn_cubo.place(x=20, y=90, width=80, height=23)

        self._btn_prisma = tk.Button(self, text="Prisma",
                                        command=self._abrir_prisma)
        self._btn_prisma.place(x=110, y=90, width=80, height=23)

    def _abrir_cilindro(self):
        VentanaCilindro(self)

    def _abrir_esfera(self):
        VentanaEsfera(self)

    def _abrir_piramide(self):
        VentanaPiramide(self)

    def _abrir_cubo(self):
        VentanaCubo(self)

    def _abrir_prisma(self):
        VentanaPrisma(self)