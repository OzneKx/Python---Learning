from datetime import date
from time import sleep
fimDeAno = date.today().year
print('=-='*10)
print('\033[33mESTÁ CHEGANDO O ANO NOVO!\033[m ')
print('\033[32mHORA DA CONTÁGEM REGRESSIVA:\033[m ')
print('=-='*10)
for c in range(10, 0-1, -1):
    print(c)
    sleep(1)
print('\033[32mFELIZ ANO NOVO! ADEUS {}, FELIZ {}! '.format(fimDeAno, (fimDeAno + 1)))

for c in range(2, 51, 2):
    print(c, end=' ')
print('End ')