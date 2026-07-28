from Pedido import Pedido
from Suma import Suma



def leer_texto(mensaje: str) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  El campo no puede estar vacio. Intente de nuevo.")


def leer_numero(mensaje: str, tipo: type = float):
    while True:
        try:
            valor = tipo(input(mensaje).strip())
            return valor
        except ValueError:
            print(
                f"  Dato invalido. Ingrese un numero "
                f"{'entero' if tipo == int else 'decimal'} valido."
            )


def separador(titulo: str = ""):
    if titulo:
        print(f"\n{'-' * 10} {titulo} {'-' * 10}")
    else:
        print("-" * 34)



def menu_pedido():
    separador("PEDIDO DE RESTAURANTE")
    print("Tipo de pedido:")
    print("  1. Primer plato + Bebida")
    print("  2. Primer plato + Segundo plato + Bebida")
    print("  3. Primer plato + Segundo plato + Postre + Bebida")

    opcion = leer_numero("Seleccione una opcion (1-3): ", tipo=int)
    while opcion not in (1, 2, 3):
        print("  Opcion invalida. Ingrese 1, 2 o 3.")
        opcion = leer_numero("Seleccione una opcion (1-3): ", tipo=int)

    pedido = Pedido()

    primer_plato       = leer_texto("Nombre del primer plato: ")
    costo_primer_plato = leer_numero("Costo del primer plato: $")
    bebida             = leer_texto("Nombre de la bebida: ")
    costo_bebida       = leer_numero("Costo de la bebida: $")

    if opcion == 1:
        pedido.calcular_pedido(
            primer_plato, costo_primer_plato,
            bebida, costo_bebida,
        )

    elif opcion == 2:
        segundo_plato       = leer_texto("Nombre del segundo plato: ")
        costo_segundo_plato = leer_numero("Costo del segundo plato: $")
        pedido.calcular_pedido(
            primer_plato, costo_primer_plato,
            bebida, costo_bebida,
            segundo_plato=segundo_plato,
            costo_segundo_plato=costo_segundo_plato,
        )

    else:
        segundo_plato       = leer_texto("Nombre del segundo plato: ")
        costo_segundo_plato = leer_numero("Costo del segundo plato: $")
        postre              = leer_texto("Nombre del postre: ")
        costo_postre        = leer_numero("Costo del postre: $")
        pedido.calcular_pedido(
            primer_plato, costo_primer_plato,
            bebida, costo_bebida,
            segundo_plato=segundo_plato,
            costo_segundo_plato=costo_segundo_plato,
            postre=postre,
            costo_postre=costo_postre,
        )



def menu_suma():
    separador("SUMA")
    print("Version de suma:")
    print("  1. Suma de dos enteros")
    print("  2. Suma de tres enteros")
    print("  3. Suma de dos decimales (double)")
    print("  4. Suma de tres decimales (double)")

    opcion = leer_numero("Seleccione una opcion (1-4): ", tipo=int)
    while opcion not in (1, 2, 3, 4):
        print("  Opcion invalida. Ingrese 1, 2, 3 o 4.")
        opcion = leer_numero("Seleccione una opcion (1-4): ", tipo=int)

    suma = Suma()

    if opcion == 1:
        a = leer_numero("Primer entero: ", tipo=int)
        b = leer_numero("Segundo entero: ", tipo=int)
        suma.sumar(a, b)

    elif opcion == 2:
        a = leer_numero("Primer entero: ", tipo=int)
        b = leer_numero("Segundo entero: ", tipo=int)
        c = leer_numero("Tercer entero: ", tipo=int)
        suma.sumar(a, b, c)

    elif opcion == 3:
        a = leer_numero("Primer decimal: ", tipo=float)
        b = leer_numero("Segundo decimal: ", tipo=float)
        suma.sumar(a, b)

    else:
        a = leer_numero("Primer decimal: ", tipo=float)
        b = leer_numero("Segundo decimal: ", tipo=float)
        c = leer_numero("Tercer decimal: ", tipo=float)
        suma.sumar(a, b, c)



def main():
    print("\n===================================")
    print("  Pedido y Suma - Sobrecarga")
    print("===================================")

    while True:
        separador()
        print("Ejercicios disponibles:")
        print("  1. Pedido de restaurante")
        print("  2. Suma")
        print("  0. Salir")

        opcion = leer_numero("Seleccione una opcion: ", tipo=int)

        if opcion == 1:
            menu_pedido()
        elif opcion == 2:
            menu_suma()
        elif opcion == 0:
            print("\nHasta luego.")
            break
        else:
            print("  Opcion invalida.")


if __name__ == "__main__":
    main()