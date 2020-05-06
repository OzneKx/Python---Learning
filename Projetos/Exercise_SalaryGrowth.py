from datetime import date
anoAtual = date.today().year
salarioInicial = float(input('Qual era o salário inicial? R$ '))
taxaAumento = 1.5
for c in range(1996, anoAtual + 1):
    taxaAumento = 2 * taxaAumento
    salarioAtual = salarioInicial + (salarioInicial * (taxaAumento/100))
    print('Salário em {}, era de R${:.2f}'.format(c, salarioAtual))