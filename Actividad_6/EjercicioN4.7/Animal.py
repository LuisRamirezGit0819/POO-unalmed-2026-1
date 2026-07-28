from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self):
        self.sonido = ""
        self.alimentos = ""
        self.habitat = ""
        self.nombre_cientifico = ""

    @abstractmethod
    def get_nombre_cientifico(self):
        pass

    @abstractmethod
    def get_sonido(self):
        pass

    @abstractmethod
    def get_alimentos(self):
        pass

    @abstractmethod
    def get_habitat(self):
        pass