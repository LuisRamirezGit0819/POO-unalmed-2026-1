class FiguraGeometrica:

    def __init__(self):
        self.__volumen = 0.0
        self.__superficie = 0.0

    def set_volumen(self, volumen: float):
        self.__volumen = volumen

    def set_superficie(self, superficie: float):
        self.__superficie = superficie

    def get_volumen(self) -> float:
        return self.__volumen

    def get_superficie(self) -> float:
        return self.__superficie