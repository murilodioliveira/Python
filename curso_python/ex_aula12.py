nome = 'Murilo Henrique'
altura = 1.90
peso = 90
imc = peso/(altura**2)

print(nome, 'tem ', altura, ' de altura, pesa', peso, 'quilos e seu IMC é ', float(imc))

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
print(linha_1)
linha_2 = f'pesa {peso} quilos e seu IMC é {imc:.2f}'
print(linha_2)