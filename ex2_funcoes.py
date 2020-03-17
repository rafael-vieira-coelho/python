#!/usr/bin/env python
# coding: utf8

def main():
	n1 = int(input("Qual é o primeiro número?"))
	n2 = int(input("Qual é o segundo número?"))
	n3 = int(input("Qual é o terceiro número?"))
	n4 = int(input("Qual é o quarto número?"))
	soma(n1, n2, n3, n4)
	multiplica(n1, n2, n3, n4)

def soma(numero1, numero2, numero3, numero4):
	somatorio = numero1 + numero2 + numero3 + numero4
	mostra_texto("Somatório: ", somatorio)

def multiplica(n1, n2, n3, n4):
	resultado = n1 * n2 * n3 * n4
	mostra_texto("Resultado da Multiplicação: ", resultado)

def mostra_texto(mnesagem, conteudo):
	print(mensagem, conteudo)

main()
