print('=-='*27)
print('Será que é possível se formar um triângulo? Escolha os lados e te falarei :P')
print('=-='*27)
ladoTri1 = int(input('Escolha um valor para um lado do triângulo: '))
ladoTri2 = int(input('Escolha um valor para outro lado do triângulo: '))
ladoTri3 = int(input('Escolha um valor para o lado restante do triângulo: '))
if ladoTri1 < (ladoTri2 + ladoTri3) and ladoTri2 < (ladoTri1 + ladoTri3) and ladoTri3 < (ladoTri1 + ladoTri2):
    print('É possível formar um triângulo. ')
else:
    print('Não é possível formar um triângulo. ')