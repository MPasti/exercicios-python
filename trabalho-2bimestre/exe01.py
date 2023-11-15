# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma
# prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número
# de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a
# ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o
# valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de
# prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste
# momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a
# quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da
# seguinte forma: para pagamentos sem atraso, cobrar o valor da prestação, e quando houver
# atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(valor, dias_atraso):
    if dias_atraso == 0:
        return valor
    else:
        multa = valor * 0.03
        juros = valor * (0.001 * dias_atraso)
        return valor + multa + juros

def relatorioDiario(quantidade, totalPago):
    print("\Final do Dia:")
    print(f"Quantidade de prestações pagas: {quantidade}")
    print(f"Valor total pago: R${totalPago:.2f}")

quantidade = 0
totalPago = 0
print("Exercicio 01!\n Prestação de Contas")

while True:
    valor = float(input("Digite o valor da prestação (digite 0 para encerrar): "))
    
    if valor == 0:
        break

    dias_atraso = int(input("Digite o número de dias em atraso: "))

    valor_a_pagar = valorPagamento(valor, dias_atraso)

    print(f"Valor a ser pago: R${valor_a_pagar:.2f}")

    quantidade += 1
    totalPago += valor_a_pagar

relatorioDiario(quantidade, totalPago)
