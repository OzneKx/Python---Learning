temperaturasDesejadas = int(input('Quantidade de temperaturas que serão digitadas: '))
listaTemperaturas = []
for c in range(1, temperaturasDesejadas + 1, 1):
    temperatura = listaTemperaturas.append(float(int(input('Informe a {}ª temperatura: '.format(c)))))
    temperaturasDesejadas += 1
print('A maior temperatura é {}'.format(max(listaTemperaturas)))
print('A menor temperatura é {}'.format(min(listaTemperaturas)))
print('A média das temperaturas é {:.2f}'.format(sum(listaTemperaturas)/len(listaTemperaturas)))