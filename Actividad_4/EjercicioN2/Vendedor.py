class Vendedor:

    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos  
        self.edad = 0

    def imprimir(self):
        lineas = [
            f"Nombre del vendedor = {self.nombre}",
            f"Apellidos del vendedor = {self.apellidos}",
            f"Edad del vendedor = {self.edad}",
        ]
        for linea in lineas:
            print(linea)
        return lineas

    def verificar_edad(self, edad: int):
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 anos.")
        if edad >= 0 and edad < 120:
            self.edad = edad
        else:
            raise ValueError(
                "La edad no puede ser negativa ni mayor a 120."
            )
