class Contacto:

    SEPARADOR = "!"  

    def __init__(self, nombre: str, numero: int):

        if not nombre or not nombre.strip():
            raise ValueError("El nombre del contacto no puede estar vacio.")
        if numero <= 0:
            raise ValueError(
                "El numero de telefono debe ser un entero positivo."
            )
        self.__nombre = nombre.strip()
        self.__numero = numero


    def get_nombre(self) -> str:
        """Retorna el nombre del contacto."""
        return self.__nombre

    def get_numero(self) -> int:
        """Retorna el numero del contacto."""
        return self.__numero


    def serializar(self) -> str:

        return f"{self.__nombre}{self.SEPARADOR}{self.__numero}"

    @classmethod
    def desde_linea(cls, linea: str) -> "Contacto":

        partes = linea.strip().split(cls.SEPARADOR, maxsplit=1)
        if len(partes) != 2:
            raise ValueError(
                f"Formato de linea invalido: '{linea}'. "
                f"Se esperaba 'nombre{cls.SEPARADOR}numero'."
            )
        try:
            numero = int(partes[1])
        except ValueError:
            raise ValueError(
                f"El numero '{partes[1]}' no es un entero valido."
            )
        return cls(partes[0], numero)

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Contacto):
            return False
        return (
            self.__nombre == other.__nombre
            or self.__numero == other.__numero
        )

    def __repr__(self) -> str:
        return (
            f"Contacto(nombre='{self.__nombre}', "
            f"numero={self.__numero})"
        )