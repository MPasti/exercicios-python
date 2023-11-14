def escolher_palavra():
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip()

def exibir_palavra_oculta(palavra, letras_adivinhadas):
    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            palavra_oculta += letra
        else:
            palavra_oculta += "_"
    return palavra_oculta

def jogar_forca(tentativas_fixas):
    palavra = escolher_palavra().upper()
    letras_adivinhadas = set()
    tentativas_restantes = tentativas_fixas

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra:")
    print(exibir_palavra_oculta(palavra, letras_adivinhadas))

    while tentativas_restantes > 0:
        tentativa = input("\nDigite uma letra: ").upper()

        if tentativa in letras_adivinhadas:
            print("Você já tentou esta letra. Tente outra vez.")
        elif tentativa in palavra:
            letras_adivinhadas.add(tentativa)
            print("Letra correta!")
        else:
            tentativas_restantes -= 1
            print(f"Letra incorreta. Tentativas restantes: {tentativas_restantes}")

        palavra_mostrada = exibir_palavra_oculta(palavra, letras_adivinhadas)
        print(palavra_mostrada)

        if palavra_mostrada == palavra:
            print("Parabéns! Você adivinhou a palavra!")
            break

    if tentativas_restantes == 0:
        print(f"Fim de jogo. A palavra era: {palavra}")

tentativas_fixas = 8  
jogar_forca(tentativas_fixas)
