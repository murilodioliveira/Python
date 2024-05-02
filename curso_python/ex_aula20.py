primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')



if primeiro_valor >= segundo_valor:
    #Podemos fazer referência ao imprimirmos uma variável desta maneira. Utilizando o f no inicio do print().
    print(f'{primeiro_valor=} é maior ou igual ao {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior do que {primeiro_valor=}')