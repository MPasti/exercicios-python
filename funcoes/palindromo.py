def palindromo(valor):
    txt = valor[::-1]
    if(txt == valor):
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo")

print("Entre uma palavra, frase ou número para verificar se é um palíndromo")
valor = input("Entre um valor ").lower()
palindromo(valor)
