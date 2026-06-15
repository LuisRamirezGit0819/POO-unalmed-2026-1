import tkinter as tk
from tkinter import messagebox, filedialog, font as tkfont
from LeerArchivo import LeerArchivo


BG_MAIN    = "#f0f0f0"
BG_DARK    = "#1a1a18"
BG_WHITE   = "#ffffff"
COLOR_OK   = "#188038"
COLOR_ERR  = "#d93025"
COLOR_MUTED = "#9e9e9e"



class PanelEncabezado(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg=BG_DARK, pady=10)
        self._construir()

    def _construir(self):
        self._lbl_titulo = tk.Label(
            self,
            text="Lector de Archivos",
            bg=BG_DARK,
            fg="#ffffff",
            font=("Helvetica", 13, "bold"),
        )
        self._lbl_titulo.pack()

        self._lbl_subtitulo = tk.Label(
            self,
            text="Lectura de archivos .txt con manejo de excepciones",
            bg=BG_DARK,
            fg=COLOR_MUTED,
            font=("Helvetica", 8),
        )
        self._lbl_subtitulo.pack()


class PanelRuta(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg=BG_MAIN, padx=14, pady=10)
        self._construir()

    def _construir(self):
        self._lbl = tk.Label(
            self,
            text="Ruta del archivo .txt:",
            bg=BG_MAIN,
            fg="#555555",
            font=("Helvetica", 9, "bold"),
            anchor="w",
        )
        self._lbl.pack(fill="x", pady=(0, 4))

        self._fila = tk.Frame(self, bg=BG_MAIN)
        self._fila.pack(fill="x")

        self._entry = tk.Entry(
            self._fila,
            font=("Helvetica", 9),
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground="#b0b0b0",
            highlightcolor="#1a73e8",
        )
        self._entry.pack(side="left", fill="x", expand=True, padx=(0, 6))
        self._entry.bind("<Return>", lambda _: None)  

        self._btn_explorar = tk.Button(
            self._fila,
            text="Explorar...",
            command=self._accion_explorar,
            bg="#e0e0e0",
            fg="#1a1a18",
            activebackground="#c0c0c0",
            relief="flat",
            font=("Helvetica", 9),
            padx=10,
            pady=3,
            cursor="hand2",
            bd=0,
        )
        self._btn_explorar.pack(side="left")

    def _accion_explorar(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
        )
        if ruta:
            self.establecer_ruta(ruta)

    def obtener_ruta(self) -> str:
        return self._entry.get().strip()

    def limpiar(self):
        self._entry.delete(0, tk.END)

    def establecer_ruta(self, ruta: str):
        self._entry.delete(0, tk.END)
        self._entry.insert(0, ruta)

    def enlazar_enter(self, callback):
        self._entry.bind("<Return>", lambda _: callback())



class PanelBotones(tk.Frame):

    def __init__(self, parent, cmd_leer, cmd_mayusculas, cmd_limpiar):
        super().__init__(parent, bg=BG_MAIN, pady=8)
        self._cmd_leer        = cmd_leer
        self._cmd_mayusculas  = cmd_mayusculas
        self._cmd_limpiar     = cmd_limpiar
        self._construir()

    def _construir(self):
        self._btn_leer = tk.Button(
            self,
            text="Leer archivo",
            command=self._cmd_leer,
            bg="#1a73e8",
            fg="#ffffff",
            activebackground="#1558b0",
            activeforeground="#ffffff",
            relief="flat",
            font=("Helvetica", 9, "bold"),
            padx=14,
            pady=5,
            cursor="hand2",
            bd=0,
        )
        self._btn_leer.pack(side="left", padx=5)

        self._btn_mayusculas = tk.Button(
            self,
            text="Leer en mayúsculas",
            command=self._cmd_mayusculas,
            bg="#188038",
            fg="#ffffff",
            activebackground="#0f5a27",
            activeforeground="#ffffff",
            relief="flat",
            font=("Helvetica", 9, "bold"),
            padx=14,
            pady=5,
            cursor="hand2",
            bd=0,
        )
        self._btn_mayusculas.pack(side="left", padx=5)

        self._btn_limpiar = tk.Button(
            self,
            text="Limpiar",
            command=self._cmd_limpiar,
            bg="#e0e0e0",
            fg="#1a1a18",
            activebackground="#c0c0c0",
            relief="flat",
            font=("Helvetica", 9),
            padx=14,
            pady=5,
            cursor="hand2",
            bd=0,
        )
        self._btn_limpiar.pack(side="left", padx=5)


