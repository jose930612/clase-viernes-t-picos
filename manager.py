# -*- coding: utf-8 -*-

import os, sys
import MySQLdb
import argparse

REQUIRED_VERSION = 3
PYTHON_VERSION = sys.version_info

hostname = 'localhost'
username = 'jose'
password = 'josepass'
database = 'viernes'

FLAGS = None

myConnection = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)

def get_estado_civil(conn):
	cur = conn.cursor()
	cur.execute( "SELECT * FROM estados_civiles" )
	print_estado = "Estado Civil"
	for id, descripcion in cur.fetchall() :
		print_estado += "\n{}. {}".format(id, descripcion)
		# print id, descripcion
	return print_estado
		
def create_user():
	from clientes import Cliente
	from db_manager import UserDbManager
	
	cedula = raw_input("Cedula: ")
	apellidos = raw_input("Apellidos: ")
	nombre = raw_input("Nombre: ")
	fecha_nacimiento = raw_input("Fecha Nacimiento YYYY-MM-DD: ")
	genero = raw_input("Genero M/F: ")
	estado_civil = raw_input("{} :".format(get_estado_civil(myConnection)))
	new_user = Cliente(cedula, nombre, apellidos, fecha_nacimiento, genero.upper(), estado_civil)
	
	user_db = UserDbManager()
	user_db.connectToDB()
	user_db.create_db(new_user)
	user_db.closeConnectionToDB()
	
	return cedula

def browse_catalog():
	from db_manager import ItemsDbManager
	from db_manager import ItemTypesDbManager
	from items import Item
	from tipos_item import ItemType
	
	catalog = {}
	
	item_db = ItemsDbManager()
	item_db.connectToDB()
	
	for id, tipo_item, descripcion, valor_unidad in item_db.read_db().fetchall():
		item_type_db = ItemTypesDbManager()
		item_type_db.connectToDB()
		
		item_type = ItemType(str(item_type_db.read_db(int(tipo_item))))
		
		item_type_db.closeConnectionToDB()
		
		item = Item(int(id), item_type.nombre, descripcion, valor_unidad)
		catalog[int(id)] = item
	
	for product in catalog:
		print(catalog[product].codigo, catalog[product].tipo, catalog[product].descripcion, catalog[product].valor)
		
	return catalog


def create_bill(cedula):
	from facturas import Factura
	from items_factura import BillItem
	from db_manager import UserDbManager
	
	user_db = UserDbManager()
	user_db.connectToDB()
	if user_db.read_db(cedula).rowcount == 0:
		user_db.closeConnectionToDB()
		print("Usuario no existe en la base de datos")
		return
	else:
		user_db.closeConnectionToDB()
		factura = Factura(cedula)
		catalogo = browse_catalog()
		
		shopping_cart = []
		total = 0
		
		newItemCod = None
		while True:
			newItemCod = raw_input("ingrese el codigo del nuevo producto o presione ENTER para parar finalizar: ")
			if newItemCod == "" or newItemCod == None:
				break
			newItemCantidad = int(raw_input("ingrese la cantidad: "))
			# print(catalogo[int(newItemCod)].descripcion)
			shopping_item = BillItem(catalogo[int(newItemCod)], newItemCantidad)
			shopping_cart.append(shopping_item)
			
		if len(shopping_cart) > 0:
			
			for bill_item in shopping_cart:
				total += (bill_item.item.valor * bill_item.cantidad)
			# print(total)
			factura.setItems(shopping_cart)
			factura.setTotal(total)
			from db_manager import FacturaDbManager
			factura_db = FacturaDbManager()
			factura_db.connectToDB()
			
			id_nueva_factura = factura_db.create_db(factura)
			
			factura_db.closeConnectionToDB()
			
			from db_manager import ItemsFacturaDbManager
			
			items_factura_db = ItemsFacturaDbManager()
			items_factura_db.connectToDB()
			
			for shopping_item in shopping_cart:
				items_factura_db.create_db(id_nueva_factura, shopping_item.item.codigo, shopping_item.cantidad)
			items_factura_db.closeConnectionToDB()
			
			
			# print(id_nueva_factura)
				
			print("Factura No. {}".format(id_nueva_factura))
			print("-------------------------------------")
			for shopping_item in shopping_cart:
				print("{}\t${} * {}".format(shopping_item.item.descripcion, shopping_item.item.valor, shopping_item.cantidad))
			print("-------------------------------------")
			print("Total: ${}".format(factura.totalFactura))
		else:
			return
		


if __name__ == "__main__":
	if PYTHON_VERSION.major < REQUIRED_VERSION:
		reload(sys)
		sys.setdefaultencoding('utf8')
	
	parser = argparse.ArgumentParser()
	
	parser.add_argument(
		'--create_bill',
		type=str,
		default='newUser',
		help='Create new user'
	)
	
	FLAGS, unparsed = parser.parse_known_args()
	
	if FLAGS.create_bill == "newUser":
		cedula = create_user()
		create_bill(cedula)
	elif FLAGS.create_bill == "existingUser":
		cedula = raw_input("Cedula: ")
		create_bill(cedula)
	
	# doQuery( myConnection )
	# myConnection.close()