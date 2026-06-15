import tkinter as tk
from tkinter import messagebox
from Vendedor import Vendedor

class CampoFormulario(tk.Frame):

    def __init__(self, parent, etiqueta: str):
        super().__init__(parent, bg="#f0f0f0")
        self._etiqueta_texto = etiqueta
        self._construir()

    def _construir(self):
        self._lbl = tk.Label(
            self,
            text=self._etiqueta_texto,
            bg="#f0f0f0",
            fg="#1a1a18",
            font=("Helvetica", 10),
            width=22,
            anchor="w",
        )
        self._lbl.pack(side="left", padx=(0, 6))

        self._entry = tk.Entry(
            self,
            font=("Helvetica", 10),
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground="#b0b0b0",
            highlightcolor="#1a73e8",
            width=22,
        )
        self._entry.pack(side="left")

    def obtener(self) -> str:
        return self._entry.get().strip()

    def limpiar(self):
        """Borra el contenido del campo."""
        self._entry.delete(0, tk.END)

    def enfocar(self):
        """Coloca el foco del teclado en este campo."""
        self._entry.focus_set()


class PanelEncabezado(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#1a1a18", pady=12)
        self._construir()

    def _construir(self):
        self._lbl_titulo = tk.Label(
            self,
            text="Registro de Vendedor",
            bg="#1a1a18",
            fg="#ffffff",
            font=("Helvetica", 14, "bold"),
        )
        self._lbl_titulo.pack()

        self._lbl_subtitulo = tk.Label(
            self,
            text="Verificacion de edad con manejo de excepciones",
            bg="#1a1a18",
            fg="#9e9e9e",
            font=("Helvetica", 9),
        )
        self._lbl_subtitulo.pack()


class PanelFormulario(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f0f0f0", pady=16, padx=20)
        self._construir()

    def _construir(self):
        self._campo_nombre = CampoFormulario(self, "Nombre del vendedor:")
        self._campo_nombre.pack(pady=5)

        self._campo_apellidos = CampoFormulario(self, "Apellidos del vendedor:")
        self._campo_apellidos.pack(pady=5)

        self._campo_edad = CampoFormulario(self, "Edad del vendedor:")
        self._campo_edad.pack(pady=5)

    def obtener_nombre(self) -> str:
        return self._campo_nombre.obtener()

    def obtener_apellidos(self) -> str:
        return self._campo_apellidos.obtener()

    def obtener_edad(self) -> str:
        return self._campo_edad.obtener()

    def limpiar(self):
        self._campo_nombre.limpiar()
        self._campo_apellidos.limpiar()
        self._campo_edad.limpiar()
        self._campo_nombre.enfocar()

    def enfocar_nombre(self):
        self._campo_nombre.enfocar()


class PanelBoton(tk.Frame):

    def __init__(self, parent, cmd_registrar, cmd_limpiar):
        super().__init__(parent, bg="#f0f0f0", pady=10)
        self._cmd_registrar = cmd_registrar
        self._cmd_limpiar = cmd_limpiar
        self._construir()

    def _construir(self):
        self._btn_registrar = tk.Button(
            self,
            text="Registrar",
            command=self._cmd_registrar,
            bg="#1a73e8",
            fg="#ffffff",
            activebackground="#1558b0",
            activeforeground="#ffffff",
            relief="flat",
            font=("Helvetica", 10, "bold"),
            padx=16,
            pady=5,
            cursor="hand2",
            bd=0,
        )
        self._btn_registrar.pack(side="left", padx=6)

        self._btn_limpiar = tk.Button(
            self,
            text="Limpiar",
            command=self._cmd_limpiar,
            bg="#e0e0e0",
            fg="#1a1a18",
            activebackground="#c0c0c0",
            relief="flat",
            font=("Helvetica", 10),
            padx=16,
            pady=5,
            cursor="hand2",
            bd=0,
        )
        self._btn_limpiar.pack(side="left", padx=6)


class PanelResultado(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f0f0f0", padx=20, pady=10)
        self._labels: list[tk.Label] = []
        self._construir()

    def _construir(self):
        self._lbl_titulo = tk.Label(
            self,
            text="Datos registrados:",
            bg="#f0f0f0",
            fg="#555555",
            font=("Helvetica", 9, "bold"),
            anchor="w",
        )
        self._lbl_titulo.pack(fill="x")

        self._frame_datos = tk.Frame(
            self,
            bg="#ffffff",
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground="#e0e0e0",
            padx=12,
            pady=8,
        )
        self._frame_datos.pack(fill="x", pady=(4, 0))

        self._lbl_vacio = tk.Label(
            self._frame_datos,
            text="Aun no se ha registrado ningun vendedor.",
            bg="#ffffff",
            fg="#9e9e9e",
            font=("Helvetica", 9, "italic"),
            anchor="w",
        )
        self._lbl_vacio.pack(fill="x")

    def mostrar(self, lineas: list[str]):
        for lbl in self._labels:
            lbl.destroy()
        self._labels.clear()

        self._lbl_vacio.pack_forget()

        for linea in lineas:
            lbl = tk.Label(
                self._frame_datos,
                text=linea,
                bg="#ffffff",
                fg="#1a1a18",
                font=("Courier", 10),
                anchor="w",
            )
            lbl.pack(fill="x")
            self._labels.append(lbl)

    def limpiar(self):
        for lbl in self._labels:
            lbl.destroy()
        self._labels.clear()
        self._lbl_vacio.pack(fill="x")


class VentanaVendedor(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Vendedor")
        self.geometry("480x440")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")
        self._construir_ui()
        self._centrar()

    def _construir_ui(self):
        self._panel_encabezado = PanelEncabezado(self)
        self._panel_encabezado.pack(fill="x")

        self._panel_formulario = PanelFormulario(self)
        self._panel_formulario.pack(fill="x")

        self._panel_boton = PanelBoton(
            self,
            cmd_registrar=self._accion_registrar,
            cmd_limpiar=self._accion_limpiar,
        )
        self._panel_boton.pack()

        tk.Frame(self, height=1, bg="#d0d0d0").pack(fill="x", pady=(6, 0))

        self._panel_resultado = PanelResultado(self)
        self._panel_resultado.pack(fill="x", padx=0)

    def _accion_registrar(self):
        nombre = self._panel_formulario.obtener_nombre()
        apellidos = self._panel_formulario.obtener_apellidos()
        edad_str = self._panel_formulario.obtener_edad()

        if not nombre:
            messagebox.showwarning(
                "Campo vacio",
                "El campo 'Nombre del vendedor' es obligatorio."
            )
            self._panel_formulario.enfocar_nombre()
            return
        if not apellidos:
            messagebox.showwarning(
                "Campo vacio",
                "El campo 'Apellidos del vendedor' es obligatorio."
            )
            return
        if not edad_str:
            messagebox.showwarning(
                "Campo vacio",
                "El campo 'Edad del vendedor' es obligatorio."
            )
            return

        try:
            edad = int(edad_str)
        except ValueError:
            messagebox.showerror(
                "Dato invalido",
                f"La edad \"{edad_str}\" no es un numero entero valido."
            )
            return

        vendedor = Vendedor(nombre, apellidos)
        try:
            vendedor.verificar_edad(edad)
        except ValueError as e:
            messagebox.showerror("Edad invalida", str(e))
            return

        lineas = vendedor.imprimir()
        self._panel_resultado.mostrar(lineas)

    def _accion_limpiar(self):
        self._panel_formulario.limpiar()
        self._panel_resultado.limpiar()

    def _centrar(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  // 2) - (self.winfo_width()  // 2)
        y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")
