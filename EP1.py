#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:04:31 2018

@author: Luiza Winter
"""

lista={}
while True:
    print()
    print('Controle de estoque')
    print('0 - sair')
    print('1 - adicionar item')
    print('2 - remover item')
    print('3 - alterar item')
    print('4 - imprimir estoque')
    
    escolha=int(input('Digite uma das alternativas: '))
    
    if escolha == 1:
        novoitem=str(input('Nome do produto: '))
        if novoitem not in lista:
            cond=True
            while cond:
                qntnovoproduto=int(input('Quantidade inicial: '))
                if qntnovoproduto > 0:
                    lista[novoitem]=qntnovoproduto
                    cond=False
                elif qntnovoproduto < 0:
                    print('A quantida de inicial nao pode ser negativa')
                    
    elif escolha == 2:
        delItem=input('Nome do produto: ')
        if delItem in lista:
            del lista[delItem]
        else:
            print('Elemento nao encontrado')
    
    elif escolha == 3:
        nomeproduto=input('Nome do produto: ')
        if nomeproduto in lista:
            novaqnt=int(input('Novo estoque de {0}: '.format(nomeproduto)))
            lista[nomeproduto]=novaqnt
        else:
            print('Elemento nao encontrado')
    elif escolha == 4:
        print(lista)
        
    elif escolha==0:
        print('Programa encerrado')
        break
    
    else:
        print('')
        print('Opcao invalida.')
        print('Digite uma opcao valida')
