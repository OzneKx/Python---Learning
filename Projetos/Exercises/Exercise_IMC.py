seuPeso = float(input('Qual o teu peso (em kg)? '))
suaAltura = float(input('Qual sua altura (em metros)? '))
IMC = (seuPeso) / (suaAltura **2)
if IMC <= 18.5:
    print('Seu IMC é de {:.2f}. Você está \033[31mabaixo do peso! '.format(IMC))
elif IMC <= 25:
    print('Seu IMC é de {:.2f}. Seu peso está \033[32mideal! '.format(IMC))
elif IMC <= 30:
    print('Seu IMC é de {:.2f}. Você está com \033[33msobrepeso! '.format(IMC))
elif IMC <= 40:
    print('Seu IMC é de {:.2f}. Você está \033[31mobeso! '.format(IMC))
elif IMC > 30:
    print('Seu IMC é de {:.2f}. Você está com \033[31mobesidade mórbida! '.format(IMC))