class PanelContenido(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg=BG_MAIN, padx=14, pady=4)
        self._construir()

    def _construir(self):
        self._lbl_estado = tk.Label(
            self,
            text="Sin archivo cargado",
            bg=BG_MAIN,
            fg=COLOR_MUTED,
            font=("Helvetica", 8, "italic"),
            anchor="w",
        )
        self._lbl_estado.pack(fill="x", pady=(0, 4))

        self._frame_txt = tk.Frame(self, bg=BG_MAIN)
        self._frame_txt.pack(fill="both", expand=True)

        fuente_mono = tkfont.Font(family="Courier", size=10)

        self._txt = tk.Text(
            self._frame_txt,
            state="disabled",
            wrap="none",           
            font=fuente_mono,
            bg="#fafafa",
            fg="#1a1a18",
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground="#e0e0e0",
            cursor="arrow",
            pady=6,
            padx=8,
        )

        self._sb_v = tk.Scrollbar(
            self._frame_txt,
            orient="vertical",
            command=self._txt.yview,
        )
        self._sb_h = tk.Scrollbar(
            self._frame_txt,
            orient="horizontal",
            command=self._txt.xview,
        )
        self._txt.configure(
            yscrollcommand=self._sb_v.set,
            xscrollcommand=self._sb_h.set,
        )

        self._sb_v.pack(side="right",  fill="y")
        self._sb_h.pack(side="bottom", fill="x")
        self._txt.pack(side="left", fill="both", expand=True)

        self._txt.tag_configure("normal",     foreground="#1a1a18")
        self._txt.tag_configure("mayusculas", foreground="#0f5a27")

    def mostrar(self, lineas: list[str], modo: str, nombre_archivo: str):
        self._txt.configure(state="normal")
        self._txt.delete("1.0", "end")

        tag = "mayusculas" if modo == "mayusculas" else "normal"
        for linea in lineas:
            self._txt.insert("end", linea + "\n", tag)

        self._txt.configure(state="disabled")

        modo_texto = " [MAYÚSCULAS]" if modo == "mayusculas" else ""
        self._lbl_estado.config(
            text=f"{nombre_archivo}{modo_texto}  —  {len(lineas)} lineas",
            fg=COLOR_OK if modo == "mayusculas" else "#1a73e8",
        )

    def limpiar(self):
        self._txt.configure(state="normal")
        self._txt.delete("1.0", "end")
        self._txt.configure(state="disabled")
        self._lbl_estado.config(
            text="Sin archivo cargado",
            fg=COLOR_MUTED,
        )


class VentanaArchivos(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Lector de Archivos")
        self.geometry("640x520")
        self.resizable(True, True)
        self.configure(bg=BG_MAIN)
        self._construir_ui()
        self._centrar()

    def _construir_ui(self):
        self._panel_encabezado = PanelEncabezado(self)
        self._panel_encabezado.pack(fill="x")

        self._panel_ruta = PanelRuta(self)
        self._panel_ruta.pack(fill="x")
        self._panel_ruta.enlazar_enter(self._accion_leer)

        self._panel_botones = PanelBotones(
            self,
            cmd_leer=self._accion_leer,
            cmd_mayusculas=self._accion_leer_mayusculas,
            cmd_limpiar=self._accion_limpiar,
        )
        self._panel_botones.pack()

        tk.Frame(self, height=1, bg="#d0d0d0").pack(fill="x")

        self._panel_contenido = PanelContenido(self)
        self._panel_contenido.pack(fill="both", expand=True)


    def _validar_ruta(self) -> str | None:
        ruta = self._panel_ruta.obtener_ruta()
        if not ruta:
            messagebox.showwarning(
                "Campo vacio",
                "Ingrese la ruta del archivo o use 'Explorar...' "
                "para seleccionarlo."
            )
            return None
        return ruta

    def _accion_leer(self):
        ruta = self._validar_ruta()
        if ruta is None:
            return

        lineas, error = LeerArchivo.leer(ruta)

        if error:
            messagebox.showerror("Error de lectura", error)
            return

        self._panel_contenido.mostrar(lineas, "normal", ruta)

    def _accion_leer_mayusculas(self):
        ruta = self._validar_ruta()
        if ruta is None:
            return

        lineas, error = LeerArchivo.leer_en_mayusculas(ruta)

        if error:
            messagebox.showerror("Error de lectura", error)
            return

        self._panel_contenido.mostrar(lineas, "mayusculas", ruta)

    def _accion_limpiar(self):
        self._panel_ruta.limpiar()
        self._panel_contenido.limpiar()

    def _centrar(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  // 2) - (self.winfo_width()  // 2)
        y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")