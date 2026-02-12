from potencias import Potencias

def main():
  x = float(input())
  xCuadrado = Potencias.calcularPotencias(x)[0]
  xCubo = Potencias.calcularPotencias(x)[1]
  
  print(f"El cuadrado de {x} es {xCuadrado}, y su cubo {xCubo}")
  
if __name__ == "__main__":
  main()