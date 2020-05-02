from random import randint
randomPC = randint(0, 10)
tentativa = 1
numeroX = int(input('Escolha um número aleatório de 0 a 10. O computador tentará adivinhar qual foi: '))
while numeroX != randomPC:
    numeroX = int(input('Errou, tente novamente: '))
    tentativa += 1
print('Você acertou, parabéns! Você conseguiu na {} tentativa! '.format(tentativa))