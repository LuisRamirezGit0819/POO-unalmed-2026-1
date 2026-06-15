import tkinter as tk
from tkinter import messagebox
from PruebaExcepciones import PruebaExcepciones

MENSAJES_ERROR = {"Division por cero", "Debe ingresar ambos valores.", "Ocurrio una excepcion"}


class VentanaExcepciones(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Prueba de Excepciones")
        self.geometry("280x200")
        self.resizable(False, False)
        self._construir_ui()

    def _construir_ui(self):
        tk.Label(self, text="Dividendo:").pack(pady=(16, 0))
        self._entrada_dividendo = tk.Entry(self)
        self._entrada_dividendo.pack()

        tk.Label(self, text="Divisor:").pack(pady=(8, 0))
        self._entrada_divisor = tk.Entry(self)
        self._entrada_divisor.pack()

        self._lbl_resultado = tk.Label(self, text="")
        self._lbl_resultado.pack(pady=(10, 0))

        tk.Button(self, text="Ejecutar", command=self._accion_ejecutar).pack(pady=(10, 0))
        tk.Button(self, text="Limpiar",  command=self._accion_limpiar).pack(pady=(6, 0))

    def _accion_ejecutar(self):
        dividendo = self._entrada_dividendo.get()
        divisor   = self._entrada_divisor.get()
        mensajes  = PruebaExcepciones.ejecutar(dividendo, divisor)

        self._lbl_resultado.config(text="")

        for mensaje in mensajes:
            if mensaje in MENSAJES_ERROR:
                messagebox.showerror("Excepcion capturada", mensaje)
                return
            if mensaje.startswith("Resultado:"):
                self._lbl_resultado.config(text=mensaje)

    def _accion_limpiar(self):
        self._entrada_dividendo.delete(0, "end")
        self._entrada_divisor.delete(0, "end")
        self._lbl_resultado.config(text="")