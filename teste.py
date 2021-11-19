import sys
from time import sleep

print('sss')
print('gay')
sleep(1)
sys.stdout.write('\x1b[1A')

for i in range(0, 11):
    sleep(1)
    print(f'Tempo: {i}')
    sys.stdout.write('\x1b[1A')
    