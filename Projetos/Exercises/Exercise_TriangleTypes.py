triangleSide1 = int(input('Digite um lado do triângulo: '))
triangleSide2 = int(input('Digite outrp lado do triângulo: '))
triangleSide3 = int(input('Digite o último lado do triângulo: '))
if triangleSide1 < (triangleSide2 + triangleSide3) and triangleSide2 < (triangleSide1 + triangleSide3) and triangleSide3 < (triangleSide1 + triangleSide2):
   print('É possível formar um triângulo! ')
   print('Agora veremos qual tipo de triângulo será formado! ')
   if triangleSide1 == triangleSide2 == triangleSide3:
        print('O triângulo é equilátero. ')
   elif triangleSide1 == triangleSide2 and triangleSide1 != triangleSide3:
        print('O triângulo é isósceles. ')
   elif triangleSide1 != triangleSide2 != triangleSide3 != triangleSide1:
        print('O triângulo é escaleno. ')
else:
    print('O triângulo não poderá ser formado ')
