def calcular_moda(vetor):
    frequencias = {}
    
    for numero in vetor:
        if numero in frequencias:
            frequencias[numero] += 1
        else:
            frequencias[numero] = 1
    
    frequencia_maxima = max(frequencias.values(), default=0)

    if frequencia_maxima == 1:
        return "A moda não existe, todos os elementos são únicos."

    modas = [numero for numero, frequencia in frequencias.items() if frequencia == frequencia_maxima]

    if len(modas) == 1:
        return f"A moda é: {modas[0]}"
    else:
        return "A moda não existe, há múltiplos números com a mesma frequência máxima."

vetor_exemplo = [1, 2, 2, 3, 4, 4, 5]
resultado = calcular_moda(vetor_exemplo)
print(resultado)
