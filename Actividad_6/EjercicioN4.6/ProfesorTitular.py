from Profesor import Profesor


class ProfesorTitular(Profesor):

    def __init__(self):
        self.annios = 0

    def imprimir(self):
        print("Es un profesor titular.")

    def imprimir_annios(self):
        print(f"Annios = {self.annios}")