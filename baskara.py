import math

ValorA_baskara = float(input('Digite o valor do coeficiente A'))
ValorB_baskara = float(input('Digite o valor do coeficiente B'))
ValorC_baskara = float(input('Digite o valor do coeficiente C'))

print('Coeficiente A:', ValorA_baskara)
print('Coeficiente B:', ValorB_baskara)
print('Coeficiente C:', ValorC_baskara)

ValorDelta_baskara = ValorB_baskara ** 2 - 4 * ValorA_baskara * ValorC_baskara

if ValorDelta_baskara < 0:
    print('Esta equação não possui raizes reais')
else:
    ValorX1_baskara = (-ValorB_baskara + math.sqrt(ValorDelta_baskara)) / 2 * ValorA_baskara
    ValorX2_baskara = (-ValorB_baskara - math.sqrt(ValorDelta_baskara)) / 2 * ValorA_baskara
    
    print('X1 =', round(ValorX1_baskara, 4))
    print('X2 =', round(ValorX2_baskara, 4))