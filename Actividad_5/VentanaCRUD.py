import tkinter as tk
from tkinter import ttk, messagebox
from GestorContactos import GestorContactos
from Contacto import Contacto


BG_MAIN    = "#f0f0f0"
BG_DARK    = "#1a1a18"
BG_WHITE   = "#ffffff"
COLOR_CREATE = "#1a73e8"
COLOR_READ   = "#188038"
COLOR_UPDATE = "#e37400"
COLOR_DELETE = "#d93025"
COLOR_MUTED  = "#9e9e9e"
COLOR_OK     = "#188038"
COLOR_ERR    = "#d93025"



class CampoFormulario(tk.Frame):
    
    def __init__(self, parent, etiqueta: str, ancho_entry: int = 24):
        super().__init__(parent, bg=BG_MAIN)
        self._etiqueta_texto = etiqueta
        self._ancho_entry = ancho_entry
        self._construir()

    def _construir(self):
        self._lbl = tk.Label(
            self,
            text=self._etiqueta_texto,
            bg=BG_MAIN,
            fg="#1a1a18",
            font=("Helvetica", 9),
            width=18,
            anchor="w",
        )
        self._lbl.pack(side="left", padx=(0, 6))

        self._entry = tk.Entry(
            self,
            font=("Helvetica", 9),
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground="#b0b0b0",
            highlightcolor="#1a73e8",
            width=self._ancho_entry,
        )
        self._entry.pack(side="left")

    def obtener(self) -> str:
        return self._entry.get().strip()

    def limpiar(self):
        self._entry.delete(0, tk.END)

    def enfocar(self):
        self._entry.focus_set()

    def establecer(self, valor: str):
        self._entry.delete(0, tk.END)
        self._entry.insert(0, valor)



class PanelEncabezado(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg=BG_DARK, pady=10)
        self._construir()

    def _construir(self):
        self._lbl_titulo = tk.Label(
            self,
            text="Agenda de Contactos",
            bg=BG_DARK,
            fg="#ffffff",
            font=("Helvetica", 13, "bold"),
        )
        self._lbl_titulo.pack()

        self._lbl_subtitulo = tk.Label(
            self,
            text="CRUD sobre archivo friendsContact.txt",
            bg=BG_DARK,
            fg=COLOR_MUTED,
            font=("Helvetica", 8),
        )
        self._lbl_subtitulo.pack()



class PanelFormulario(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg=BG_MAIN, padx=16, pady=10)
        self._construir()

    def _construir(self):
        self._lbl_sec = tk.Label(
            self,
            text="Datos del contacto",
            bg=BG_MAIN,
            fg="#555555",
            font=("Helvetica", 9, "bold"),
            anchor="w",
        )
        self._lbl_sec.pack(fill="x", pady=(0, 6))

        self._campo_nombre = CampoFormulario(self, "Nombre:")
        self._campo_nombre.pack(anchor="w", pady=2)

        self._campo_numero = CampoFormulario(self, "Número de teléfono:")
        self._campo_numero.pack(anchor="w", pady=2)

        self._lbl_nota = tk.Label(
            self,
            text="Para Delete y Read solo se usa el campo Nombre.",
            bg=BG_MAIN,
            fg=COLOR_MUTED,
            font=("Helvetica", 7, "italic"),
            anchor="w",
        )
        self._lbl_nota.pack(fill="x", pady=(4, 0))

    def obtener_nombre(self) -> str:
        return self._campo_nombre.obtener()

    def obtener_numero(self) -> str:
        return self._campo_numero.obtener()

    def establecer_nombre(self, valor: str):
        self._campo_nombre.establecer(valor)

    def establecer_numero(self, valor: str):
        self._campo_numero.establecer(valor)

    def limpiar(self):
        self._campo_nombre.limpiar()
        self._campo_numero.limpiar()
        self._campo_nombre.enfocar()



