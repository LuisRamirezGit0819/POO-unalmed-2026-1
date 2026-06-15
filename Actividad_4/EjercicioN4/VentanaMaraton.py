import tkinter as tk
from tkinter import messagebox
from EquipoMaraton import EquipoMaratonProgramacion
from Programador import Programador


BG_MAIN    = "#f0f0f0"
BG_DARK    = "#1a1a18"
BG_WHITE   = "#ffffff"
COLOR_OK   = "#188038"
COLOR_ERR  = "#d93025"
COLOR_MUTED = "#9e9e9e"


class CampoFormulario(tk.Frame):
    
    def __init__(self, parent, etiqueta: str, ocultar: bool = False):
        super().__init__(parent, bg=BG_MAIN)
        self._etiqueta_texto = etiqueta
        self._ocultar = ocultar
        self._construir()

    def _construir(self):
        self._lbl = tk.Label(
            self,
            text=self._etiqueta_texto,
            bg=BG_MAIN,
            fg="#1a1a18",
            font=("Helvetica", 9),
            width=22,
            anchor="w",
        )
        self._lbl.pack(side="left", padx=(0, 4))

        self._entry = tk.Entry(
            self,
            font=("Helvetica", 9),
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground="#b0b0b0",
            highlightcolor="#1a73e8",
            width=20,
            show="*" if self._ocultar else "",
        )
        self._entry.pack(side="left")

    def obtener(self) -> str:
        return self._entry.get().strip()

    def limpiar(self):
        self._entry.delete(0, tk.END)

    def enfocar(self):
        self._entry.focus_set()


class PanelEncabezado(tk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent, bg=BG_DARK, pady=10)
        self._construir()

    def _construir(self):
        self._lbl_titulo = tk.Label(
            self,
            text="Maratón de Programación",
            bg=BG_DARK,
            fg="#ffffff",
            font=("Helvetica", 13, "bold"),
        )
        self._lbl_titulo.pack()

        self._lbl_subtitulo = tk.Label(
            self,
            text="Registro de equipo con validación de datos y contraseña",
            bg=BG_DARK,
            fg=COLOR_MUTED,
            font=("Helvetica", 8),
        )
        self._lbl_subtitulo.pack()


class PanelEquipo(tk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent, bg=BG_MAIN, padx=16, pady=6)
        self._construir()

    def _construir(self):
        self._lbl_seccion = tk.Label(
            self,
            text="Datos del equipo",
            bg=BG_MAIN,
            fg="#555555",
            font=("Helvetica", 9, "bold"),
            anchor="w",
        )
        self._lbl_seccion.pack(fill="x", pady=(0, 4))

        self._campo_nombre_equipo = CampoFormulario(
            self, "Nombre del equipo:"
        )
        self._campo_nombre_equipo.pack(anchor="w", pady=2)

        self._campo_universidad = CampoFormulario(
            self, "Universidad:"
        )
        self._campo_universidad.pack(anchor="w", pady=2)

        self._campo_lenguaje = CampoFormulario(
            self, "Lenguaje de programación:"
        )
        self._campo_lenguaje.pack(anchor="w", pady=2)

    def obtener_nombre_equipo(self) -> str:
        return self._campo_nombre_equipo.obtener()

    def obtener_universidad(self) -> str:
        return self._campo_universidad.obtener()

    def obtener_lenguaje_programacion(self) -> str:
        return self._campo_lenguaje.obtener()

    def limpiar(self):
        self._campo_nombre_equipo.limpiar()
        self._campo_universidad.limpiar()
        self._campo_lenguaje.limpiar()
        self._campo_nombre_equipo.enfocar()



class PanelProgramador(tk.Frame):

    def __init__(self, parent, numero: int):
        super().__init__(parent, bg=BG_MAIN, padx=16, pady=3)
        self._numero = numero
        self._construir()

    def _construir(self):
        self._lbl_seccion = tk.Label(
            self,
            text=f"Integrante {self._numero}",
            bg=BG_MAIN,
            fg="#555555",
            font=("Helvetica", 8, "bold"),
            anchor="w",
        )
        self._lbl_seccion.pack(fill="x", pady=(0, 2))

        self._campo_nombre = CampoFormulario(
            self, f"  Nombre {self._numero}:"
        )
        self._campo_nombre.pack(anchor="w", pady=1)

        self._campo_apellidos = CampoFormulario(
            self, f"  Apellidos {self._numero}:"
        )
        self._campo_apellidos.pack(anchor="w", pady=1)

    def obtener_nombre(self) -> str:
        return self._campo_nombre.obtener()

    def obtener_apellidos(self) -> str:
        return self._campo_apellidos.obtener()

    def limpiar(self):
        self._campo_nombre.limpiar()
        self._campo_apellidos.limpiar()



