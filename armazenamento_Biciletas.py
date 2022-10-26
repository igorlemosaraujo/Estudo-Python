class bicicleta():
  def __init__(self, cor, modelo, ano, valor):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor
  
  def buzinar(self): #deve declarar a referencia explicitamente com o self
    print("booommmm booomm")

  def parar(self):
    print("parando...")
    print("estou parada")
  
  def correr(self):
    print("cleck cleck clekc...")

  def trocar_marcha(self, nro_marcha):
    print(f"Marcha trocada para {nro_marcha}")
  
  # def __str__(self) -> str:
  #   return f"Bicicleta: cor:{self.cor}, modelo:{self.modelo}, ano:{self.ano}, valor:{self.valor}"
   
  def __str__(self) -> str:
    return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b_01 = bicicleta("Azul","Elite 10","1998",12580)
b_02 = bicicleta("Rosa","bmx","2008",6758)

print(b_01.valor,b_01.cor,b_01.ano)
b_01.buzinar()
b_01.parar()
b_01.correr()

b_02.buzinar()
print(b_01)
b_01.trocar_marcha(2)