# -*- coding: utf-8 -*-
# 2. Obtener el titulo de la documentación de las ayudas, para una ayuda concreta introducida por el usuario.

import json

f = open('ayudas.json','r')
doc = json.load(f)

ayudausuario = raw_input("Introduzca el título de una ayuda: ").capitalize()

for ayudas in doc["documentacion"]["documentacion_item"]:
	if doc["titulo"] == ayudausuario:
		print ayudas["titulo"] 
