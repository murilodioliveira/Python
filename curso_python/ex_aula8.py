nome = 'Murilo'
sobrenome = 'Oliveira'
idade = 101.5
ano_nascimento = 2024-idade
maior_de_idade = idade >= 18
print('Qual sua altura? ', end="")
altura_metros = float(input())

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de Nascimento:', ano_nascimento)

if(maior_de_idade):
    print('É maior de idade?', 'Sim')
else:
    print('É maior de idade?', 'Não')

print('Altura em metros:', altura_metros)