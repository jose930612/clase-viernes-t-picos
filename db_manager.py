from abc import ABCMeta, abstractmethod
import MySQLdb

class DbManager:

	__metaclass__ = ABCMeta
	
	def __init__(self):
		self.hostname = 'localhost'
		self.username = 'jose'
		self.password = 'josepass'
		self.database = 'viernes'
		self.connection = None
		
	def connectToDB(self):
		self.connection = MySQLdb.connect(host=self.hostname, user=self.username, passwd=self.password, db=self.database)
	
	def closeConnectionToDB(self):
		self.connection.close()
	
	@abstractmethod
	def create_db(self):
		return
	@abstractmethod
	def read_db(self):
		return
	@abstractmethod
	def update_db(self):
		return
	@abstractmethod
	def delete_db(self):
		return

class UserDbManager(DbManager):
	def create_db(self, cliente):
		cursor = self.connection.cursor()
		cursor.execute("INSERT INTO clientes (id, nombre, apellido, genero, fecha_nacimiento, estado_civil) VALUES ({},'{}','{}','{}','{}',{})".format(cliente.cedula, cliente.nombre, cliente.apellidos, cliente.genero, cliente.fecha_nacimiento, cliente.estado_civil ))
		self.connection.commit()
		print("Nuevo cliente creado")
		
	def read_db(self, cedula_cliente):
		cursor = self.connection.cursor()
		cursor.execute("SELECT id FROM clientes WHERE id={}".format(cedula_cliente))
		return cursor
		
	def update_db(self):
		return
		
	def delete_db(self):
		return

class ItemsDbManager(DbManager):
	def create_db(self):
		return
		
	def read_db(self):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM items")
		return cursor
		
	def update_db(self):
		return
		
	def delete_db(self):
		return

class ItemTypesDbManager(DbManager):
	def create_db(self):
		return
		
	def read_db(self, id):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM tipos_item WHERE id={}".format(id))
		type_name = ""
		for id, descripcion in cursor.fetchall():
			type_name = descripcion
		return type_name
		
	def update_db(self):
		return
		
	def delete_db(self):
		return

class FacturaDbManager(DbManager):
	def create_db(self, factura):
		cursor = self.connection.cursor()
		cursor.execute("INSERT INTO facturas (Fecha_factura, cliente, total_factura, estado) VALUES ('{}',{},{},{})".format(factura.fecha_facturacion, factura.cedula, factura.totalFactura, factura.estado))
		self.connection.commit()
		return cursor.lastrowid
		
	def read_db(self):
		return
		
	def update_db(self):
		return
		
	def delete_db(self):
		return

class ItemsFacturaDbManager(DbManager):
	def create_db(self, id_factura, item, cantidad):
		cursor = self.connection.cursor()
		cursor.execute("INSERT INTO items_factura (id_factura, id_item, cantidad) VALUES ({}, {}, {})".format(id_factura, item, cantidad))
		self.connection.commit()
		
	def read_db(self):
		return
		
	def update_db(self):
		return
		
	def delete_db(self):
		return






