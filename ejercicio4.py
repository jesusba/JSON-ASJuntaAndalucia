# -*- coding: utf-8 -*-
# 4. Mostrar todas las ayudas creadas en una fecha concreta (si existe).

import json

f = open('ayudas.json','r')
doc = json.load(f)

fechainicio = raw_input("Introduzca una fecha (DD-MM-YYYY): ")

fechainicior = fechainicio[6:10]+"-"+fechainicio[3:6]+fechainicio[0:2]

for ayudas in doc:
	if ayudas["fechapub"][:10] == fechainicior:
		print ""
		print ayudas["titulo"] 