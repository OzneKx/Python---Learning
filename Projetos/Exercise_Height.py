listaAltura = []
listaPeso = []
listaCodigo = []
numeroClientes = int(input('Qual o número de clientes que deseja avaliar? '))
for c in range(1, numeroClientes + 1, 1):
    codigoClientes = listaCodigo.append(int(input('Qual o código do {}º cliente? '.format(c))))
    alturaClientes = listaAltura.append(float(input('Qual a altura do {}º cliente em metros? '.format(c))))
    pesoClientes = listaPeso.append(float(input('Qual é o peso do {}º cliente em kg? '.format(c))))
    maisAlto = listaAltura.index(max(listaAltura))
    maisBaixo = listaAltura.index(min(listaAltura))
    maisGordo = listaPeso.index(max(listaPeso))
    maisMagro = listaPeso.index(min(listaPeso))
    mediaAltura = sum(listaAltura)/len(listaAltura)
    mediaPeso = sum(listaPeso)/len(listaPeso)
print('O maior cliente é o do código {:.0f}, com uma altura de {:.2f}'.format(listaCodigo[maisAlto], max(listaAltura)))
print('O menor cliente é o do código {:.0f}, com uma altura de {:.2f}'.format(listaCodigo[maisBaixo], min(listaAltura)))
print('O cliente com maior massa é o do código {:.0f}, com uma altura de {:.2f}'.format(listaCodigo[maisGordo], max(listaPeso)))
print('O cliente com menor massa é o do código {:.0f}, com uma altura de {:.2f}'.format(listaCodigo[maisMagro], min(listaPeso)))
print('A média das alturas é equivalente à {:.2f}'.format(mediaAltura))
print('A média dos pesos é equivalente à {:.2f}'.format(mediaPeso))