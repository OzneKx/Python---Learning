listaNotas = []
listaGabarito = []
conditi0n = True
conz = True
nota = 0
contad0r = 0
contad0r2 = 0
conzdzd = 1
while len(listaGabarito) != 10:
    contad0r2 += 1
    gabarito = str(input('Digite a resposta da {}ª pergunta: '.format(contad0r2)))
    if gabarito != 'a' and gabarito != 'b' and gabarito != 'c' and gabarito != 'd' and gabarito != 'e':
        contad0r2 -= 1
        print('Resposta inválida! Tente novamente! ')
    else: listaGabarito.append(gabarito)
while conz:
    contad0r += 1
    nota = 0
    cond1 = True
    for c in range(0, 2):
        quealu = str(input('Qual a resposta da {}ª pergunta(a/b/c/d/e)? '.format(c + 1)))
        if quealu in listaGabarito[c]:
            nota += 1
            print('Resposta correta')
        if quealu not in listaGabarito[c]:
            print('Resposta incorreta')
            continue
    print('O {}º aluno tirou {}'.format(contad0r, nota))
    listaNotas.append(nota)
    while conditi0n:
        conditi0n = str(input('Outro aluno vai verificar o gabarito(sim/nao)? '))
        if conditi0n == 'sim':
            break
        if conditi0n == 'nao':
            conz = False
            break
print('O gabarito era {}' .format(listaGabarito))
print('O maior acerto foi de {}' .format(max(listaNotas)))
print('O menor acerto foi de {}' .format(min(listaNotas)))
print('A média de notas da turma foi de {:.2f}' .format(sum(listaNotas)/contad0r))
mediaNotas = 1
somaNotas = 0
term = int(input('Digite o ultimo termo da sequencia: '))
for c in range(1, term + 1):
    somaNotas += c/mediaNotas
    mediaNotas += 2
print('A soma da série é {:.2f}'.format(somaNotas))