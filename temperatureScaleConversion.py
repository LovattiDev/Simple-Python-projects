def temperatura():
    Escala_temperatura = input('Em qual escala você vai digitar a temperatura (C/F)?')

    if Escala_temperatura == 'C':
        Celsius_temperatura = float(input('Digite a temperatura em Celsius'))
        TemperaturaF_temperatura = (9 * Celsius_temperatura) / 5 + 32
        print('Temperatura em Fahrenheit:', round(TemperaturaF_temperatura, 2), '°F')
    elif Escala_temperatura == 'F':
        Fahrenheit_temperatura = float(input('Digite a temperatura em Fahrenheit'))
        TemperaturaC_temperatura = 5 / 9 * (Fahrenheit_temperatura - 32)
        print('Temperatura em Celsius:', round(TemperaturaC_temperatura, 2), '°C')
    else:
        print('Essa escala não pode ser utilizada')
    return

Confirmacao_temperatura = input('Deseja continuar (S/N)?')

while Confirmacao_temperatura == 'S':
    temperatura()
    Confirmacao_temperatura = input('Deseja continuar (S/N)?')
    