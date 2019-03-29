#!/usr/bin/python3

# Monte um programa em Python que solicite a idade e o nome das pessoas, 
# ao término deverá exibir:
# somente a pessoa mais velha, 
# a mais nova, 
# a quantidade de pessoas maiores de idade,
# média entre as idades que foram digitadas.

# imports para comandos do sistema (somente unix) e time delay
import os
import time


# inicio
os.system('clear')


# declaracao de variaveis
cont=1
sair='n'
maioridade=0
media=0

# Laço de repetição que recebe nome e idade, guarda o valor na primeira sequência e faz condicional
# de acordo com o enunciado
while sair!='s':
    nome = input('Digite seu nome:\nR: ').capitalize()
    idade= int(input('Digite sua idade:\nR: '))
    media = media + idade
    if cont == 1:
        maior_idade = idade
        maior_nome = nome
        menor_idade = idade
        menor_nome = nome
    else:
        if idade > maior_idade:
            maior_idade = idade
            maior_nome = nome
        elif idade < menor_idade:
            menor_idade = idade
            menor_nome = nome

    # Verifica se a pessoa é maior de idade
    if idade >=18:
        maioridade+=1    

    # verifica se o programa pode ser encerrado, caso contrário, reinicia a sequência
    sair = input('Deseja sair? (s/n)\nR: ').lower()
    if sair=='s':
        break
    else:
        os.system('clear')
        cont+=1
        pass

# Faz o calculo da média
media = media / cont

# Limpa o console 
os.system('clear')

print('Resultado')
time.sleep(0.8)
print('.')
time.sleep(0.8)
print('.')
time.sleep(0.8)
print('.')
time.sleep(0.8)

# Exibe resultados
print('O teste rodou',str(cont),'vezes')
time.sleep(0.5)
print('A pessoa mais velha é', maior_nome, 'com', str(maior_idade))
time.sleep(0.5)
print('A pessoa mais nova é', menor_nome, 'com', str(menor_idade))
time.sleep(0.5)
print('Total  de pessoas maior de idade:', str(maioridade))
time.sleep(0.5)
print('A média de idade das pessoas é de', str(media))

