def somaVetor(vet):
    soma = 0
    for i in range(N):
        soma = soma + vet[i]
        
    return soma

vet = []
N = int(input('Entre com uma quantidade: '))
for i in range(N):
 vet.append(int(input('Entre com um número: ')))

result = somaVetor(vet)
print('\nSoma dos valores do vetor:', result)
