estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto']
nivel_minimo = 50

for i, qtd in enumerate(estoque):
    if qtd < nivel_minimo:
        print('{} está abaixo do nível mínimo. Temos apenas {} unidades.'.format(produtos[i], qtd))
