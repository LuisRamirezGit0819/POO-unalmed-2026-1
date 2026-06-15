class LeerArchivo:
    
    @staticmethod
    def leer(nombre_archivo: str) -> tuple[list[str], str]:
        try:
            lineas = []
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    lineas.append(linea.rstrip('\n'))
            return (lineas, "")
        except OSError:
            return ([], "No se pudo leer el archivo.")

    @staticmethod
    def leer_en_mayusculas(nombre_archivo: str) -> tuple[list[str], str]:
        lineas, error = LeerArchivo.leer(nombre_archivo)
        if error:
            return ([], error)
        lineas_mayusculas = [linea.upper() for linea in lineas]
        return (lineas_mayusculas, "")