class PanelBotones(tk.Frame):

    def __init__(self, parent, cmd_create, cmd_read,
                    cmd_update, cmd_delete):
        super().__init__(parent, bg=BG_MAIN, pady=8)
        self._cmd_create = cmd_create
        self._cmd_read   = cmd_read
        self._cmd_update = cmd_update
        self._cmd_delete = cmd_delete
        self._construir()

    def _construir(self):
        botones = [
            ("Create",  self._cmd_create, COLOR_CREATE),
            ("Read",    self._cmd_read,   COLOR_READ),
            ("Update",  self._cmd_update, COLOR_UPDATE),
            ("Delete",  self._cmd_delete, COLOR_DELETE),
        ]
        self._btns: list[tk.Button] = []
        for texto, cmd, color in botones:
            btn = tk.Button(
                self,
                text=texto,
                command=cmd,
                bg=color,
                fg="#ffffff",
                activebackground=color,
                activeforeground="#ffffff",
                relief="flat",
                font=("Helvetica", 9, "bold"),
                padx=14,
                pady=5,
                cursor="hand2",
                bd=0,
            )
            btn.pack(side="left", padx=5)
            self._btns.append(btn)



class PanelTabla(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg=BG_MAIN, padx=16, pady=4)
        self._on_seleccion_callback = None
        self._construir()

    def _construir(self):
        self._lbl_sec = tk.Label(
            self,
            text="Contactos en archivo:",
            bg=BG_MAIN,
            fg="#555555",
            font=("Helvetica", 9, "bold"),
            anchor="w",
        )
        self._lbl_sec.pack(fill="x", pady=(0, 4))

        frame_tree = tk.Frame(self, bg=BG_MAIN)
        frame_tree.pack(fill="both", expand=True)

        self._sb = tk.Scrollbar(frame_tree, orient="vertical")
        self._sb.pack(side="right", fill="y")

        self._tree = ttk.Treeview(
            frame_tree,
            columns=("nombre", "numero"),
            show="headings",
            selectmode="browse",
            yscrollcommand=self._sb.set,
            height=8,
        )
        self._sb.config(command=self._tree.yview)

        self._tree.heading("nombre", text="Nombre")
        self._tree.heading("numero", text="Número de teléfono")
        self._tree.column("nombre", width=200, anchor="w")
        self._tree.column("numero", width=160, anchor="center")
        self._tree.pack(side="left", fill="both", expand=True)

        self._tree.bind("<<TreeviewSelect>>", self._on_seleccion)

    def _on_seleccion(self, event):

        if self._on_seleccion_callback:
            seleccion = self.obtener_seleccion()
            if seleccion:
                self._on_seleccion_callback(*seleccion)

    def set_on_seleccion(self, callback):
        
        self._on_seleccion_callback = callback

    def actualizar(self, contactos: list[Contacto]):

        for item in self._tree.get_children():
            self._tree.delete(item)

        for c in contactos:
            self._tree.insert(
                "",
                "end",
                values=(c.get_nombre(), c.get_numero()),
            )

    def limpiar(self):

        for item in self._tree.get_children():
            self._tree.delete(item)

    def obtener_seleccion(self) -> tuple[str, str] | None:

        seleccion = self._tree.selection()
        if not seleccion:
            return None
        valores = self._tree.item(seleccion[0], "values")
        return (valores[0], valores[1])



