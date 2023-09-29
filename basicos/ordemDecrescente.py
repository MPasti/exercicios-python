num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

if num1 > num2:
    if num1 > num3:
        if num2 > num3:
            maior = num1
            doMeio = num2
            menor = num3
        else:
            maior = num1
            doMeio = num3
            menor = num2
    else:
        maior = num3
        doMeio = num1
        menor = num2
else:
    if num2 > num3:
        if num1 > num3:
            maior = num2
            doMeio = num1
            menor = num3
        else:
            maior = num2
            doMeio = num3
            menor = num1
    else:
        maior = num3
        doMeio = num2
        menor = num1

print("Valores em ordem decrescente:", maior, doMeio, menor)
