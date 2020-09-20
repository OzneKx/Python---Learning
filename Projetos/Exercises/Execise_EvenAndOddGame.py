from random import randint
print('Vamos jogar par ou ímpar? ')
vitorias = 0
while True:
    digiteUmValor = int(input('Digite um número: '))
    computadorEscolha = randint(0, 10)
    somaParOuImpoar = (digiteUmValor + computadorEscolha)
    escolhaParOuImpar = ''
    while escolhaParOuImpar not in 'PI':
        escolhaParOuImpar = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Sua escolha foi o número {digiteUmValor}, enquanto a do computador foi {computadorEscolha}.\nA soma foi igual a: {somaParOuImpoar}.')
    print('Deu par! ' if somaParOuImpoar % 2 == 0 else 'Deu ímpar! ')
    if escolhaParOuImpar == 'P':
        if somaParOuImpoar % 2 == 0:
            print(f'você ganhou!')
            vitorias += 1
        elif somaParOuImpoar % 2 != 0:
            print('Você perdeu! ')
            break
    elif escolhaParOuImpar == 'I':
        if somaParOuImpoar % 2 != 0:
            print(f'você ganhou!')
            vitorias += 1
            continue
        elif somaParOuImpoar % 2 == 0:
            print('Você perdeu! ')
            break
    print('Vamos jogar novamente! ')
print(f'Você conquistou {vitorias} vitórias consecutivas! ')