class PanelEstado(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#e8e8e8", pady=5)
        self._construir()

    def _construir(self):
        self._lbl = tk.Label(
            self,
            text="Listo.",
            bg="#e8e8e8",
            fg=COLOR_MUTED,
            font=("Helvetica", 8, "italic"),
            anchor="w",
            padx=14,
        )
        self._lbl.pack(fill="x")

    def mostrar_ok(self, mensaje: str):
        self._lbl.config(text=f"✔  {mensaje}", fg=COLOR_OK)

    def mostrar_error(self, mensaje: str):
        self._lbl.config(text=f"✖  {mensaje}", fg=COLOR_ERR)

    def limpiar(self):
        self._lbl.config(text="Listo.", fg=COLOR_MUTED)



class VentanaCrud(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Agenda de Contactos — CRUD")
        self.geometry("520x580")
        self.resizable(False, True)
        self.configure(bg=BG_MAIN)
        self._gestor = GestorContactos()
        self._construir_ui()
        self._centrar()
        self._accion_read()

    def _construir_ui(self):
        self._panel_encabezado = PanelEncabezado(self)
        self._panel_encabezado.pack(fill="x")

        self._panel_formulario = PanelFormulario(self)
        self._panel_formulario.pack(fill="x")

        self._panel_botones = PanelBotones(
            self,
            cmd_create=self._accion_create,
            cmd_read=self._accion_read,
            cmd_update=self._accion_update,
            cmd_delete=self._accion_delete,
        )
        self._panel_botones.pack()

        tk.Frame(self, height=1, bg="#d0d0d0").pack(fill="x")

        self._panel_tabla = PanelTabla(self)
        self._panel_tabla.pack(fill="both", expand=True)
        self._panel_tabla.set_on_seleccion(self._rellenar_formulario)

        self._panel_estado = PanelEstado(self)
        self._panel_estado.pack(fill="x", side="bottom")


    def _rellenar_formulario(self, nombre: str, numero: str):

        self._panel_formulario.establecer_nombre(nombre)
        self._panel_formulario.establecer_numero(numero)


    def _validar_nombre(self) -> str | None:

        nombre = self._panel_formulario.obtener_nombre()
        if not nombre:
            messagebox.showwarning(
                "Campo vacio",
                "El campo 'Nombre' es obligatorio."
            )
            return None
        return nombre

    def _validar_numero(self) -> int | None:

        numero_str = self._panel_formulario.obtener_numero()
        if not numero_str:
            messagebox.showwarning(
                "Campo vacio",
                "El campo 'Numero de telefono' es obligatorio."
            )
            return None
        try:
            numero = int(numero_str)
            if numero <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Dato invalido",
                f"'{numero_str}' no es un numero entero positivo valido.\n"
                "Ingrese solo digitos (ej: 3001234567)."
            )
            return None
        return numero


    def _accion_create(self):

        nombre = self._validar_nombre()
        if nombre is None:
            return
        numero = self._validar_numero()
        if numero is None:
            return

        try:
            mensaje = self._gestor.crear(nombre, numero)
            if "agregado" in mensaje:
                self._panel_estado.mostrar_ok(mensaje)
                self._panel_formulario.limpiar()
                self._accion_read()  # Refrescar tabla
            else:
                self._panel_estado.mostrar_error(mensaje)
        except (ValueError, IOError) as e:
            messagebox.showerror("Error", str(e))
            self._panel_estado.mostrar_error(str(e))


    def _accion_read(self):

        try:
            contactos = self._gestor.leer_todos()
            self._panel_tabla.actualizar(contactos)
            if contactos:
                self._panel_estado.mostrar_ok(
                    f"{len(contactos)} contacto(s) en la agenda."
                )
            else:
                self._panel_estado.limpiar()
        except IOError as e:
            messagebox.showerror("Error de lectura", str(e))
            self._panel_estado.mostrar_error(str(e))


    def _accion_update(self):

        nombre = self._validar_nombre()
        if nombre is None:
            return
        numero = self._validar_numero()
        if numero is None:
            return

        try:
            mensaje = self._gestor.actualizar(nombre, numero)
            if "actualizado" in mensaje:
                self._panel_estado.mostrar_ok(mensaje)
                self._panel_formulario.limpiar()
                self._accion_read()  # Refrescar tabla
            else:
                self._panel_estado.mostrar_error(mensaje)
        except (ValueError, IOError) as e:
            messagebox.showerror("Error", str(e))
            self._panel_estado.mostrar_error(str(e))


    def _accion_delete(self):

        nombre = self._validar_nombre()
        if nombre is None:
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminacion",
            f"¿Seguro que desea eliminar el contacto '{nombre}'?\n"
            "Esta accion no se puede deshacer."
        )
        if not confirmar:
            return

        try:
            mensaje = self._gestor.eliminar(nombre)
            if "eliminado" in mensaje:
                self._panel_estado.mostrar_ok(mensaje)
                self._panel_formulario.limpiar()
                self._accion_read()  # Refrescar tabla
            else:
                self._panel_estado.mostrar_error(mensaje)
        except IOError as e:
            messagebox.showerror("Error", str(e))
            self._panel_estado.mostrar_error(str(e))

    def _centrar(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  // 2) - (self.winfo_width()  // 2)
        y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")