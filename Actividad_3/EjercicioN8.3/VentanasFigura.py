import math
import tkinter as tk
from tkinter import messagebox
from Figuras import Cilindro, Esfera, Piramide, Cubo, Prisma

def _dibujar_cilindro(canvas: tk.Canvas):

    canvas.delete("all")

    canvas.create_rectangle(30, 30, 110, 110, fill="#a8d8ea", outline="#2c7da0", width=2)

    canvas.create_oval(30, 20, 110, 44, fill="#cce8f4", outline="#2c7da0", width=2)

    canvas.create_oval(30, 96, 110, 120, fill="#a8d8ea", outline="#2c7da0", width=2)


def _dibujar_esfera(canvas: tk.Canvas):

    canvas.delete("all")
    canvas.create_oval(20, 10, 120, 110, fill="#f9c784", outline="#d4a017", width=2)

    canvas.create_oval(20, 52, 120, 68, outline="#d4a017", width=1, dash=(4, 3))


def _dibujar_piramide(canvas: tk.Canvas):
    """Dibuja una piramide esquematica en el canvas."""
    canvas.delete("all")

    canvas.create_polygon(70, 10, 15, 110, 125, 110,
                            fill="#b7e4c7", outline="#2d6a4f", width=2)

    canvas.create_oval(15, 100, 125, 120, fill="#95d5b2", outline="#2d6a4f", width=2)


def _dibujar_cubo(canvas: tk.Canvas):

    canvas.delete("all")

    canvas.create_rectangle(20, 40, 90, 110, fill="#e2b4bd", outline="#7b2d8b", width=2)

    canvas.create_polygon(20, 40, 50, 15, 120, 15, 90, 40,
                            fill="#f2d0d7", outline="#7b2d8b", width=2)

    canvas.create_polygon(90, 40, 120, 15, 120, 85, 90, 110,
                            fill="#d198a8", outline="#7b2d8b", width=2)


def _dibujar_prisma(canvas: tk.Canvas):

    canvas.delete("all")

    canvas.create_polygon(15, 50, 40, 20, 110, 20, 85, 50,
                            fill="#ddd0f5", outline="#4a2c8a", width=2)

    canvas.create_polygon(85, 50, 110, 20, 110, 80, 85, 110,
                            fill="#b09ed8", outline="#4a2c8a", width=2)

    canvas.create_rectangle(15, 50, 85, 110, 
                            fill="#c9b8e8", outline="#4a2c8a", width=2)



