class Empleado:

    ID_DEFAULT        = 100
    NOMBRE_DEFAULT    = "Nuevo empleado"
    APELLIDOS_DEFAULT = "Nuevo empleado"
    EDAD_DEFAULT      = 18

    def __init__(
        self,
        identificador: int = None,
        nombre: str = None,
        apellidos: str = None,
        edad: int = None,
    ):
        self.identificador = (
            identificador if identificador is not None
            else self.ID_DEFAULT
        )
        self.nombre = nombre if nombre is not None else self.NOMBRE_DEFAULT
        self.apellidos = (
            apellidos if apellidos is not None
            else self.APELLIDOS_DEFAULT
        )
        self.edad = edad if edad is not None else self.EDAD_DEFAULT

    def imprimir(self):
        print(f"Identificador = {self.identificador}")
        print(f"Nombre        = {self.nombre}")
        print(f"Apellidos     = {self.apellidos}")
        print(f"Edad          = {self.edad}")