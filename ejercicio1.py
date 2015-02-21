# -*- coding: utf-8 -*-
# 1. Obtener los títulos de las ayudas.

import json

f = open('ayudas.json','r')
doc = json.load(f)

for ayudas in doc:
	print " "
	print ayudas["titulo"]