class _VentanaFigura(tk.Toplevel):

    def __init__(self, titulo: str, ancho: int, alto: int,
                    funcion_dibujo, parent=None):
        super().__init__(parent)
        self.title(titulo)
        self.geometry(f"{ancho}x{alto}")
        self.resizable(False, False)
        self._funcion_dibujo = funcion_dibujo
        self._label_volumen = None
        self._label_superficie = None

    def _centrar(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.winfo_width() // 2)
        y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")

    def _agregar_canvas(self, frame: tk.Frame):
        canvas = tk.Canvas(frame, width=140, height=130, bg="#f5f5f5",
                            highlightthickness=1, highlightbackground="#cccccc")
        canvas.pack(pady=(8, 4))
        self._funcion_dibujo(canvas)

    def _agregar_resultados(self, frame: tk.Frame):
        self._label_volumen = tk.Label(frame, text="Volumen (cm3):")
        self._label_volumen.pack(anchor="w", padx=12)
        self._label_superficie = tk.Label(frame, text="Superficie (cm2):")
        self._label_superficie.pack(anchor="w", padx=12)

    def _mostrar_error(self, campo: str = ""):
        if campo:
            messagebox.showerror(
                "Dato invalido",
                f"El campo \"{campo}\" no es un numero valido.\n"
                "Por favor ingrese solo valores numericos."
            )
        else:
            messagebox.showerror(
                "Error",
                "Campo nulo o error en formato de numero."
            )


class VentanaCilindro(_VentanaFigura):

    def __init__(self, parent=None):
        super().__init__("Cilindro", 280, 330, _dibujar_cilindro, parent)
        self._inicio()
        self._centrar()

    def _inicio(self):
        self._agregar_canvas(self)

        self._radio_lbl = tk.Label(self, text="Radio (cms):")
        self._radio_lbl.place(x=20, y=145, width=135, height=23)
        self._campo_radio = tk.Entry(self)
        self._campo_radio.place(x=120, y=145, width=135, height=23)

        self._altura_lbl = tk.Label(self, text="Altura (cms):")
        self._altura_lbl.place(x=20, y=175, width=135, height=23)
        self._campo_altura = tk.Entry(self)
        self._campo_altura.place(x=120, y=175, width=135, height=23)

        self._btn_calcular = tk.Button(self, text="Calcular",
                                        command=self._accion_calcular)
        self._btn_calcular.place(x=100, y=205, width=135, height=23)

        self._label_volumen = tk.Label(self, text="Volumen (cm3):")
        self._label_volumen.place(x=20, y=240, width=230, height=23)

        self._label_superficie = tk.Label(self, text="Superficie (cm2):")
        self._label_superficie.place(x=20, y=268, width=230, height=23)

    def _accion_calcular(self):
        try:
            radio = float(self._campo_radio.get())
            altura = float(self._campo_altura.get())
        except ValueError:
            self._mostrar_error("Radio o Altura")
            return
        cilindro = Cilindro(radio, altura)
        self._label_volumen.config(
            text=f"Volumen (cm3): {cilindro.calcular_volumen():.2f}")
        self._label_superficie.config(
            text=f"Superficie (cm2): {cilindro.calcular_superficie():.2f}")



class VentanaEsfera(_VentanaFigura):

    def __init__(self, parent=None):
        super().__init__("Esfera", 280, 300, _dibujar_esfera, parent)
        self._inicio()
        self._centrar()

    def _inicio(self):
        self._agregar_canvas(self)

        self._radio_lbl = tk.Label(self, text="Radio (cms):")
        self._radio_lbl.place(x=20, y=150, width=135, height=23)
        self._campo_radio = tk.Entry(self)
        self._campo_radio.place(x=120, y=150, width=135, height=23)

        self._btn_calcular = tk.Button(self, text="Calcular",
                                        command=self._accion_calcular)
        self._btn_calcular.place(x=100, y=180, width=135, height=23)

        self._label_volumen = tk.Label(self, text="Volumen (cm3):")
        self._label_volumen.place(x=20, y=220, width=230, height=23)

        self._label_superficie = tk.Label(self, text="Superficie (cm2):")
        self._label_superficie.place(x=20, y=248, width=230, height=23)

    def _accion_calcular(self):
        try:
            radio = float(self._campo_radio.get())
        except ValueError:
            self._mostrar_error("Radio")
            return
        esfera = Esfera(radio)
        self._label_volumen.config(
            text=f"Volumen (cm3): {esfera.calcular_volumen():.2f}")
        self._label_superficie.config(
            text=f"Superficie (cm2): {esfera.calcular_superficie():.2f}")


class VentanaPiramide(_VentanaFigura):

    def __init__(self, parent=None):
        super().__init__("Piramide", 280, 360, _dibujar_piramide, parent)
        self._inicio()
        self._centrar()

    def _inicio(self):
        self._agregar_canvas(self)

        self._base_lbl = tk.Label(self, text="Base (cms):")
        self._base_lbl.place(x=20, y=148, width=135, height=23)
        self._campo_base = tk.Entry(self)
        self._campo_base.place(x=120, y=148, width=135, height=23)

        self._altura_lbl = tk.Label(self, text="Altura (cms):")
        self._altura_lbl.place(x=20, y=178, width=135, height=23)
        self._campo_altura = tk.Entry(self)
        self._campo_altura.place(x=120, y=178, width=135, height=23)

        self._apotema_lbl = tk.Label(self, text="Apotema (cms):")
        self._apotema_lbl.place(x=20, y=208, width=135, height=23)
        self._campo_apotema = tk.Entry(self)
        self._campo_apotema.place(x=120, y=208, width=135, height=23)

        self._btn_calcular = tk.Button(self, text="Calcular",
                                        command=self._accion_calcular)
        self._btn_calcular.place(x=120, y=238, width=135, height=23)

        self._label_volumen = tk.Label(self, text="Volumen (cm3):")
        self._label_volumen.place(x=20, y=278, width=230, height=23)

        self._label_superficie = tk.Label(self, text="Superficie (cm2):")
        self._label_superficie.place(x=20, y=306, width=230, height=23)

    def _accion_calcular(self):
        try:
            base = float(self._campo_base.get())
            altura = float(self._campo_altura.get())
            apotema = float(self._campo_apotema.get())
        except ValueError:
            self._mostrar_error("Base, Altura o Apotema")
            return
        piramide = Piramide(base, altura, apotema)
        self._label_volumen.config(
            text=f"Volumen (cm3): {piramide.calcular_volumen():.2f}")
        self._label_superficie.config(
            text=f"Superficie (cm2): {piramide.calcular_superficie():.2f}")


class VentanaCubo(_VentanaFigura):

    def __init__(self, parent=None):
        super().__init__("Cubo", 280, 290, _dibujar_cubo, parent)
        self._inicio()
        self._centrar()

    def _inicio(self):
        self._agregar_canvas(self)

        self._lado_lbl = tk.Label(self, text="Lado (cms):")
        self._lado_lbl.place(x=20, y=150, width=135, height=23)
        self._campo_lado = tk.Entry(self)
        self._campo_lado.place(x=120, y=150, width=135, height=23)

        self._btn_calcular = tk.Button(self, text="Calcular",
                                        command=self._accion_calcular)
        self._btn_calcular.place(x=100, y=180, width=135, height=23)

        self._label_volumen = tk.Label(self, text="Volumen (cm3):")
        self._label_volumen.place(x=20, y=218, width=230, height=23)

        self._label_superficie = tk.Label(self, text="Superficie (cm2):")
        self._label_superficie.place(x=20, y=246, width=230, height=23)

    def _accion_calcular(self):
        try:
            lado = float(self._campo_lado.get())
        except ValueError:
            self._mostrar_error("Lado")
            return
        cubo = Cubo(lado)
        self._label_volumen.config(
            text=f"Volumen (cm3): {cubo.calcular_volumen():.2f}")
        self._label_superficie.config(
            text=f"Superficie (cm2): {cubo.calcular_superficie():.2f}")


class VentanaPrisma(_VentanaFigura):

    def __init__(self, parent=None):
        super().__init__("Prisma", 280, 360, _dibujar_prisma, parent)
        self._inicio()
        self._centrar()

    def _inicio(self):
        self._agregar_canvas(self)

        self._base_lbl = tk.Label(self, text="Base (cms):")
        self._base_lbl.place(x=20, y=148, width=135, height=23)
        self._campo_base = tk.Entry(self)
        self._campo_base.place(x=120, y=148, width=135, height=23)

        self._ancho_lbl = tk.Label(self, text="Ancho (cms):")
        self._ancho_lbl.place(x=20, y=178, width=135, height=23)
        self._campo_ancho = tk.Entry(self)
        self._campo_ancho.place(x=120, y=178, width=135, height=23)

        self._altura_lbl = tk.Label(self, text="Altura (cms):")
        self._altura_lbl.place(x=20, y=208, width=135, height=23)
        self._campo_altura = tk.Entry(self)
        self._campo_altura.place(x=120, y=208, width=135, height=23)

        self._btn_calcular = tk.Button(self, text="Calcular",
                                        command=self._accion_calcular)
        self._btn_calcular.place(x=120, y=238, width=135, height=23)

        self._label_volumen = tk.Label(self, text="Volumen (cm3):")
        self._label_volumen.place(x=20, y=278, width=230, height=23)

        self._label_superficie = tk.Label(self, text="Superficie (cm2):")
        self._label_superficie.place(x=20, y=306, width=230, height=23)

    def _accion_calcular(self):
        try:
            base = float(self._campo_base.get())
            ancho = float(self._campo_ancho.get())
            altura = float(self._campo_altura.get())
        except ValueError:
            self._mostrar_error("Base, Ancho o Altura")
            return
        prisma = Prisma(base, ancho, altura)
        self._label_volumen.config(
            text=f"Volumen (cm3): {prisma.calcular_volumen():.2f}")
        self._label_superficie.config(
            text=f"Superficie (cm2): {prisma.calcular_superficie():.2f}")