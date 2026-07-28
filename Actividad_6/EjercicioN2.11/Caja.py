class Caja:

    def __init__(
        self,
        base: float = None,
        anchura: float = None,
        altura: float = None,
        tipo: str = None,
    ):

        if base is None and anchura is None and altura is None:
            self.base    = 0.0
            self.anchura = 0.0
            self.altura  = 0.0
            self.tipo    = None

        elif base is not None and anchura is None and altura is None:
            self.base    = base
            self.anchura = base   # todos iguales a la longitud
            self.altura  = base
            self.tipo    = None

        else:
            self.base    = base
            self.anchura = anchura
            self.altura  = altura
            self.tipo    = tipo

    def calcular_volumen(self) -> float:
        return self.base * self.anchura * self.altura

    def imprimir(self):
        print(f"Base    = {self.base}")
        print(f"Anchura = {self.anchura}")
        print(f"Altura  = {self.altura}")
        if self.tipo is not None:
            print(f"Tipo    = {self.tipo}")
        print(f"Volumen = {self.calcular_volumen()}")