class PanelContrasenna(tk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent, bg=BG_MAIN, padx=16, pady=6)
        self._construir()

    def _construir(self):
        self._lbl_seccion = tk.Label(
            self,
            text="Contraseña del equipo",
            bg=BG_MAIN,
            fg="#555555",
            font=("Helvetica", 9, "bold"),
            anchor="w",
        )
        self._lbl_seccion.pack(fill="x", pady=(0, 4))

        requisitos = (
            "• Mínimo 8 caracteres  • Sin espacios  "
            "• Mayúscula, minúscula, número y carácter especial"
        )
        self._lbl_requisitos = tk.Label(
            self,
            text=requisitos,
            bg=BG_MAIN,
            fg=COLOR_MUTED,
            font=("Helvetica", 7),
            anchor="w",
            wraplength=420,
            justify="left",
        )
        self._lbl_requisitos.pack(fill="x", pady=(0, 4))

        self._campo_contrasenna = CampoFormulario(
            self, "Contraseña:", ocultar=True
        )
        self._campo_contrasenna.pack(anchor="w", pady=2)

        self._campo_confirmacion = CampoFormulario(
            self, "Confirmar contraseña:", ocultar=True
        )
        self._campo_confirmacion.pack(anchor="w", pady=2)

    def obtener_contrasenna(self) -> str:
        return self._campo_contrasenna.obtener()

    def obtener_confirmacion(self) -> str:
        return self._campo_confirmacion.obtener()

    def limpiar(self):
        self._campo_contrasenna.limpiar()
        self._campo_confirmacion.limpiar()



