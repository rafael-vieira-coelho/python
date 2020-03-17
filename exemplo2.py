#!/usr/bin/env python

import random

def main():
	
	turma = {}
	num_alunos = int(input("Qual a quantidade de alunos?"))
	for i in range(num_alunos):
		nota = gera_nota()
		nome = input("Qual o seu nome?")
		turma[nome] = nota
	
	print(turma)
	mostra_notas(turma)
	
def gera_nota():
	x = random.randint(0, 10)
	return float(x)

def mostra_notas(turma):
	for nome in turma:
		print("Aluno:", nome, "tirou", turma.get(nome))

main()
