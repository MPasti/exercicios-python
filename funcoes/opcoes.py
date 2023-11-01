def tabuada(numero):
    if 1 <= numero <= 9:
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    else:
        print("Número fora do intervalo (1 a 9).")

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def calcular_fatorial(numero):
    if numero < 0:
        return "Erro: Número negativo não tem fatorial."
    if numero == 0:
        return 1
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

while True:
    print("Selecione uma opção:")
    print("1. Tabuada")
    print("2. Calcular IMC")
    print("3. Calcular Fatorial")
    print("-1. Para sair")

    escolha = int(input("Opção: "))

    if escolha == -1:
        break

    if escolha == 1:
        numero = int(input("Digite um número (1 a 9): "))
        tabuada(numero)
    elif escolha == 2:
        peso = float(input("Digite o peso (em kg): "))
        altura = float(input("Digite a altura (em metros): "))
        imc = calcular_imc(peso, altura)
        print(f"Seu IMC é: {imc:.2f}")
    elif escolha == 3:
        numero = int(input("Digite um número para calcular o fatorial: "))
        resultado = calcular_fatorial(numero)
        print(f"{numero}! = {resultado}")
    else:
        print("Opção inválida. Tente novamente.")
