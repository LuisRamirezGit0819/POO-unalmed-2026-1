from Edades import CalcularEdades

def main():
  EdJuan = 9
  EdAlber = CalcularEdades.calcularEdAlber(EdJuan)
  EdAna = CalcularEdades.calcularEdAna(EdJuan)
  EdMama = CalcularEdades.calcularEdMama(EdJuan, EdAlber, EdAna)
  
  print(f"Las edades son: Alberto={EdAlber}, Juan={EdJuan}, Ana={EdAna}, Mama={EdMama}")
  
if __name__ == "__main__":
  main()