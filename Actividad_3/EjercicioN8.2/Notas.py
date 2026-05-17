import math

class Notas:

    def __init__(self):
        self.lista_notas = [0.0] * 5  

    def calcular_promedio(self):
        suma = 0.0
        
        for i in range(1, len(self.lista_notas)):
            suma = suma + self.lista_notas[i]
            
        return suma / len(self.lista_notas)

    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = 0.0
        
        for i in range(len(self.lista_notas)):
            suma += math.pow(self.lista_notas[i] - prom, 2)
            
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_menor(self):
        menor = self.lista_notas[0]
        
        for i in range(len(self.lista_notas)):
            if self.lista_notas[i] < menor:
                menor = self.lista_notas[i]
                
        return menor

    def calcular_mayor(self):
        mayor = self.lista_notas[0]
        
        for i in range(len(self.lista_notas)):
            if self.lista_notas[i] > mayor:
                mayor = self.lista_notas[i]
                
        return mayor