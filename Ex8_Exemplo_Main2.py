#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "30/04/2019"

def main():
    # a_str e b_str guardam strings
    a_str = input("Digite o primeiro numero: ")
    b_str = input("Digite o segundo numero: ")

    # a_int e b_int guardam inteiros
    a_int = int(a_str) # converte string/texto para inteiro
    b_int = int(b_str) # converte string/texto para inteiro

    # calcule a soma entre valores que são números inteiros
    soma = a_int + b_int

    #texto_soma guarda strings
    texto_soma = str(soma) # converte inteiro para string/texto
	
    # imprima a soma
    print("A soma de " + a_str + " + " + str(b_int) + " eh igual a " + texto_soma)

if __name__ == "__main__":
	main()
