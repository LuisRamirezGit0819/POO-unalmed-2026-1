from Programador import Programador

class EquipoMaratonProgramacion:

    def __init__(
        self,
        nombre_equipo: str,
        universidad: str,
        lenguaje_programacion: str,
    ):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad                    
        self.lenguaje_programacion = lenguaje_programacion  
        self.tamano_equipo = 0                            
        self.programadores: list[Programador | None] = [None] * 3  

    def esta_lleno(self) -> bool:
        return self.tamano_equipo == len(self.programadores)

    def annadir(self, programador: Programador):
        if self.esta_lleno():
            raise Exception(
                "El equipo esta completo. No se pudo agregar programador."
            )
        self.programadores[self.tamano_equipo] = programador
        self.tamano_equipo += 1  

    @staticmethod
    def validar_campo(campo: str):
        for c in campo:
            if c.isdigit():
                raise Exception("El nombre no puede tener digitos.")
        if len(campo) > 20:
            raise Exception(
                "La longitud no debe ser superior a 20 caracteres."
            )

    @staticmethod
    def validar_contrasenna(contrasenna: str, confirmacion: str):
        CARACTERES_ESPECIALES = set("!@#$%^&*()_+-=[]{}|;':\",./<>?")

        if len(contrasenna) < 8:
            raise Exception(
                "La contrasenna debe tener minimo 8 caracteres."
            )
        if " " in contrasenna:
            raise Exception(
                "La contrasenna no debe tener espacios en blanco."
            )
        if not any(c.islower() for c in contrasenna):
            raise Exception(
                "La contrasenna debe tener al menos una letra minuscula."
            )
        if not any(c.isupper() for c in contrasenna):
            raise Exception(
                "La contrasenna debe tener al menos una letra mayuscula."
            )
        if not any(c.isdigit() for c in contrasenna):
            raise Exception(
                "La contrasenna debe tener al menos un numero."
            )
        if not any(c in CARACTERES_ESPECIALES for c in contrasenna):
            raise Exception(
                "La contrasenna debe tener al menos un caracter especial "
                "(!@#$%^&* etc.)."
            )
        if contrasenna != confirmacion:
            raise Exception(
                "Las contrasennas no coinciden."
            )