#!/usr/bin/python3

# 1. Crie um programa em Python que peça para usuário o dia,
# mês e ano em variáveis separadas, valide todos os dados,
# aceite comente dados válidos

import datetime
import time
import os
console = os.system('clear')
print('***************')
print('*             *')
print('***************')
ano_atual = datetime.datetime.now()
sair=''
while (sair !='s'):
    dia = int(input('Digite um dia:\nR: '))
    if dia>=1 and dia <=31:
        mes = int(input('Digite um mês:\nR: '))
        if mes == 2 and dia >29:
            print('Fevereiro deve conter entre 1 e 28 dias.')
        elif(mes >=1 and mes <=7 and mes %2 ==0 and dia >30) or (mes >=8 and mes <=12 and mes %2 ==1 and dia >30):
            print('O mês deve conter entre 1 e 30 dias.')
        else:
            ano = int(input('Digite um ano:\nR: '))
            if ano <1900 or ano >ano_atual.year:
                print("Insira um ano válido.")
            else:
                sair = 's'
    else:
        print('Você deve escolher um dia válido.')
    if sair =='s':
        break
    else:
        time.sleep(1.3)
        console = os.system('clear')
# Python não sabe se decidir entre tipo de variaveis, então precisa lançar casting em cada vez que misturar tipos de dados
if mes >=1 and mes <=9:
    mes = '0'+str(mes)
print('A data escolhida é', str(dia)+'-'+str(mes)+'-'+str(ano))