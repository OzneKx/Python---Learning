rimeiroTermoPA = int(input('Primeiro termo da PA: '))
razaoPA = int(input('Razão da PA: '))
contador = 1
termos = total = 0
querMais = 10
print('Os dez primeiros termos de um PA são: ')
while querMais != 0:
    total += querMais
    while contador <= total:
        print(primeiroTermoPA, end=' → ')
        primeiroTermoPA += razaoPA
        contador += 1
    print('PAUSA! ')
    querMais = int(input('Quantos termos quer mostrar a mais? '))
print('Fim! Foram mostrados {} termos. '.format(total))