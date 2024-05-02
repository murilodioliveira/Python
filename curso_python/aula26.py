'''
FORMATAÇÃO BÁSICA DE STRINGS

s - string
d - int
f - float
.<número de dígitos>f - float
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
> - Direita
^ - Centro

Sinal - + ou -
= - Força o sinal a aparecer antes dos zeros
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:f^9}')
print(f'{1000.86134891834:0=+10,.2f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')