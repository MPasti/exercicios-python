n1 = int(input('Entre o primeiro número: '))
n2 = int(input('Entre o segundo número: '))
n3 = int(input('Entre o terceiro número: '))

if(n1 == n2 and n1 == n3 and n2 == n3):
    print('Se trata de um triangulo equilatero')
elif( n1 == n2 and n1 != n3) or (n2 == n3 and n2 != n1) or (n3 == n1 and n3 != n2):
    print('Se trata de um triangulo isósceles')
else:
    print('É um triangulo escaleno!')
