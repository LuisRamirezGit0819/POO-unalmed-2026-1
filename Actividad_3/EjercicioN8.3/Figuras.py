import math
from FiguraGeometrica import FiguraGeometrica


class Cilindro(FiguraGeometrica):

    def __init__(self, radio: float, altura: float):
        super().__init__()
        self.__radio = radio
        self.__altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self) -> float:
        volumen = math.pi * self.__altura * math.pow(self.__radio, 2.0)
        return volumen

    def calcular_superficie(self) -> float:
        area_lado_a = 2.0 * math.pi * self.__radio * self.__altura
        area_lado_b = 2.0 * math.pi * math.pow(self.__radio, 2.0)
        return area_lado_a + area_lado_b


class Esfera(FiguraGeometrica):

    def __init__(self, radio: float):
        super().__init__()
        self.__radio = radio
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self) -> float:
        volumen = 1.333 * math.pi * math.pow(self.__radio, 3.0)
        return volumen

    def calcular_superficie(self) -> float:
        superficie = 4.0 * math.pi * math.pow(self.__radio, 2.0)
        return superficie


class Piramide(FiguraGeometrica):
    
    def __init__(self, base: float, altura: float, apotema: float):
        super().__init__()
        self.__base = base
        self.__altura = altura
        self.__apotema = apotema
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self) -> float:
        volumen = (math.pow(self.__base, 2.0) * self.__altura) / 3.0
        return volumen

    def calcular_superficie(self) -> float:
        area_base = math.pow(self.__base, 2.0)
        area_lado = 2.0 * self.__base * self.__apotema
        return area_base + area_lado


class Cubo(FiguraGeometrica):

    def __init__(self, lado: float):
        super().__init__()
        self.__lado = lado
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self) -> float:
        volumen = math.pow(self.__lado, 3.0)
        return volumen

    def calcular_superficie(self) -> float:
        superficie = 6.0 * math.pow(self.__lado, 2.0)
        return superficie


class Prisma(FiguraGeometrica):

    def __init__(self, base: float, ancho: float, altura: float):
        super().__init__()
        self.__base = base
        self.__ancho = ancho
        self.__altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self) -> float:
        volumen = self.__base * self.__ancho * self.__altura
        return volumen

    def calcular_superficie(self) -> float:
        superficie = (
            2.0 * (self.__base * self.__ancho)
            + 2.0 * (self.__base * self.__altura)
            + 2.0 * (self.__ancho * self.__altura)
        )
        return superficie