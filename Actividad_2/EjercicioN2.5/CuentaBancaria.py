from enum import Enum

class TipoCuenta(Enum):
    AHORROS = 1
    CORRIENTE = 2

class CuentaBancaria:
    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta, interes_mensual):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.interes_mensual = interes_mensual
        self.saldo = 0.0 
        
    def aplicar_interes(self):
        if self.saldo > 0:
            interes_generado = self.saldo * (self.interes_mensual / 100)
            self.saldo += interes_generado
            print(f"Interes aplicado ({self.interes_mensual}%). Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("No se puede aplicar interés a una cuenta sin saldo.")

    def imprimir(self):
        print(f"Nombres del titular = {self.nombres_titular}")
        print(f"Apellidos del titular = {self.apellidos_titular}")
        print(f"Numero de cuenta = {self.numero_cuenta}")
        print(f"Tipo de cuenta = {self.tipo_cuenta.name}")
        print(f"Saldo = ${self.saldo:.2f}")

    def consultar_saldo(self):
        print(f"El saldo actual es = ${self.saldo:.2f}")

    def consignar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor}. El nuevo saldo es ${self.saldo:.2f}")
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Se ha retirado ${valor}. El nuevo saldo es ${self.saldo:.2f}")
            return True
        else:
            print("El valor a retirar debe ser mayor a cero y menor o igual al saldo actual.")
            return False

if __name__ == "__main__":
    
    nombres = input("Nombres del titular: ")
    apellidos = input("Apellidos del titular: ")
    numero = int(input("Numero de cuenta: "))
    
    print("Seleccione Tipo de Cuenta (1: Ahorros, 2: Corriente): ")
    opcion = int(input())
    tipo = TipoCuenta.AHORROS if opcion == 1 else TipoCuenta.CORRIENTE
    
    interes = float(input("Porcentaje de interes mensual (ej. 1.5): "))

    mi_cuenta = CuentaBancaria(nombres, apellidos, numero, tipo, interes)
    mi_cuenta.imprimir()

    monto_consignar = float(input("Ingrese valor a consignar: "))
    mi_cuenta.consignar(monto_consignar)
    
    monto_retirar = float(input("Ingrese valor a retirar: "))
    mi_cuenta.retirar(monto_retirar)
    
    mi_cuenta.consultar_saldo()
    
    mi_cuenta.aplicar_interes()