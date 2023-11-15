
# A MODA de um vetor de números é o número no vetor que é repetido com maior frequência.
# Se mais de um número for repetido com frequência máxima igual, não existirá uma moda.
# Escreva uma função que aceite um vetor de números e retorne a moda ou uma indicação de que
# a moda não existe.

import random

def moda(vetor):
    moda = []
    vet1 = []
    vet2 = []

    for i in range(tamanho):
        moda.append(0)
        for j in range(tamanho):
            if vetor[i] == vetor[j]:
                moda[i] += 1
    
    frequencia = moda[0] 
    valor = 0
    for i in range(tamanho): 
        if frequencia < moda[i]:
            frequencia = moda[i]
            valor = i 

    for i in range(tamanho):
        if moda[i] == frequencia:
            vet1.append(vetor[i])
        vet2 = vet1[::-1] 

    for i in range(len(vet1)): 
        if (vet1[i] != vet2[i]) or (i < len(vet1)-1 and vet1[i] != vet1[i+1]): 
            return -1 
        else:
            return vetor[valor]
    
    
vetor = []
print('Exercicio 03! \nA MODA de um vetor')
tamanho = (int(input("Entre o tamanho do vetor: ")))
for i in range(tamanho):
    vetor.append(int(input(f'Entre o {i+1}° valor: ')))

print(vetor,'\n')
resultado = moda(vetor)
if resultado == -1:
    print("Não existe uma moda.\n")
    
else:
    print(f"MODA = {resultado}\n")
