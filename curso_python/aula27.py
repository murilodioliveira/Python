"""
FATIAMENTO DE STRINGS
 012345678
 Olá mundo
-987654321

Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str

"""

variavel = 'Olá mundo'
print(variavel[4:7]) #definindo o final
print(variavel[4:]) # omitindo o final ele irá até o final da string
print(variavel[0::3])
# Ao que parece o "f" indica o índice final menos 1 para ser impresso (f - 1)
# Já o "p" (passo) serve para pular os índices na quantidade especificada, na quantidade p - 1

print(variavel[0:len(variavel):2])

# Podemos inverter a ordem de uma string dessa forma:
print(variavel[::-1])