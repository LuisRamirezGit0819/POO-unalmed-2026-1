from salario import Salario

def main():
  horas_trabajadas = 48
  valor_hora = 5000
  retencion = 12.5
  porcentaje_retefunte = Salario.porcentajeReteFuente(retencion)
  salario_bruto = Salario.salarioBruto(horas_trabajadas, valor_hora)
  valor_retefuente = Salario.valorReteFuente(porcentaje_retefunte, salario_bruto)
  salario_neto = Salario.salarioNeto(salario_bruto, valor_retefuente)
  
  print(f"Salario Bruto: {salario_bruto}\nRetencion en la Fuente: {valor_retefuente}\nSalario Neto: {salario_neto}")
  
if __name__ == "__main__":
  main()