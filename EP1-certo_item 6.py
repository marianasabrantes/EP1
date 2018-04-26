# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:34:44 2018

@author: Mariana Abrantes
"""
from firebase import firebase
firebase=firebase.FirebaseApplication('https://trabalho-ep1.firebaseio.com/',None)

try:
    lista=firebase.get('/estoques',None)
    lista=lista[0][0]
except:
    lista={'Loja':{}}




def lojas(dicionario):
    aaaa=[]
    for i in dicionario:
        aaaa.append(i)
    return aaaa

while True:
    loja=lojas(lista)
    print()
    print('Controle de lojas')
    print('0 - Sair')
    print('1 - Adicione uma loja')
    print('2 - Alterar estoque de loja')
    print('3 - Remover loja')
    print('4 - Imprimir todas as lojas')
    op=int(input('Escolha uma opção: '))
    if op==0:
        print("Até logo!")
        break
    if op ==1:
        a= input('Qual o nome da loja? ')
        if a in loja:
            print ('Loja já cadastrada')
        else:
            lista[a]={}
            print('Loja adicionada')
    elif op == 2:
        b=input('Qual estoque a ser alterado? ')
        
        if b in loja:
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
                    if novoitem not in lista[b]:
                        cond=True
                        while cond:
                            qntnovoproduto=int(input('Quantidade inicial: '))
                            lista[b][novoitem]={}
                            lista[b][novoitem]['quantidade']=qntnovoproduto
                            cond=False
        
                        cond=True
                        while cond:
                            valnovoproduto=float(input('Valor do produto: '))
                            if valnovoproduto > 0:
                                lista[b][novoitem]['valor']=valnovoproduto
                                cond = False
                            else:
                                print('Valor inválido')
                    
                    else:
                        print('Produdo já cadastrado')
            
                elif escolha == 2:
                    delItem=input('Nome do produto: ')
                    if delItem in lista[b]:
                        del lista[b][delItem]
                    else:
                        print('Elemento não encontrado')
        
                elif escolha == 3:
                    nomeproduto=input('Nome do produto: ')
                    if nomeproduto in lista[b]:
                        escolha3=input('Alterar o a quantidade ou o valor? (Q/V): ')
                        if escolha3.lower()=='q': 
                            novaqnt=int(input('Novo estoque de {0}: '.format(nomeproduto)))
                            lista[b][nomeproduto]['quantidade']+=novaqnt
                        elif escolha3.lower()=='v':
                            while True:
                                novovalor=float(input('Novo valor de {0}: '.format(nomeproduto)))
                                if novovalor>=0:
                                    break
                                else:
                                    print('Insira um valor válido')
                            lista[b][nomeproduto]['valor']=novovalor
                    else:
                        print('Elemento não encontrado')
                    
                elif escolha == 4:
                    print('5 : Estoque')
                    print('6 : Valor total do estoque')
                    print('7 : Itens com quantidade negativa')
        
                    escolha2=int(input('Digite uma das opcoes: '))
              
                    if escolha2==5:
                        for i in lista[b]:
                            print('{0} : {1} : {2}'.format(i,lista[b][i]['quantidade'],lista[b][i]['valor']))
                        
                    elif escolha2==6:
                        soma=0
                        for i in lista[b]:
                            
                            soma+=lista[b][i]['valor']*lista[b][i]['quantidade']
                        print(soma)
                    
                    elif escolha2==7:
                        for i in lista[b]:
                            if lista[b][i]['quantidade']<0:
                                print('{0} : {1}'.format(i,lista[b][i]['quantidade']))
                            
                elif escolha==0:
                    print('Programa encerrado')
                    break
            
            else:
                print('Opção inválida')
                print('Digite uma opção válida')
        else:
            print('Loja não encontrada')
    elif op == 3:
        remover= input('Qual o nome da loja? ')
        if remover in loja:
            del lista[remover]
            print ('Loja removida')
        else:
            print('Loja não cadastrada')
        
    elif op==4:
        s=[]
        for i in lista:
            s.append(i)
        print(', '.join(s))

a=[lista]
firebase.put('/estoques', '0', a)        
