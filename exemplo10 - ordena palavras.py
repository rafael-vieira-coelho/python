#!/usr/bin/env python
# coding: utf8


__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "31/03/2019"

palavra1 = input('Informe a primeira palavra:')
palavra2 = input('Informe a primeira palavra:')

if palavra1 < palavra2:
	print ("A palavra, " + palavra1 + " vem antes de " + palavra2 + ".")
elif palavra1 > palavra2:
	print ("A palavra, " + palavra1 + " vem depois de " + palavra2 + ".")
else:
	print ("São iguais.")
