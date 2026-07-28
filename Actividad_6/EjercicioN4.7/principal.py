from Gato import Gato
from Perro import Perro
from Lobo import Lobo
from Leon import Leon


def main():

    animales = [
        Gato(),
        Perro(),
        Lobo(),
        Leon()
    ]

    for animal in animales:
        print(animal.get_nombre_cientifico())
        print("Sonido:", animal.get_sonido())
        print("Alimentos:", animal.get_alimentos())
        print("Habitat:", animal.get_habitat())
        print()


if __name__ == "__main__":
    main()