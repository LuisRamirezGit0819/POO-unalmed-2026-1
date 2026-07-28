class Suma:

    def sumar(self, a, b, c=None):

        if c is None:
            if isinstance(a, int) and isinstance(b, int):
                resultado = a + b
                print(f"Suma de dos enteros: {a} + {b} = {resultado}")
            else:
                resultado = a + b
                print(f"Suma de dos doubles: {a} + {b} = {resultado}")
        else:
            if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
                resultado = a + b + c
                print(
                    f"Suma de tres enteros: {a} + {b} + {c} = {resultado}"
                )
            else:
                resultado = a + b + c
                print(
                    f"Suma de tres doubles: {a} + {b} + {c} = {resultado}"
                )

        return resultado