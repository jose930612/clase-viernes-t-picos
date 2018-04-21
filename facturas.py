from datetime import datetime

class Factura:
	def __init__(self, cedula):
		self.cedula = cedula
		self.fecha_facturacion = datetime.now().strftime("%Y-%m-%d %H:%M")
		self.estado = 1
		self.itemsFactura = None
		self.totalFactura = None
	def setItems(self, items):
		self.itemsFactura = items
	def setTotal(self, total):
		self.totalFactura = total
	def changeEstado(self, nuevoEstado):
		self.estado = nuevoEstado