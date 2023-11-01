def formula(n):
    s = 0
    for i in range(n):
        s += (i+1) / ((i+1)**2)
    
    print(f'O resultado da fórmula é {s}')

nro = int(input('Entre o valor de Nº para ser calculado: '))
while nro <= 1:
    nro = int(input('Entre um número que seja maior que 1'))
resp = formula(nro)
