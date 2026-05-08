class Persona:
    
    def __init__(self, nombre, apellidos, numero_documento_identidad, anno_nacimiento, pais, genero):

        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento_identidad = numero_documento_identidad
        self.anno_nacimiento = anno_nacimiento
        self.pais = pais
        self.genero = genero

    def imprimir(self):

        print(f"Nombre = {self.nombre}")
        print(f"Apellidos = {self.apellidos}")
        print(f"Numero de documento de identidad = {self.numero_documento_identidad}")
        print(f"Anno de nacimiento = {self.anno_nacimiento}")
        print(f"Pais de nacimiento = {self.pais}")
        print(f"Genero = {self.genero}")
        
if __name__ == "__main__":
    p1 = Persona("Pedro", "Perez", "1053121010", 1998, "Peru", "M")
    p2 = Persona("Luis", "Leon", "1053223344", 2001, "Colombia", "M" )
    
    p1.imprimir()
    p2.imprimir()
    
    nombre = str(input("Nombre: "))
    apellidos = str(input("Apellidos: "))
    ndoc = str(input("Numero Documento: "))
    anno = int(input("Anno de nacimiento: "))
    pais = str(input("Pais de macimiento: "))
    genero = str(input("Genero (F o M): "))
    
    pi = Persona(nombre, apellidos, ndoc, anno, pais, genero)
    
    pi.imprimir()