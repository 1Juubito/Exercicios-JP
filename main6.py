qtd_pessoas = int(input('Quantas pessoas terão no quarto? '))
quarto = []

for i in range(qtd_pessoas):
    nome = input('Digite o nome da pessoa: ')
    cpf = input('Digite o CPF: ')
    hospede = [nome, 'cpf: {}'.format(cpf)]
    quarto.append(hospede)

print(quarto)