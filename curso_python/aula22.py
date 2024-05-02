# OPERADORES LÓGICOS
# and (e) or (ou) not (não)
# or - Uma das condições precisam ser verdadeiras

# São consideradas falsy:
# 0, 0.0, '', False
# Também temos o tipo None que é usado para representar um não valor

'''
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456' #nunca deve ser utilizado uma senha dessa maneira não criptografada em plaintext

if (entrada =='E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
'''

print(True or False)
print(False or False or '123' or True)

# Avaliação de Curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)
