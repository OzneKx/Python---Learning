def fatorial(numero_fatorial=1, show=False):
    """
    → Calcula o fatorial de um número
    :param numero_fatorial: O número a ser calculado
    :param show: opção: mostrar ou não a conta
    :return: valor do fatorial
    """
    print(f'{numero_fatorial}! = ', end='')
    fat = 1
    for c in range(numero_fatorial, 0, -1):
        if show:
            if c > 1:
                print(f'{c}', end=' x ')
            elif c == 1:
                print(f'{c}', end=' = ')
        fat *= c
    return fat

numero_fatorial = int(input('Digite um número para saber seu fatorial: '))
mostar_processo = int(input('Deseja mostrar o processo de cálculo? [1] Sim [2] Não: '))
if mostar_processo == 1:
    show = True
else:
    show = False
print(fatorial(numero_fatorial, show=show))