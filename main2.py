produtos = ['tv', 'geladeira', 'fogão', 'microondas', 'notebook', 'tablet', 'celular', 'smartwatch', 'smartband', 'smartphone']
estoque = [10, 5, 3, 7, 15, 20, 10, 5, 10, 15]

produto = input('Insira o nome do produto em letra minúscula: ')
if produto in produtos:
    i = produtos.index(produto)
    qtd_estoque = estoque[i]
    print('Temos {} unidades de {} no estoque'.format(qtd_estoque, produto))
else:
    print('{} não existe no estoque.'.format(produto))