ano = 0
habitantesPaisA = int(input('Qual o número de habitantes do país A? '))
habitantesPaisB = int(input('Qual o número de habitantes do país B? '))
taxaCrescimentoPaisB = float(input('Qual a taxa de crescimento do país B %? '))
taxaCrescimentoPaisA = float(input('Qual a taxa de crescimento do país A %? '))
c = ''
porcentagemA = (taxaCrescimentoPaisA/100)
porcentagemB = (taxaCrescimentoPaisB/100)
if habitantesPaisA <= habitantesPaisB:
    while habitantesPaisA <= habitantesPaisB:
        habitantesPaisA += habitantesPaisA * porcentagemA
        habitantesPaisB += habitantesPaisB * porcentagemB
        ano += 1
print('A população do país A iguala ou supera a de B em {} anos'.format(ano))
if habitantesPaisA >= habitantesPaisB:
    while habitantesPaisA >= habitantesPaisB:
        habitantesPaisA += habitantesPaisA * porcentagemA
        habitantesPaisB += habitantesPaisB * porcentagemB
        ano += 1
print('A população do país B iguala ou supera a de A em {} anos'.format(ano))