valor1 = float(input('Digite um número: '))
valor2 = float(input('Digite outro número: '))
maiorValor = 0
while True:
    print('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR NÚMERO\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA')
    escolha = int(input('Digite sua escolha: '))
    if 0 >= escolha > 5:
        print('Escolha novamente! ')
        continue
    elif escolha == 1:
        print('{} + {} = {} '.format(valor1, valor2, (valor1 + valor2)))
    elif escolha == 2:
        print('{} * {} = {} '.format(valor1, valor2, (valor1 * valor2)))
    elif escolha == 3:
        if valor1 > valor2:
            maiorValor += 1
            print('Foram digitados os números {} e {}. O maior deles é {} '.format(valor1, valor2, maiorValor))
        if valor1 == valor2:
            print('Foram digitados os números {} e {}. Logo, os dois valores são iguais! '.format(valor1, valor2))
    elif escolha == 4:
        valor1 = int(input('Você pediu para digitar outro número! Faça sua escolha: '))
        valor2 = int(input('Faça sua outra escolha: '))
    elif escolha == 5:
        break
print('Fim')