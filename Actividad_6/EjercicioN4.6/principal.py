from Profesor import Profesor
from ProfesorTitular import ProfesorTitular


def main():

    profesor1: Profesor = ProfesorTitular()

    profesor1.imprimir()

    if isinstance(profesor1, ProfesorTitular):
        profesor1.imprimir_annios()


if __name__ == "__main__":
    main()