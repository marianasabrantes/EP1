# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:08:06 2018

@author: luca_
"""

import json

with open ('EP1.json','r') as documento:
    data = documento.read().strip()
    
lista=json.loads(data)

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
                    lista[novoitem]={}
                    lista[novoitem]['quantidade']=qntnovoproduto
                    cond=False

                elif qntnovoproduto < 0:
                    print('A quantida de inicial nao pode ser negativa')
            cond=True
            while cond:
                valnovoproduto=float(input('Valor do produto: '))
                if valnovoproduto > 0:
                    lista[novoitem]['valor']=valnovoproduto
                    cond = False
                else:
                    print('Valor invalido')
            print(lista)
            
        else:
            print('Produdo ja cadastrado')
    
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
            lista[nomeproduto]['quantidade']=novaqnt
            novovalor=float(input('Novo valor de {0}: '.format(nomeproduto)))
            lista[nomeproduto]['valor']+=novovalor
                
        else:
            print('Elemento nao encontrado')
            
    elif escolha == 4:
        print(lista)

        escolha2=int(input('Digite uma das opcoes: '))
      
        if escolha2==5:
            for i in lista:
                print('{0} : {1} : {2}'.format(i,lista[i]['quantidade'],lista[i]['valor']))
                
        elif escolha2==6:
            for i in lista:
                soma=0
                soma+=lista[i]['valor']*lista[i]['quantidade']
            print(soma)
            
        elif escolha2==7:
            for i in lista:
                if lista[i]['quantidade']<0:
                    print('{0} : {1}'.format(i,lista[i]['quantidade']))
                    
    elif escolha==0:
        print('Programa encerrado')
        break
    
    else:
        print('Opcao invalida.')
        print('Digite uma opcao valida')
 
with open('EP1.json', 'w') as documento:        
    documento.write(json.dumps(lista))       