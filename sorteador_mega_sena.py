'''Faça um programa que sorteie 6 dezenas para o concurso da Mega Sena. As dezenas não devem se repetir!'''

from random import randint as rd
from os import system as st
from time import sleep
st('cls') #limpa o terminal no VSCODE

print("Olá, seja bem vindo(a)!")
sleep(1)
print("Vou sortear o seu jogo!")
sleep(1)

qt_dezenas = 6
num_sorteados = list()
total_dezenas = 60

while len(num_sorteados) < qt_dezenas:
    x = rd(1,total_dezenas)
    if x not in num_sorteados:
        num_sorteados.append(x)



num_sorteados.sort()

print('Os números sorteados para o concurso da Mega Sena foram:')
for c in range(0,len(num_sorteados)):
    print(f'{c+1}ª dezena: {num_sorteados[c]}')
    sleep(0.2)

    
print('Boa sorte!')
