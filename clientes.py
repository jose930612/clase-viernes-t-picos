class Cliente:
	
	def __init__(self, cedula, nombre, apellidos, fecha_nacimiento, genero, estado_civil):
		self.cedula = cedula
		self.nombre = nombre
		self.apellidos = apellidos
		self.fecha_nacimiento = fecha_nacimiento
		self.genero = genero
		self.estado_civil = int(estado_civil)