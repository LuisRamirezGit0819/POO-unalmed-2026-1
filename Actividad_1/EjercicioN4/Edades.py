class CalcularEdades():
  @staticmethod
  def calcularEdAlber(EdJuan):
    return 2*EdJuan/3

  @staticmethod
  def calcularEdAna(EdJuan):
    return 4*EdJuan/3

  @staticmethod
  def calcularEdMama(EdJuan, EdAlber, EdAna):
    return EdJuan+EdAna+EdAlber