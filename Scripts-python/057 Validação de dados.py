sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Informe novamente: ')).strip().upper()[0]
print('Sexo {} Registrado com sucesso'.format(sexo))


