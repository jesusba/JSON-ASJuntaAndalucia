# -*- coding: utf-8 -*-
# 2. Obtener el titulo de la documentación de las ayudas, para una ayuda concreta introducida por el usuario.

import json

f = open('ayudas.json','r')
doc = json.load(f)

ayudausuario = raw_input("Introduzca el ID de una ayuda: ").capitalize()

for ayudas in doc:
	if ayudas["id"]==ayudausuario:
		if type(ayudas["documentacion"]["documentacion_item"])==list:
			for docu in ayudas["documentacion"]["documentacion_item"]:
				print ""
				print docu["titulo"]
		else:
			if ayudas["documentacion"]["documentacion_item"]["titulo"] == None:
				print ""
				print "No tiene"
			else:
				print ""
				print ayudas["documentacion"]["documentacion_item"]["titulo"]
