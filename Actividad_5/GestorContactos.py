import os
from pathlib import Path
from Contacto import Contacto


class GestorContactos:


    NOMBRE_ARCHIVO = "friendsContact.txt"
    NOMBRE_TEMP    = "temp.txt"

    def __init__(self, ruta_directorio: str = "."):

        self.__directorio = Path(ruta_directorio)
        self.__ruta_archivo = self.__directorio / self.NOMBRE_ARCHIVO
        self.__ruta_temp    = self.__directorio / self.NOMBRE_TEMP

    def _asegurar_archivo(self):
        
        if not self.__ruta_archivo.exists():
            self.__ruta_archivo.touch()

    def _leer_todos(self) -> list[Contacto]:
        
        self._asegurar_archivo()
        contactos = []
        try:
            with open(self.__ruta_archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        try:
                            contacto = Contacto.desde_linea(linea)
                            contactos.append(contacto)
                        except ValueError:
                            continue
        except OSError as e:
            raise IOError(f"No se pudo leer el archivo: {e}")
        return contactos

    def _escribir_todos(self, contactos: list[Contacto]):

        try:
            with open(self.__ruta_archivo, 'w', encoding='utf-8') as f:
                for contacto in contactos:
                    f.write(contacto.serializar() + "\n")
        except OSError as e:
            raise IOError(f"No se pudo escribir el archivo: {e}")


    def crear(self, nombre: str, numero: int) -> str:

        nuevo = Contacto(nombre, numero)
        contactos = self._leer_todos()

        encontrado = False
        for c in contactos:
            if c == nuevo:
                encontrado = True
                break

        if not encontrado:
            try:
                self._asegurar_archivo()
                with open(self.__ruta_archivo, 'a', encoding='utf-8') as f:
                    f.write(nuevo.serializar() + "\n")
            except OSError as e:
                raise IOError(f"No se pudo escribir el archivo: {e}")
            return "Contacto agregado."
        else:
            return (
                "El nombre o numero ya existe en la agenda."
            )


    def leer_todos(self) -> list[Contacto]:
        return self._leer_todos()


    def actualizar(self, nombre_buscar: str, nuevo_numero: int) -> str:

        if nuevo_numero <= 0:
            raise ValueError(
                "El nuevo numero debe ser un entero positivo."
            )

        contactos = self._leer_todos()

        encontrado = any(
            c.get_nombre() == nombre_buscar for c in contactos
        )

        if not encontrado:
            return (
                f"El contacto '{nombre_buscar}' no existe en la agenda."
            )

        nuevos_contactos = []
        for c in contactos:
            if c.get_nombre() == nombre_buscar:
                nuevos_contactos.append(
                    Contacto(c.get_nombre(), nuevo_numero)
                )
            else:
                nuevos_contactos.append(c)

        self._escribir_todos(nuevos_contactos)
        return f"Contacto '{nombre_buscar}' actualizado."

    def eliminar(self, nombre_buscar: str) -> str:

        contactos = self._leer_todos()

        encontrado = any(
            c.get_nombre() == nombre_buscar for c in contactos
        )

        if not encontrado:
            return (
                f"El contacto '{nombre_buscar}' no existe en la agenda."
            )

        nuevos_contactos = [
            c for c in contactos
            if c.get_nombre() != nombre_buscar
        ]

        self._escribir_todos(nuevos_contactos)
        return f"Contacto '{nombre_buscar}' eliminado."  