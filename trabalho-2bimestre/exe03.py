# Fazer um programa que desenvolva um jogo para adivinhar uma palavra oculta. Será um jogo
# semelhante ao da forca, mas com algumas diferenças. Neste jogo, o jogador tenta adivinhar uma
# palavra oculta, mediante uma quantidade de tentativas limitada. Para isso, o programa escolhe,
# aleatoriamente, uma palavra de uma lista de palavras contidas em um arquivo e o jogador deve
# adivinhar a palavra. Essa lista deve conter, no mínimo, 10 palavras. A quantidade de tentativas
# também deve ser aleatória, em um intervalo de 6 a 11. Quando o jogador adivinha alguma letra,
# as letras correspondentes na palavra são reveladas. Além disso, deve ser informado também a
# quantidade de tentativas que ainda resta quando a letra for incorreta, mensagem caso já tenha
# tentado a letra, e outras situações para tornar o jogo mais interessante. O jogo finaliza quando o
# jogador adivinhar a palavra ou acabar as suas tentativas.

import random

def escolherPalavra():
    with open("trabalho-2bimestre\palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip()

def palavraOculta(palavra, letrasAdv):
    palavra_oculta = ""
    for letra in palavra:
        if letra in letrasAdv:
            palavra_oculta += letra
        else:
            palavra_oculta += "_"
    return palavra_oculta

def jogoDaForca():
    palavra = escolherPalavra().upper()
    letrasAdv = set()
    tentativas = 8

    print("Exercicio 03! \nBem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra:")
    print(palavraOculta(palavra, letrasAdv))

    while tentativas > 0:
        tentativa = input("\nDigite uma letra: ").upper()

        if tentativa in letrasAdv:
            print("Você já tentou esta letra\n Tente outra vez.")
        elif tentativa in palavra:
            letrasAdv.add(tentativa)
            print("Letra correta!")
        else:
            tentativas -= 1
            print(f"Letra incorreta \nTentativas restantes: {tentativas}")

        palavra_mostrada = palavraOculta(palavra, letrasAdv)
        print(palavra_mostrada)

        if palavra_mostrada == palavra:
            print("Parabéns! Você adivinhou a palavra!")
            break

    if tentativas == 0:
        print(f"Você perdeu! :( \nA palavra era: {palavra}")


jogoDaForca()
