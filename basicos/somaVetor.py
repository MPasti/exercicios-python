vet = []
soma = 0
N = int(input('Entre com uma quantidade: '))
for i in range(N):
 vet.append(int(input('Entre com um número: ')))
for i in range(N):
 soma = soma + vet[i]
print('\nVetor')
print(vet)
print('\nSoma dos valores do vetor: ', soma)
