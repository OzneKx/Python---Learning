valorSacar = int(input('Informe o valor que deseja sacar: R$ '))
total = valorSacar
cedula = 100
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Todal de cédulas de {totalCedula} de R${cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        totalCedula = 0
        if total == 0: break