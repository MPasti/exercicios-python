l = int(input('Entre com a quantidade de litros vendidos: '))
s = (input('Entre com o tipo de combustível vendido\nA para Álcool\nG para gasolina\n')).upper()

if(s == "A"):
    if(l>20):
        print("O valor a ser pago pelo cliente é de R$ ",round((l*2.10) - (l*2.10)*(5/100), 2))
    else:
        print("O valor a ser pago pelo cliente é de R$ ", round((l*2.10) - (l*2.10)*(3/100), 2)), 
if(s == "G"):
    if(l>20):
        print("O valor a ser pago pelo cliente é de R$ ", round((l*3.30) - (l*3.30)*(6/100), 2))
    else:
        print("O valor a ser pago pelo cliente é de R$ ", round((l*3.30) - (l*3.30)*(4/100), 2))
