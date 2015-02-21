# -*- coding: utf-8 -*-
# 5. Mostrar el plazo de presentación de una ayuda introducida por el usuario.

import json

f = open('ayudas.json','r')
doc = json.load(f)

ayudausuario = raw_input("Introduzca el título de una ayuda: ").capitalize()

for ayudas in doc:
	if ayudas["titulo"] == ayudausuario:
		print "Plazo inicial:",ayudas["plazopresentacion"]["plazopresentacion_item"]["incial"][:10]
		print "Plazo final:",ayudas["plazopresentacion"]["plazopresentacion_item"]["final"][:10]
		