# -*- coding: utf-8 -*-
# 5. Mostrar el plazo de presentación de una ayuda introducida por el usuario.

import json

f = open('ayudas.json','r')
doc = json.load(f)

ayudausuario = raw_input("Introduzca el título de una ayuda: ").capitalize()

for ayudas in doc:
	for docu in ayudas["plazopresentacion"]["plazopresentacion_item"]:
		if ayudas["titulo"] == ayudausuario:
			print "Plazo inicial:",docu["incial"][:10]
			print "Plazo final:",docu["final"][:10]
		