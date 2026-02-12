from calculos import Calculos

def main():
  r = float(input())
  area = Calculos.area(r)
  longitud = Calculos.longitud(r)
  
  print(f"La circunferencia con radio {r} tiene area: {area} y longitud de la circunferencia: {longitud}")
  
if __name__ == "__main__":
  main()