ano = 0
habitantesA = 80000
habitantesB = 200000
while habitantesA <= habitantesB:
    habitantesA += habitantesA * 0.03
    habitantesB += habitantesB * 0.015
    ano += 1
print('A população do país A iguala ou supera a de B em {} anos'.format(ano))