vet = []
n = 10
for i in range(n):
    vet.append(int(input('Entre um valor: ')))
for i in range(n):
    vet[i] = vet[i] * 3
print('Vetor multiplicado por 3: ')
print(vet)