vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
meta = 1000

qtd_bateu_meta = 0

for venda in vendas:
    if venda >= meta:
        qtd_bateu_meta += 1

qtd_funcionarios = len(vendas)
print('O percentual de pessoas que bateram a meta foi de {:.0%}'.format(qtd_bateu_meta / qtd_funcionarios))