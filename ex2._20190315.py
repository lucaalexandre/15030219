#!/usr/bin/python3

# 2. Crie um programa em Python que pergunte a estação favorita do ano
# e no final apresente a porcentagem de pessoas que escolheram cada estação do ano
import os
import time

continua='s'
cont=1
primavera=0
verao=0
outono=0
inverno=0
while continua !='n':
    os.system("clear")
    print("Passa o inverno, chega o verão\t\tQueria sempre essa alegria")
    print("O calor aquece minha emoção\t\tViver sonhando, quem me dera")
    print("Não pelo clima da estação\t\tOutono é sempre igual")
    print("Mas pelo fogo dessa paixão\t\tAs folhas caem no quintal")
    print("Na primavera, calmaria\t\t\tSó não cai o meu amor")
    print("Tranquilidade, uma quimera\t\tPois não tem jeito, é imortal")
    print("\n\n\t\tSandy&Junior - As 4 Estações \n\n")

    estacao = input("Qual a sua estação favorita do ano?\nR: ").lower()
    if estacao=='primavera':
        print('Primavera')
        primavera+=1
    elif estacao=='verao' or estacao=='verão':
        print('Verão')
        verao+=1
    elif estacao=='outono':
        print('Outono')
        outono+=1
    elif estacao=='inverno':
        print('Inverno')
        inverno+=1
    continua = input('Deseja continuar?(s/n)\nR: ').lower()
    if continua =='s':
        pass
        cont +=1
    else:
        break
os.system('clear')
print('Resultado')
time.sleep(0.8)
print('.')
time.sleep(0.8)
print('.')
time.sleep(0.8)
print('.')
time.sleep(0.8)

print('Responderam a pergunta um total de', str(cont), 'pessoas')
print('Dessas', str(cont)+':')

primavera = (primavera * 100)//cont
verao = (verao*100)//cont
outono = (outono*100)//cont
inverno = (inverno * 100)//cont

print(str(primavera)+"% gostam da Primavera.")
print(str(verao)+"% gostam do Verão.")
print(str(outono)+"% gostam de Outono.")
print(str(inverno)+"% gostam do Inverno.")
