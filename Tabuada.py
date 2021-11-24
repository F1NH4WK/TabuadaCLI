from time import sleep, time
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
acertos = 0

while not level in [1,2,3]:
        digitar('\033[mDigite uma resposta entre 1 a 3: \033[1;32m')
        try:
                level = int(input())
        except: 
                digitar('\033[1;31mERRO! FIQUE ATENTO AO QUE ESCREVE!\033[m\n')

if level == 1:
        system('cls')
        digitar('\033[mVOCÊ ESCOLHEU O NÍVEL \033[1;32mFÁCIL\033[m!\n')
        print('')
        digitar("COMEÇANDO EM:\n")

        for i in range(3, 0, -1):
                print(i)
                sleep(1)
        start = time()
        result = []

        for i in range(1, 11):
                system('cls')
                var = 0
                num = [randint(2, 4), randint(2, 4)]

                while i >= 2:
                        if num in result[var][0:2]:
                                num = [randint(2,4), randint(2,4)]
                        if var+1 == len(result):
                                break
                        var += 1
                        
                digitar(f'\033[1;35m{num[0]}\033[m X \033[1;35m{num[1]}\033[m\n')
                sleep(1)
                resp = int(input('\033[mRESPOSTA: \033[1;32m'))
                if resp == num[0] * num[1]:
                        num.append(True)
                        result.append(num)
                else:
                        num.append(False)
                        result.append(num)

        total = time() - start
        digitar('\033[mFIM\n')
        sleep(0.5)
        if total >= 60:
                digitar(f"Você levou \033[1;31m{total:.0f} segundos\033[m para resolver as contas, \033[1;31mESTUDE MAIS\033[m!\n")
        if 30 <= total < 60:
                digitar(f'Você levou \033[1;33m{total:.0f} segundos\033[m para resolver as contas, \033[1;33mCONTINUE SE ESFORÇANDO\033[m!\n')
        if total < 30:
                digitar(f'Você levou \033[1;32m{total:.0f} segundos\033[m para resolver as contas, \033[1;32mCONTINUE ASSIM, PORRA\033[m!\n')
        for i in result:
                if i[2] == True:
                        digitar(f'\033[1;32m{i[0]} X {i[1]}\033[m = \033[1;35m{i[0]*i[1]}\033[m\n')
                        acertos += 1
                else:
                        digitar(f'\033[1;31m{i[0]} X {i[1]}\033[m = \033[1;35m{i[0]*i[1]}\033[m\n')

        digitar(f'\033[1;32mACERTOS: {acertos}\033[m\n')
        digitar(f'\033[1;31mERROS: {10 - acertos}\033[m')

if level == 2:
        system('cls')
        digitar('\033[mVOCÊ ESCOLHEU O NÍVEL \033[1;33mMÉDIO\033[m!')
        print('')
        digitar("COMEÇANDO EM:\n")

        for i in range(3, 0, -1):
                print(i)
                sleep(1)

        result = []
        start = time()
        for i in range(1, 11):
                system('cls')
                var = 0
                num = [randint(2, 6), randint(2, 6)]

                while i >= 2:
                        if num in result[var][0:2]:
                                num = [randint(2,6), randint(2,6)]
                        if var+1 == len(result):
                                break
                        var += 1
                        
                digitar(f'\033[1;35m{num[0]}\033[m X \033[1;35m{num[1]}\033[m\n')
                sleep(0.5)
                resp = int(input('\033[mRESPOSTA: \033[1;32m'))
                if resp == num[0] * num[1]:
                        num.append(True)
                        result.append(num)
                else:
                        num.append(False)
                        result.append(num)

        total = time() - start
        digitar('\033[mFIM\n')
        sleep(1)
        if total >= 60:
                digitar(f"Você levou \033[1;31m{total:.0f} segundos\033[m para resolver as contas, \033[1;31mESTUDE MAIS\033[m!\n")
        if 30 <= total < 60:
                digitar(f'Você levou \033[1;33m{total:.0f} segundos\033[m para resolver as contas, \033[1;33mCONTINUE SE ESFORÇANDO\033[m!\n')
        if total < 30:
                digitar(f'Você levou \033[1;32m{total:.0f} segundos\033[m para resolver as contas, \033[1;32mCONTINUE ASSIM, PORRA\033[m!\n')

        for i in result:
                if i[2] == True:
                        digitar(f'\033[1;32m{i[0]} X {i[1]}\033[m = \033[1;35m{i[0]*i[1]}\033[m\n')
                        acertos += 1
                else:
                        digitar(f'\033[1;31m{i[0]} X {i[1]}\033[m = \033[1;35m{i[0]*i[1]}\033[m\n')

        digitar(f'\033[1;32mACERTOS: {acertos}\033[m\n')
        digitar(f'\033[1;31mERROS: {10 - acertos}\033[m')

if level == 3:
        system('cls')
        digitar('\033[mVOCÊ ESCOLHEU O NÍVEL \033[1;31mDIFÍCIL\033[m!')
        print('')
        digitar("COMEÇANDO EM:\n")

        for i in range(3, 0, -1):
                print(i)
                sleep(1)

        result = []
        start = time()

        for i in range(1, 11):
                system('cls')
                var = 0
                num = [randint(2, 9), randint(2, 9)]
                while i >= 2:
                        if num in result[var][0:2]:
                                num = [randint(2,9), randint(2,9)]
                        if var+1 == len(result):
                                break
                        var += 1
                        
                digitar(f'\033[1;35m{num[0]}\033[m X \033[1;35m{num[1]}\033[m\n')
                sleep(0.5)
                resp = int(input('\033[mRESPOSTA: \033[1;32m'))
                if resp == num[0] * num[1]:
                        num.append(True)
                        result.append(num)
                else:
                        num.append(False)
                        result.append(num)

        total = time() - start
        digitar('\033[mFIM\n')
        sleep(1)

        if total >= 60:
                digitar(f"Você levou \033[1;31m{total:.0f} segundos\033[m para resolver as contas, \033[1;31mESTUDE MAIS\033[m!\n")
        if 30 <= total < 60:
                digitar(f'Você levou \033[1;33m{total:.0f} segundos\033[m para resolver as contas, \033[1;33mCONTINUE SE ESFORÇANDO\033[m!\n')
        if total < 30:
                digitar(f'Você levou \033[1;32m{total:.0f} segundos\033[m para resolver as contas, \033[1;32mCONTINUE ASSIM, PORRA\033[m!\n')

        for i in result:
                if i[2] == True:
                        digitar(f'\033[1;32m{i[0]} X {i[1]}\033[m = \033[1;35m{i[0]*i[1]}\033[m\n')
                        acertos += 1
                else:
                        digitar(f'\033[1;31m{i[0]} X {i[1]}\033[m = \033[1;35m{i[0]*i[1]}\033[m\n')

        digitar(f'\033[1;32mACERTOS: {acertos}\033[m\n')
        digitar(f'\033[1;31mERROS: {10 - acertos}\033[m')