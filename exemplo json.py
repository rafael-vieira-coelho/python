#!/usr/bin/env python
# coding: utf8

#Carregando biblioteca json
import json

#Gerando os dados: 
pessoas = []  
pessoas.append({  
    'name': 'Scott',
    'website': 'stackoverflow.com',
    'from': 'Nebraska'
})
pessoas.append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
pessoas.append({  
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

#Gravando em arquivo json:
arquivo = open('pessoas.json', 'w')  
json.dump(pessoas, arquivo)

#Lendo do arquivo json:
arquivo = open('pessoas.json') 
pessoas = json.load(arquivo)
for p in pessoas:
	print('Name: ' + p['name'])
	print('Website: ' + p['website'])
	print('From: ' + p['from'] + '\n')
