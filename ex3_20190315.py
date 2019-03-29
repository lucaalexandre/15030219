#!/usr/bin/python3

# Crie um programa em Python que pergunte ao usuário o seu nível de escolaridade
# (Médio, Superior ou Pós) e apresente somente nível que foi mais votado


import os

#inicio
# limpa o console
os.system('clear')

#declaracao de variaveis
sair='n'
cont = 1
medio =0
pos =0
superior=0

# verifica qual nível de escolaridade foi escolhido
while sair!='s':
    print('Médio | Superior | Pós')
    escol = input('Qual seu nível de escolaridade?\nR: ').lower()
    if escol =='médio' or escol=='medio':
        medio+=1
    elif escol == 'superior':
        superior+=1
    elif escol =='pos' or escol =='pos':
        pos+=1
    else:
        break
    sair = input('Deseja sair?\nR: ')
    if sair =='s':
        break
    else:
        os.system('clear')
        cont+=1


votado=0

# 
if pos > medio and pos > superior:
    votado = pos
    votado = 'pós'
elif medio > pos and medio > superior :
    votado = medio
    votado = 'médio'
elif superior > pos and superior > medio:
    votado = superior
    votado = 'superior'
else:
    print("Empate.")

# print('Tivemos',str(cont),'votante(s).')
# print('Pós',str(pos))
# print('Médio',str(medio))
# print('Superior',str(superior))
print('O nível de escolaridade mais votado foi', str(votado))


