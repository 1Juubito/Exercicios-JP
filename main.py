nome = input("Digite seu nome: ")
email = input("Digite seu email: ")

if nome and email:
    pos_a = email.find('@')
    servidor = email[pos_a:]
    if pos_a != -1 and '.' in servidor:
        print('Cadastro realizado com sucesso!')
    else:
        print('Email inválido')
else:
    print('Preencha todos os campos')