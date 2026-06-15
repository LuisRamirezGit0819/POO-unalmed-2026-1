import tkinter as tk
from tkinter import messagebox
from CalculosNumericos import CalculosNumericos


COLOR_OK    = "#188038" 
COLOR_ERROR = "#d93025" 
COLOR_VACIO = "#9e9e9e" 


class PanelEncabezado(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#1a1a18", pady=12)
        self._construir()

    def _construir(self):
        self._lbl_titulo = tk.Label(
            self,
            text="Cálculos Numéricos",
            bg="#1a1a18",
            fg="#ffffff",
            font=("Helvetica", 14, "bold"),
        )
        self._lbl_titulo.pack()

        self._lbl_subtitulo = tk.Label(
            self,
            text="Logaritmo neperiano y raíz cuadrada con manejo de excepciones",
            bg="#1a1a18",
            fg="#9e9e9e",
            font=("Helvetica", 9),
        )
        self._lbl_subtitulo.pack()


class PanelEntrada(tk.Frame):

    def __init__(self, parent, cmd_calcular):
        super().__init__(parent, bg="#f0f0f0", pady=18, padx=24)
        self._cmd_calcular = cmd_calcular
        self._construir()

    def _construir(self):
        self._fila = tk.Frame(self, bg="#f0f0f0")
        self._fila.pack()

        self._lbl = tk.Label(
            self._fila,
            text="Valor numérico:",
            bg="#f0f0f0",
            fg="#1a1a18",
            font=("Helvetica", 10),
            width=18,
            anchor="w",
        )
        self._lbl.pack(side="left", padx=(0, 8))

        self._entry = tk.Entry(
            self._fila,
            font=("Helvetica", 10),
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground="#b0b0b0",
            highlightcolor="#1a73e8",
            width=20,
        )
        self._entry.pack(side="left")
        self._entry.bind("<Return>", lambda _: self._cmd_calcular())

        self._btn = tk.Button(
            self,
            text="Calcular",
            command=self._cmd_calcular,
            bg="#1a73e8",
            fg="#ffffff",
            activebackground="#1558b0",
            activeforeground="#ffffff",
            relief="flat",
            font=("Helvetica", 10, "bold"),
            padx=20,
            pady=5,
            cursor="hand2",
            bd=0,
        )
        self._btn.pack(pady=(10, 0))

    def obtener_valor(self) -> str:
        return self._entry.get().strip()

    def limpiar(self):
        self._entry.delete(0, tk.END)
        self._entry.focus_set()

    def enfocar(self):
        self._entry.focus_set()


class FilaResultado(tk.Frame):

    def __init__(self, parent, etiqueta: str):
        super().__init__(parent, bg="#ffffff", pady=6, padx=12)
        self._etiqueta_texto = etiqueta
        self._construir()

    def _construir(self):
        self._lbl_etiqueta = tk.Label(
            self,
            text=self._etiqueta_texto,
            bg="#ffffff",
            fg="#555555",
            font=("Helvetica", 9, "bold"),
            width=22,
            anchor="w",
        )
        self._lbl_etiqueta.pack(side="left")

        self._lbl_valor = tk.Label(
            self,
            text="—",
            bg="#ffffff",
            fg=COLOR_VACIO,
            font=("Courier", 10),
            anchor="w",
        )
        self._lbl_valor.pack(side="left", fill="x", expand=True)

    def mostrar_ok(self, texto: str):
        self._lbl_valor.config(text=texto, fg=COLOR_OK)

    def mostrar_error(self, texto: str):
        self._lbl_valor.config(text=texto, fg=COLOR_ERROR)

    def limpiar(self):
        self._lbl_valor.config(text="—", fg=COLOR_VACIO)


class PanelResultados(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f0f0f0", padx=20, pady=8)
        self._construir()

    def _construir(self):
        self._lbl_titulo = tk.Label(
            self,
            text="Resultados:",
            bg="#f0f0f0",
            fg="#555555",
            font=("Helvetica", 9, "bold"),
            anchor="w",
        )
        self._lbl_titulo.pack(fill="x", pady=(0, 4))

        self._frame_filas = tk.Frame(
            self,
            bg="#ffffff",
            highlightthickness=1,
            highlightbackground="#e0e0e0",
        )
        self._frame_filas.pack(fill="x")

        self._fila_log = FilaResultado(
            self._frame_filas,
            "Logaritmo neperiano:",
        )
        self._fila_log.pack(fill="x")

        tk.Frame(self._frame_filas, height=1, bg="#e0e0e0").pack(fill="x")

        self._fila_raiz = FilaResultado(
            self._frame_filas,
            "Raiz cuadrada:",
        )
        self._fila_raiz.pack(fill="x")

    def mostrar(
        self,
        res_log: str, err_log: str,
        res_raiz: str, err_raiz: str,
    ):
        if res_log:
            self._fila_log.mostrar_ok(res_log)
        else:
            self._fila_log.mostrar_error(err_log)

        if res_raiz:
            self._fila_raiz.mostrar_ok(res_raiz)
        else:
            self._fila_raiz.mostrar_error(err_raiz)

    def limpiar(self):
        self._fila_log.limpiar()
        self._fila_raiz.limpiar()


class VentanaCalculos(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Cálculos Numéricos")
        self.geometry("500x340")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")
        self._construir_ui()
        self._centrar()

    def _construir_ui(self):
        self._panel_encabezado = PanelEncabezado(self)
        self._panel_encabezado.pack(fill="x")

        self._panel_entrada = PanelEntrada(
            self,
            cmd_calcular=self._accion_calcular,
        )
        self._panel_entrada.pack(fill="x")

        tk.Frame(self, height=1, bg="#d0d0d0").pack(fill="x")

        self._panel_resultados = PanelResultados(self)
        self._panel_resultados.pack(fill="x")

    def _accion_calcular(self):
        valor_str = self._panel_entrada.obtener_valor()

        if not valor_str:
            messagebox.showwarning(
                "Campo vacio",
                "Por favor ingrese un valor numerico."
            )
            self._panel_entrada.enfocar()
            return

        try:
            valor = float(valor_str)
        except ValueError:
            messagebox.showerror(
                "Dato invalido",
                f'"{valor_str}" no es un numero valido.\n'
                "Ingrese un valor numerico (ej: 25, 3.14)."
            )
            self._panel_entrada.limpiar()
            return

        res_log, err_log   = CalculosNumericos.calcular_logaritmo_neperiano(valor)
        res_raiz, err_raiz = CalculosNumericos.calcular_raiz_cuadrada(valor)

        self._panel_resultados.mostrar(res_log, err_log, res_raiz, err_raiz)

    def _centrar(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  // 2) - (self.winfo_width()  // 2)
        y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")
