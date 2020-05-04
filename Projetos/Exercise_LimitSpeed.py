print('A velocidade mínima é de 30km/h e a velocidade máxima é 80km/h. Fique entre esses dois! ')
print('O valor da multa para cada quilômetro irregular é de R$7,00 ')
velMin = 30
velMáx = 80
velLimites = (velMin, velMáx)
velocidadeAtual = int(input('Qual a sua velocidade atual? '))
multa = (velocidadeAtual <= velMin, velocidadeAtual >= velMáx)
print('Vai ser multado!' if multa else 'Não será multado! ')
if velocidadeAtual > velMáx:
    multaValor1 = ((velocidadeAtual - velMáx) * 7)
    print('O valor da multa será de R${:.2f}'.format(multaValor1))
else:
    velocidadeAtual < velMin
    multaValor2 = ((velMin - velocidadeAtual) * 7)
    print('O valor da multa será de R${:.2f}'.format(multaValor2))