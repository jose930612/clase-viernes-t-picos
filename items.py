class Item:
	def __init__(self, codigo, tipo, descripcion, valor):
		self.codigo = codigo
		self.tipo = tipo
		self.descripcion = descripcion
		self.valor = int(valor*1000)
