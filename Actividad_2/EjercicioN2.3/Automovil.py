from enum import Enum

class TipoCom(Enum):
    GASOLINA = 1; BIOETANOL = 2; DIESEL = 3; BIODIESEL = 4; GAS_NATURAL = 5

class TipoA(Enum):
    CIUDAD = 1; SUBCOMPACTO = 2; COMPACTO = 3; FAMILIAR = 4; EJECUTIVO = 5; SUV = 6

class TipoColor(Enum):
    BLANCO = 1; NEGRO = 2; ROJO = 3; NARANJA = 4; AMARILLO = 5; VERDE = 6; AZUL = 7; VIOLETA = 8

class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil, num_puertas, cant_asientos, vel_maxima, color, es_automatico):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.num_puertas = num_puertas
        self.cant_asientos = cant_asientos
        self.vel_maxima = vel_maxima
        self.color = color
        self.es_automatico = es_automatico 
        self.velocidad_actual = 0
        self.multas = 0 
        self.valor_multas = 0.0 

    @property
    def es_automatico(self):
        return self._es_automatico

    @es_automatico.setter
    def es_automatico(self, valor):
        if isinstance(valor, bool):
            self._es_automatico = valor
        else:
            print("Error: Debe ser un valor booleano (True/False)")

    def acelerar(self, incremento):
        nueva_velocidad = self.velocidad_actual + incremento
        if nueva_velocidad <= self.vel_maxima:
            self.velocidad_actual = nueva_velocidad
        else:
            self.velocidad_actual = self.vel_maxima
            self.multas += 1
            self.valor_multas += 150.0  
            print(f"MULTA Has intentado superar los {self.vel_maxima} km/h.")
            print(f"Multas totales: {self.multas}. Deuda total: ${self.valor_multas}")

    def tiene_multas(self):
        return self.multas > 0

    def total_multas(self):
        return self.valor_multas

    def imprimir(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo}")
        print(f"Transmisión: {'Automática' if self.es_automatico else 'Manual'}")
        print(f"Velocidad Actual: {self.velocidad_actual} km/h de {self.vel_maxima} km/h")
        print(f"Multas: {self.multas} | Total a pagar: ${self.valor_multas}")

def capturar_datos_auto():
    marca = input("Marca: ")
    modelo = int(input("Modelo (Año): "))
    motor = int(input("Cilindraje motor (L): "))
    
    print("Tipo Combustible (1:Gasolina, 2:Bioetanol, 3:Diesel, 4:Biodiesel, 5:Gas Natural):")
    comb = TipoCom(int(input()))
    
    print("Tipo Auto (1:Ciudad, 2:Subcompacto, 3:Compacto, 4:Familiar, 5:Ejecutivo, 6:SUV):")
    tipo = TipoA(int(input()))
    
    puertas = int(input("Numero de puertas: "))
    asientos = int(input("Cantidad de asientos: "))
    vel_max = int(input("Velocidad maxima: "))
    
    print("Color (1:Blanco, 2:Negro, 3:Rojo, 4:Naranja, 5:Amarillo, 6:Verde, 7:Azul, 8:Violeta):")
    col = TipoColor(int(input()))
    
    auto_input = input("¿Es automatico? (s/n): ").lower()
    es_auto = auto_input == 's'

    return Automovil(marca, modelo, motor, comb, tipo, puertas, asientos, vel_max, col, es_auto)

if __name__ == "__main__":
    mi_auto = capturar_datos_auto()
    mi_auto.imprimir()
    
    mi_auto.acelerar(300) 
    mi_auto.acelerar(50)
    
    if mi_auto.tiene_multas():
        print(f"El vehiculo tiene multas pendientes por un total de ${mi_auto.total_multas()}")