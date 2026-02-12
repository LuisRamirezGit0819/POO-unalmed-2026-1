from suma import Suma

def main():
  suma = 0
  x = 20
  suma = Suma.primeraSuma(suma, x)
  y = 40
  x = Suma.calculoX(x, y)
  suma = Suma.segundaSuma(suma, x, y)
  
  print(f"El valo de la suma es:{suma}")
  
if __name__ == "__main__":
  main()