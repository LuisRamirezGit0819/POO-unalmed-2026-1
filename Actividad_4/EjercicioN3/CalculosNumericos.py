import math


class CalculosNumericos:

    @staticmethod
    def calcular_logaritmo_neperiano(valor: float) -> tuple[str, str]:
        try:
            if valor <= 0:
                raise ArithmeticError(
                    "El valor debe ser un numero positivo y =/= 0"
                )
            resultado = math.log(valor)
            return (f"Resultado = {resultado}", "")

        except ArithmeticError:
            return (
                "",
                "El valor debe ser un numero positivo para "
                "calcular el logaritmo",
            )
        except TypeError:
            return (
                "",
                "El valor debe ser numerico para calcular "
                "el logaritmo",
            )

    @staticmethod
    def calcular_raiz_cuadrada(valor: float) -> tuple[str, str]:
        try:
            if valor < 0:
                raise ArithmeticError(
                    "El valor debe ser un numero positivo"
                )
            resultado = math.sqrt(valor)
            return (f"Resultado = {resultado}", "")

        except ArithmeticError:
            return (
                "",
                "El valor debe ser un numero positivo para "
                "calcular la raiz cuadrada",
            )
        except TypeError:
            return (
                "",
                "El valor debe ser numerico para calcular "
                "la raiz cuadrada",
            )
