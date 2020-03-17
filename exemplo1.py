#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "31/03/2019"

import string

def main():
	poesia = "O orvalho no carvalho..."
	lista = poesia.split(" ")
	for palavra in lista:
		print(palavra)

if __name__=="__main__":
	main()
