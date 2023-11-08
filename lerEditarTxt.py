with open('teste.txt', 'w') as arquivo:
    valor = input("Entre um valor para escrever no txt\n")
    arquivo.write(valor)
with open('teste.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo novo do arquivo\n" + conteudo)
