from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = 1
    TERRESTRE = 2
    ENANO = 3

class Planeta:
    def __init__(self, nombre, cantidad_satelites, masa, volumen, diametro, distancia_sol, tipo, es_observable, periodo_orbital, periodo_rotacion):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable
        self.periodo_orbital = periodo_orbital 
        self.periodo_rotacion = periodo_rotacion

    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distancia_sol}")
        print(f"Tipo de planeta = {self.tipo.name}")
        print(f"Es observable = {self.es_observable}")
        print(f"Periodo orbital = {self.periodo_orbital} años")
        print(f"Periodo de rotación = {self.periodo_rotacion} días")

    def calcular_densidad(self):
        if self.volumen == 0:
            return 0
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        limite = 149597870 * 3.4
        return self.distancia_sol > limite


    

if __name__ == "__main__":
    
    tierra = Planeta("Tierra", 1, 5.9736e24, 1.08321e12, 12742, 150000000, TipoPlaneta.TERRESTRE, True, 1.0, 1.0)
    tierra.imprimir()
    print(f"Densidad = {tierra.calcular_densidad()}")
    print(f"Es exterior = {tierra.es_planeta_exterior()}\n")

    nombre = str(input("Nombre: "))
    satelites = int(input("Cantidad de satélites: "))
    masa = float(input("Masa (kg): "))
    volumen = float(input("Volumen (km³): "))
    diametro = int(input("Diámetro (km): "))
    distancia = int(input("Distancia al sol (km): "))
    
    tipo = TipoPlaneta(int(input("Seleccione tipo (1: Gaseoso, 2: Terrestre, 3: Enano): ")))
    
    observable_input = str(input("¿Es observable? (s/n): ")).lower()
    es_observable = True if (observable_input == 's') else False
    
    p_orbital = float(input("Periodo orbital (años): "))
    p_rotacion = float(input("Periodo de rotación (días): "))

    planeta_usuario = Planeta(nombre, satelites, masa, volumen, diametro, distancia, tipo, es_observable, p_orbital, p_rotacion)
    print(f"Densidad = {planeta_usuario.calcular_densidad()}")
    print(f"Es exterior = {planeta_usuario.es_planeta_exterior()}")