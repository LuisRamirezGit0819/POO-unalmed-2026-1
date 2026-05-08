import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (2 * self.base) + (2 * self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        return math.sqrt(self.base**2 + self.altura**2)

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            print("Es un triangulo equilatero")
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            print("Es un triangulo escaleno")
        else:
            print("Es un triangulo isosceles")

class Rombo:
    def __init__(self, diagonal_mayor, diagonal_menor, lado):
        self.d_mayor = diagonal_mayor
        self.d_menor = diagonal_menor
        self.lado = lado

    def calcular_area(self):
        return (self.d_mayor * self.d_menor) / 2

    def calcular_perimetro(self):
        return 4 * self.lado

class Trapecio:
    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        self.b_mayor = base_mayor
        self.b_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        return ((self.b_mayor + self.b_menor) * self.altura) / 2

    def calcular_perimetro(self):
        return self.b_mayor + self.b_menor + self.lado1 + self.lado2

if __name__ == "__main__":
    
    r = float(input("Ingrese el radio del circulo: "))
    figura1 = Circulo(r)
    
    b_rec = float(input("Ingrese la base del rectangulo: "))
    a_rec = float(input("Ingrese la altura del rectangulo: "))
    figura2 = Rectangulo(b_rec, a_rec)
    
    l = float(input("Ingrese el lado del cuadrado: "))
    figura3 = Cuadrado(l)
    
    b_tri = float(input("Ingrese la base del triangulo rectangulo: "))
    a_tri = float(input("Ingrese la altura del triangulo rectangulo: "))
    figura4 = TrianguloRectangulo(b_tri, a_tri)
    
    dm = float(input("Diagonal mayor del rombo: "))
    dn = float(input("Diagonal menor del rombo: "))
    l_rombo = float(input("Lado del rombo: "))
    figura_rombo = Rombo(dm, dn, l_rombo)

    bma = float(input("Base mayor del trapecio: "))
    bmi = float(input("Base menor del trapecio: "))
    h_trap = float(input("Altura del trapecio: "))
    l1 = float(input("Lado lateral 1 del trapecio: "))
    l2 = float(input("Lado lateral 2 del trapecio: "))
    figura_trapecio = Trapecio(bma, bmi, h_trap, l1, l2)

    print(f"Circulo: Area = {figura1.calcular_area():.2f}, Perimetro = {figura1.calcular_perimetro():.2f}")
    print(f"Rectangulo: Area = {figura2.calcular_area():.2f}, Perimetro = {figura2.calcular_perimetro():.2f}")
    print(f"Cuadrado: Area = {figura3.calcular_area():.2f}, Perimetro = {figura3.calcular_perimetro():.2f}")
    print(f"Triangulo: Area = {figura4.calcular_area():.2f}, Perimetro = {figura4.calcular_perimetro():.2f}")
    figura4.determinar_tipo_triangulo()
    print(f"Rombo: Area = {figura_rombo.calcular_area():.2f}, Perimetro = {figura_rombo.calcular_perimetro():.2f}")
    print(f"Trapecio: Area = {figura_trapecio.calcular_area():.2f}, Perimetro = {figura_trapecio.calcular_perimetro():.2f}")