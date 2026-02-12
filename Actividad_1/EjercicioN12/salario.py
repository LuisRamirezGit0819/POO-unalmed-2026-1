class Salario():
  @staticmethod
  def porcentajeReteFuente(retencion):
    return retencion/100
    
  @staticmethod  
  def salarioBruto(horas_trabajadas, valor_horas):
    return horas_trabajadas * valor_horas
    
  @staticmethod
  def valorReteFuente(porcentaje_fuente, salario_bruto):
    return porcentaje_fuente * salario_bruto
    
  @staticmethod
  def salarioNeto(salario_bruto, valor_retefunete):
    return salario_bruto - valor_retefunete