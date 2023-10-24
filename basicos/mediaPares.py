vet = []
pares = []
qtd = 0
somaPares = 0
N = int(input('Entre com o tamanho do vetor: '))
for i in range(N):
 vet.append(int(input('Entre com um número: ')))
for i in range(N):
    if vet[i] % 2 == 0:
        pares.append(vet[i])
        somaPares = somaPares + vet[i]
        qtd = qtd + 1
print('Pares:')
print(pares)
print('Media Pares:')
print(somaPares/qtd)