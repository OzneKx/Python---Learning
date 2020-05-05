quantasPessoas = int(input('Digite um número de pessoas para analisar a idade de cada uma delas: '))
idadePessoas = 0
mediaIdade = 0
resultado = 0
for c in range(1, quantasPessoas+1):
    suaIdade = int(input('Qual a idade da {}° pessoa? '.format(c)))
    idadePessoas += suaIdade
    mediaIdade = (idadePessoas)/quantasPessoas
    if 0 < mediaIdade <= 25:
        resultado = 'Jovem'
    elif mediaIdade <= 60:
        resultado = 'Adulta'
    else:
        resultado = 'Idosa'
print('Num total de {} pessoas, a média da idade da turma é {}.'.format(quantasPessoas, resultado))