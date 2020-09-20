print('Dedução das potências de "i": ')
expoentei = int(input('Qual o expoente do "i" que deseja calcular? '))
deducaoexpoentei = expoentei % 4
if deducaoexpoentei == 0:
    print('Será igual a 1 ')
elif deducaoexpoentei == 1:
    print('Será igual a i ')
elif deducaoexpoentei == 2:
    print('Será igual a -1 ')
elif deducaoexpoentei == 3:
    print('Será igual a -i ')