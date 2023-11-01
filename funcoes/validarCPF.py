def validacao(vetCPF):
    soma1 = soma2 = dig1 = dig2 = 0

    for i in range(9):
        soma1 += vetCPF[i] * (10 - i)
    
    div1 = soma1 // 11
    resto1 = soma1 - (div1 * 11)

    if resto1 >= 2:
        dig1 = 11 - resto1
    else:
        dig1 = 0
    
    for i in range(10):
        soma2 += vetCPF[i] * (11 - i)
    
    div2 = soma2 // 11
    resto2 = soma2 - (div2 * 11)

    if resto2 >= 2:
        dig2 = 11 - resto2
    else:
        dig2 = 0

    if vetCPF[9] == dig1 and vetCPF[10] == dig2:
        print('CPF VÁLIDO')
        cpf2 = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        print(cpf2)

    else: 
        print('CPF INVÁLIDO')

print('Validador de CPF')
nome = input('Nome completo: ')
cpf = input('Seu CPF: ')\
    .replace(' ','')\
    .replace('.','')\
    .replace('-','')

vetCPF = []
for i in range(len(cpf)):
    vetCPF.append(int(cpf[i]))
resp = validacao(vetCPF)
