quantosCD = int(input('Você tem quantos CDs? '))
somaPrecoCD = 0
mediaPrecoCD = 0
for c in range(1, quantosCD + 1):
    quantoPagou = float(input('Quanto pagou em cada um desses CD em reais? O {}º custou R$: '.format(c)))
    somaPrecoCD += quantoPagou
    mediaPrecoCD = (somaPrecoCD)/(quantosCD)
print('Num total de {} CDs, foram gastos cerca de R${:.2f}. A média em reais gasta foi de R${:.2f}'.format(quantosCD, somaPrecoCD, mediaPrecoCD))