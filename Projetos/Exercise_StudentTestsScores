lista_alunos = []
while True:
    nome_aluno = str(input('Nome do aluno: '))
    nota1_aluno = float(input('Nota da primeira prova do aluno: '))
    nota2_aluno = float(input('Nota da segunda prova do aluno: '))
    mediaNotaAluno = (nota1_aluno + nota2_aluno) / 2
    lista_alunos.append([nome_aluno, [nota1_aluno, nota2_aluno], mediaNotaAluno])
    continuar = int(input('[1] para continuar [2] para sair: '))
    if continuar == 2: break
print('=-=' * 15)
print(f'{"BOLETIM":^30}')
print(f'{"NÚMERO":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=-=' * 15)
for c, value in enumerate(lista_alunos):
    print(f'{c:<4} {value[0]:<10} {value[2]:>8.1f}')
while True:
    mostrarNota = int(input('Deseja mostrar a nota de qual aluno (999 para sair): '))
    if mostrarNota == 999: break
    else:
        print(f'Notas de {lista_alunos[mostrarNota][0]} são: {lista_alunos[mostrarNota][1]}')