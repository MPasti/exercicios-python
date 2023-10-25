def maiorMenor(a,b):
    if a > b:
        print('O maior valor é %d' %a)
        return 
    elif a < b:
        print('O maior valor é %d' %b)
        return 
    else:
        print('Os valores são iguais')
        return 

x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
maiorMenor(x, y)

