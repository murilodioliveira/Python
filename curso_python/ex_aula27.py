nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

if (nome and idade != ""):
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if (" " in nome):
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[len(nome)-1]}")
else:
    print("Desculpe, você deixou campos vazios")

"""
RESOLUÇÃO MELHOR DO PROFESSOR

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if (" " in nome):
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios")


"""