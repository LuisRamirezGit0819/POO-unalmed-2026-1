class PruebaExcepciones:

    @staticmethod
    def ejecutar(dividendo: str, divisor: str) -> list[str]:
        mensajes = []

        try:
            if dividendo.strip() == "" or divisor.strip() == "":
                raise ValueError("Debe ingresar ambos valores.")
            cociente = float(dividendo) / float(divisor)
            mensajes.append(f"Resultado: {dividendo} / {divisor} = {cociente}")
        except ZeroDivisionError:
            mensajes.append("Division por cero")
        except ValueError as e:
            mensajes.append(str(e))
        finally:
            mensajes.append("finally")

        return mensajes