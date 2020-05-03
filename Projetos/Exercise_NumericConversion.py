digiteUmNumero = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão númerica: \n'
       '[1] BINÁRIO\n'
       '[2] DECIMAL\n'
       '[3] HEXADECIMAL')
digiteEscolhaBaseNumerica = int(input('Digite a opção desejada: '))
if digiteEscolhaBaseNumerica == 1:
    print('{} convertido em binário é: \033[33m{}'.format(digiteUmNumero, bin(digiteEscolhaBaseNumerica)[2:]))
elif digiteEscolhaBaseNumerica == 2:
    print('{} convertido em octal é: \033[33m{}'.format(digiteUmNumero, oct(digiteEscolhaBaseNumerica)[2:]))
elif digiteEscolhaBaseNumerica == 3:
    print('{} convertido em hexadecimal é: \033[33m{}'.format(digiteUmNumero, hex(digiteEscolhaBaseNumerica)[2:]))
else:
    print('Opção inválida, tente novamente.')