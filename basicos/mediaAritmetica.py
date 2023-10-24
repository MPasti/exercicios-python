acimaMedia = []
vet = []
media = 0
soma = 0
n = int(input('Entre a quantidade de alunos: '))
for i in range(n):
    vet.append(int(input('Entre a nota do '+ str(i+1) +'º aluno: ')))
for i in range(n):
    soma = soma + vet[i]
media = soma/n

for i in range(n):
    if vet[i] >= media:
        acimaMedia.append(vet[i])

print('Notas acima da média: ')
print(acimaMedia)