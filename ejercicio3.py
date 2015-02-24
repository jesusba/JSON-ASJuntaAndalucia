# -*- coding: utf-8 -*-

#3. Obtener una taxonomía concreta, y que te muestre los nombres de las ayudas que contenga esa taxonomía.

import json

f = open('ayudas.json','r')
doc = json.load(f)

taxonomiausuario = raw_input("Introduzca el nombre de una taxonomía: ")

for ayuda in doc:
	for docu in ayuda["taxonomias"]["taxonomia_item"]:
		if ayuda["titulo"] == taxonomiausuario:
			print docu["titulo"]