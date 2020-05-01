from datetime import date
current_year = date.today().year


def voto(seu_nascimento):
    sua_idade = (current_year - seu_nascimento)
    if sua_idade < 16:
        return f'Com {sua_idade} anos o voto é negado! '
    elif 18 <= sua_idade <= 65:
        return f'Com {sua_idade} anos, o voto é obrigatório! '
    elif 16 <= sua_idade < 18 or sua_idade > 65:
        return f'Com {sua_idade} anos o voto é opcional! '


seu_nascimento = int(input('Digite seu ano de nascimento: '))
print(voto(seu_nascimento))