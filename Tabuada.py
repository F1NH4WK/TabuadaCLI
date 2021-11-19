from time import sleep
from random import randint
from os import system


def digitar(frase:str):
        for i in frase:
                print(i, end = '')
                sleep(0.01)

print('''------------------------------------
        \033[1;40mGERADOR DE TABUADA\033[m
------------------------------------''')

digitar('Qual o nível de dificuldade que você deseja:')

sleep(0.5)
print('\n[\033[1;34m1\033[m] \033[1;32mFÁCIL\033[m \033[1;35m(2 ao 4)\033[m')
sleep(0.5)
print('[\033[1;34m2\033[m] \033[1;33mMÉDIO\033[m \033[1;35m(2 ao 6)\033[m')
sleep(0.5)
print('[\033[1;34m3\033[m] \033[1;31mDIFÍCIL\033[m \033[1;35m(2 ao 9)\033[m')
sleep(0.5)

level = int(input("Resposta: \033[1;32m"))

while not level in [1,2,3]:
        digitar('\033[mDigite uma resposta entre 1 a 3: \033[1;32m')
        try:
                level = int(input())
        except: 
                digitar('\033[1;31mERRO! FIQUE ATENTO AO QUE ESCREVE!\033[m\n')

if level == 1:
        system('cls')
        digitar('\033[mVOCÊ ESCOLHEU O NÍVEL \033[1;32mFÁCIL\033[m!')
        