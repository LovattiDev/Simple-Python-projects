PrecoProduto_troco = float(input('Digite o valor unitário do produto'))
Quantidade_troco = int(input('Digite a quantidade de produtos'))
DinheiroRecebido_troco = float(input('Digite o valor pago pelo cliente'))

ValorTotalCompra_troco = Quantidade_troco * PrecoProduto_troco
Troco_troco = DinheiroRecebido_troco - ValorTotalCompra_troco

print('Preço unitário do produto: R$', PrecoProduto_troco)
print('Quantidade de produtos:', Quantidade_troco)
print('Dinheiro recebido: R$', DinheiroRecebido_troco)

ValorFaltante_troco = (DinheiroRecebido_troco - ValorTotalCompra_troco) * -1

if Troco_troco >= 0:
    print('Troco: R$', Troco_troco)
else:
    print('Dinheiro insuficiente!  Valor a pagar: R$', ValorFaltante_troco)