class PanelBoton(tk.Frame):
    
    def __init__(self, parent, cmd_registrar, cmd_limpiar):
        super().__init__(parent, bg=BG_MAIN, pady=8)
        self._cmd_registrar = cmd_registrar
        self._cmd_limpiar = cmd_limpiar
        self._construir()

    def _construir(self):
        self._btn_registrar = tk.Button(
            self,
            text="Registrar equipo",
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
        super().__init__(parent, bg=BG_MAIN, padx=16, pady=6)
        self._labels: list[tk.Label] = []
        self._construir()

    def _construir(self):
        self._lbl_titulo = tk.Label(
            self,
            text="Equipo registrado:",
            bg=BG_MAIN,
            fg="#555555",
            font=("Helvetica", 9, "bold"),
            anchor="w",
        )
        self._lbl_titulo.pack(fill="x", pady=(0, 4))

        self._frame_datos = tk.Frame(
            self,
            bg=BG_WHITE,
            highlightthickness=1,
            highlightbackground="#e0e0e0",
            padx=12,
            pady=8,
        )
        self._frame_datos.pack(fill="x")

        self._lbl_vacio = tk.Label(
            self._frame_datos,
            text="Aun no se ha registrado ningun equipo.",
            bg=BG_WHITE,
            fg=COLOR_MUTED,
            font=("Helvetica", 9, "italic"),
            anchor="w",
        )
        self._lbl_vacio.pack(fill="x")

    def mostrar(self, equipo: EquipoMaratonProgramacion):
        for lbl in self._labels:
            lbl.destroy()
        self._labels.clear()
        self._lbl_vacio.pack_forget()

        lineas_equipo = [
            f"Equipo           : {equipo.nombre_equipo}",
            f"Universidad      : {equipo.universidad}",
            f"Lenguaje         : {equipo.lenguaje_programacion}",
            f"Integrantes      : {equipo.tamano_equipo}",
        ]
        for texto in lineas_equipo:
            lbl = tk.Label(
                self._frame_datos,
                text=texto,
                bg=BG_WHITE,
                fg=COLOR_OK,
                font=("Courier", 9, "bold"),
                anchor="w",
            )
            lbl.pack(fill="x")
            self._labels.append(lbl)

        sep = tk.Frame(self._frame_datos, height=1, bg="#e0e0e0")
        sep.pack(fill="x", pady=4)
        self._labels.append(sep)

        for i, prog in enumerate(equipo.programadores):
            if prog is not None:
                lbl = tk.Label(
                    self._frame_datos,
                    text=f"  Integrante {i+1}: {prog.nombre} {prog.apellidos}",
                    bg=BG_WHITE,
                    fg="#1a1a18",
                    font=("Courier", 9),
                    anchor="w",
                )
                lbl.pack(fill="x")
                self._labels.append(lbl)

    def limpiar(self):
        for lbl in self._labels:
            lbl.destroy()
        self._labels.clear()
        self._lbl_vacio.pack(fill="x")



class VentanaMaraton(tk.Tk):
    
    NUM_PROGRAMADORES = 3  

    def __init__(self):
        super().__init__()
        self.title("Maratón de Programación")
        self.geometry("520x680")
        self.resizable(False, True)
        self.configure(bg=BG_MAIN)
        self._construir_ui()
        self._centrar()


    def _construir_ui(self):
        self._panel_encabezado = PanelEncabezado(self)
        self._panel_encabezado.pack(fill="x")

        self._canvas = tk.Canvas(self, bg=BG_MAIN, highlightthickness=0)
        self._scrollbar = tk.Scrollbar(
            self, orient="vertical", command=self._canvas.yview
        )
        self._canvas.configure(yscrollcommand=self._scrollbar.set)

        self._scrollbar.pack(side="right", fill="y")
        self._canvas.pack(side="left", fill="both", expand=True)

        self._frame_scroll = tk.Frame(self._canvas, bg=BG_MAIN)
        self._canvas_window = self._canvas.create_window(
            (0, 0), window=self._frame_scroll, anchor="nw"
        )

        self._frame_scroll.bind(
            "<Configure>",
            lambda e: self._canvas.configure(
                scrollregion=self._canvas.bbox("all")
            ),
        )
        self._canvas.bind(
            "<Configure>",
            lambda e: self._canvas.itemconfig(
                self._canvas_window, width=e.width
            ),
        )
        self._canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self._panel_equipo = PanelEquipo(self._frame_scroll)
        self._panel_equipo.pack(fill="x")

        tk.Frame(self._frame_scroll, height=1, bg="#d0d0d0").pack(
            fill="x", padx=16, pady=2
        )

        self._paneles_programador: list[PanelProgramador] = []
        for i in range(self.NUM_PROGRAMADORES):
            panel = PanelProgramador(self._frame_scroll, numero=i + 1)
            panel.pack(fill="x")
            self._paneles_programador.append(panel)

        tk.Frame(self._frame_scroll, height=1, bg="#d0d0d0").pack(
            fill="x", padx=16, pady=2
        )

        self._panel_contrasenna = PanelContrasenna(self._frame_scroll)
        self._panel_contrasenna.pack(fill="x")

        tk.Frame(self._frame_scroll, height=1, bg="#d0d0d0").pack(
            fill="x", padx=16, pady=2
        )

        self._panel_boton = PanelBoton(
            self._frame_scroll,
            cmd_registrar=self._accion_registrar,
            cmd_limpiar=self._accion_limpiar,
        )
        self._panel_boton.pack()

        self._panel_resultado = PanelResultado(self._frame_scroll)
        self._panel_resultado.pack(fill="x")

    def _on_mousewheel(self, event):
        self._canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


    def _accion_registrar(self):
        
        nombre_equipo = self._panel_equipo.obtener_nombre_equipo()
        universidad   = self._panel_equipo.obtener_universidad()
        lenguaje      = self._panel_equipo.obtener_lenguaje_programacion()

        if not nombre_equipo:
            messagebox.showwarning("Campo vacio", "Ingrese el nombre del equipo.")
            return
        if not universidad:
            messagebox.showwarning("Campo vacio", "Ingrese la universidad.")
            return
        if not lenguaje:
            messagebox.showwarning("Campo vacio", "Ingrese el lenguaje de programacion.")
            return

        try:
            EquipoMaratonProgramacion.validar_campo(nombre_equipo)
        except Exception as e:
            messagebox.showerror("Nombre del equipo invalido", str(e))
            return
        try:
            EquipoMaratonProgramacion.validar_campo(universidad)
        except Exception as e:
            messagebox.showerror("Universidad invalida", str(e))
            return

        contrasenna  = self._panel_contrasenna.obtener_contrasenna()
        confirmacion = self._panel_contrasenna.obtener_confirmacion()

        if not contrasenna:
            messagebox.showwarning("Campo vacio", "Ingrese la contrasenna.")
            return
        if not confirmacion:
            messagebox.showwarning("Campo vacio", "Confirme la contrasenna.")
            return

        try:
            EquipoMaratonProgramacion.validar_contrasenna(contrasenna, confirmacion)
        except Exception as e:
            messagebox.showerror("Contrasenna invalida", str(e))
            return

        equipo = EquipoMaratonProgramacion(nombre_equipo, universidad, lenguaje)

        for i, panel in enumerate(self._paneles_programador):
            nombre_prog   = panel.obtener_nombre()
            apellidos_prog = panel.obtener_apellidos()

            if not nombre_prog:
                messagebox.showwarning(
                    "Campo vacio",
                    f"Ingrese el nombre del integrante {i + 1}."
                )
                return
            if not apellidos_prog:
                messagebox.showwarning(
                    "Campo vacio",
                    f"Ingrese los apellidos del integrante {i + 1}."
                )
                return

            try:
                EquipoMaratonProgramacion.validar_campo(nombre_prog)
            except Exception as e:
                messagebox.showerror(
                    f"Nombre invalido (Integrante {i + 1})", str(e)
                )
                return

            try:
                EquipoMaratonProgramacion.validar_campo(apellidos_prog)
            except Exception as e:
                messagebox.showerror(
                    f"Apellidos invalidos (Integrante {i + 1})", str(e)
                )
                return

            programador = Programador(nombre_prog, apellidos_prog)
            try:
                equipo.annadir(programador)
            except Exception as e:
                messagebox.showerror("Error al agregar programador", str(e))
                return

        self._panel_resultado.mostrar(equipo)

    def _accion_limpiar(self):
        self._panel_equipo.limpiar()
        for panel in self._paneles_programador:
            panel.limpiar()
        self._panel_contrasenna.limpiar()
        self._panel_resultado.limpiar()

    def _centrar(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  // 2) - (self.winfo_width()  // 2)
        y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")