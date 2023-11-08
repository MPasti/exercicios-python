def calcularFatorial(n)
    if n == 0:
        return 1
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

def media(somaIdades):
    mediaIdades = somaIdades/30
    return mediaIdades

def mostrarFatorial(idades):
    for idade in idades:
        fatorial = calcularFatorial(idade)
        print(f"Valor: {idade}, Fatorial: {fatorial}")

def acimaMedia(idades, media):
    qt = 0
    for idade in idades:
        if idade > media:
            qt += 1
    return qt

def maiorIdade(idades, nomes):
    maior_idade = idades[0]
    pessoaMaiorIdade = nomes[0]
    for i in range(30):
        if idades[i] > maior_idade:
            maior_idade = idades[i]
            pessoaMaiorIdade = nomes[i]
    return pessoaMaiorIdade

def menorIdade(idades, nomes):
    menor_idade = idades[0]
    pessoaMenorIdade = nomes[0]
    for i in range(30):
        if idades[i] < menor_idade:
            menor_idade = idades[i]
            pessoaMenorIdade = nomes[i]
    return pessoaMenorIdade

nomes = []
idades = []
somaIdades = 0
qt = 0
for i in range(30):
            nomes.append(input(f"Entre o {i+1}º nome: "))

            while True:
                idadeEntrada = input(f"Entre a {i+1}º idade: ")

                if idadeEntrada.isdigit():
                    idade = int(idadeEntrada)
                    if idade > 0:
                        idades.append(idade)
                        somaIdades = somaIdades + idade
                        break
                    else:
                        print("Entre com uma idade maior que zero")
                else:
                    print("Entre com um número válido para a idade")

while True:
    print("Escolha uma opção:")
    print("a - Calcular média das idades")
    print("b - Contar idades acima da média")
    print("c - Encontrar pessoa com a maior idade")
    print("d - Encontrar pessoa com a menor idade")
    print("e - Calcular fatorial das idades")
    print("f - Sair")
    
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "a":
        mediaIdades = format(media(somaIdades), ".2f")
        print("Média das idades:", mediaIdades)

    elif opcao == "b":
        qt = acimaMedia(idades, mediaIdades)
        print("Quantidade de idades acima da média:", qt)

    elif opcao == "c":
        pessoaMaiorIdade = maiorIdade(idades, nomes)
        print("Pessoa com a maior idade:", pessoaMaiorIdade)

    elif opcao == "d":
        pessoaMenorIdade = menorIdade(idades, nomes)
        print("Pessoa com a menor idade:", pessoaMenorIdade)
    
    elif opcao == "e":
        mostrarFatorial(idades)

    elif opcao == "f":
        break

    else:
        print("Opção inválida. Tente novamente.")
