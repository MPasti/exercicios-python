h = float(input('Entre com a altura da pessoa: '))
s = (input('Entre com o sexo da pessoa\nM ou F:\n')).upper()

if(s == "M"):
    print('O peso para pessoas do sexo masculino com este tamanho é de', round(((72.7*h)-58),2))
elif(s == "F"):
    print('O peso para pessoas do sexo feminino com este tamanho é de', round(((62.1*h)-44.7),2))
else:    
    print('Sexo inválido!')
