from ArticuloCientifico import ArticuloCientifico
from Empleado import Empleado
from Caja import Caja



def leer_texto(mensaje: str) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  El campo no puede estar vacio. Intente de nuevo.")


def leer_numero(mensaje: str, tipo: type = float):
    while True:
        try:
            return tipo(input(mensaje).strip())
        except ValueError:
            print(
                f"  Dato invalido. Ingrese un numero "
                f"{'entero' if tipo == int else 'decimal'} valido."
            )


def leer_palabras_clave(n: int = 3) -> list[str]:
    palabras = []
    for i in range(n):
        p = leer_texto(f"  Palabra clave {i + 1}: ")
        palabras.append(p)
    return palabras


def separador(titulo: str = ""):
    if titulo:
        print(f"\n{'─' * 10} {titulo} {'─' * 10}")
    else:
        print("─" * 34)



def menu_articulo():
    separador("ARTICULO CIENTIFICO")
    print("Tipo de constructor:")
    print("  1. Solo titulo y autor")
    print("  2. Titulo, autor, palabras clave, publicacion y anno")
    print("  3. Completo (incluye resumen)")

    opcion = leer_numero("Seleccione (1-3): ", tipo=int)
    while opcion not in (1, 2, 3):
        print("  Opcion invalida.")
        opcion = leer_numero("Seleccione (1-3): ", tipo=int)

    titulo = leer_texto("Titulo del articulo: ")
    autor  = leer_texto("Autor del articulo: ")

    if opcion == 1:
        articulo = ArticuloCientifico(titulo, autor)

    elif opcion == 2:
        print("Ingrese las 3 palabras clave:")
        palabras    = leer_palabras_clave(3)
        publicacion = leer_texto("Nombre de la publicacion: ")
        anno        = leer_numero("Anno de publicacion: ", tipo=int)
        articulo    = ArticuloCientifico(
            titulo, autor, palabras, publicacion, anno
        )

    else:
        print("Ingrese las 3 palabras clave:")
        palabras    = leer_palabras_clave(3)
        publicacion = leer_texto("Nombre de la publicacion: ")
        anno        = leer_numero("Anno de publicacion: ", tipo=int)
        resumen     = leer_texto("Resumen del articulo: ")
        articulo    = ArticuloCientifico(
            titulo, autor, palabras, publicacion, anno, resumen
        )

    separador("DATOS DEL ARTICULO")
    articulo.imprimir()



def menu_empleado():
    separador("EMPLEADO")
    print("Tipo de constructor:")
    print("  1. Constructor por defecto (id=100, nombre='Nuevo empleado'...)")
    print("  2. Constructor con parametros")

    opcion = leer_numero("Seleccione (1-2): ", tipo=int)
    while opcion not in (1, 2):
        print("  Opcion invalida.")
        opcion = leer_numero("Seleccione (1-2): ", tipo=int)

    if opcion == 1:
        empleado = Empleado()
    else:
        identificador = leer_numero("Identificador del empleado: ", tipo=int)
        nombre        = leer_texto("Nombre del empleado: ")
        apellidos     = leer_texto("Apellidos del empleado: ")
        edad          = leer_numero("Edad del empleado: ", tipo=int)
        empleado      = Empleado(identificador, nombre, apellidos, edad)

    separador("DATOS DEL EMPLEADO")
    empleado.imprimir()



def menu_caja():
    separador("CAJA")
    print("Tipo de constructor:")
    print("  1. Caja(base, anchura, altura)")
    print("  2. Caja sin parametros -> todos los atributos en 0")
    print("  3. Caja(longitud)      -> todos los atributos iguales")
    print("  4. Caja(base, anchura, altura, tipo) -> agrega tipo de caja")

    opcion = leer_numero("Seleccione (1-4): ", tipo=int)
    while opcion not in (1, 2, 3, 4):
        print("  Opcion invalida.")
        opcion = leer_numero("Seleccione (1-4): ", tipo=int)

    if opcion == 1:
        base    = leer_numero("Base de la caja: ")
        anchura = leer_numero("Anchura de la caja: ")
        altura  = leer_numero("Altura de la caja: ")
        caja    = Caja(base, anchura, altura)

    elif opcion == 2:
        caja = Caja()

    elif opcion == 3:
        longitud = leer_numero("Longitud (igual para base, anchura y altura): ")
        caja     = Caja(longitud)

    else:
        base    = leer_numero("Base de la caja: ")
        anchura = leer_numero("Anchura de la caja: ")
        altura  = leer_numero("Altura de la caja: ")
        tipo    = leer_texto("Tipo de caja: ")
        caja    = Caja(base, anchura, altura, tipo)

    separador("DATOS DE LA CAJA")
    caja.imprimir()



def main():
    print("\n=========================================")
    print("  Constructores Sobrecargados")
    print("  ArticuloCientifico | Empleado | Caja")
    print("=========================================")

    while True:
        separador()
        print("Ejercicios disponibles:")
        print("  1. Articulo Cientifico")
        print("  2. Empleado")
        print("  3. Caja")
        print("  0. Salir")

        opcion = leer_numero("Seleccione una opcion: ", tipo=int)

        if opcion == 1:
            menu_articulo()
        elif opcion == 2:
            menu_empleado()
        elif opcion == 3:
            menu_caja()
        elif opcion == 0:
            print("\nHasta luego.")
            break
        else:
            print("  Opcion invalida.")


if __name__ == "__main__":
    main()