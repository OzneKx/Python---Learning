nomeUsuario = 1
senhaUsuario = 1
while nomeUsuario == senhaUsuario:
    nomeUsuario = str(input('Qual o seu nome? '))
    senhaUsuario = str(input('Digite sua senha? '))
    if nomeUsuario != senhaUsuario:
        print('Usuários e senha aceitos! ')
    else:
        print('Usuário e senha inválidos! Tente novamente! ')
        continue