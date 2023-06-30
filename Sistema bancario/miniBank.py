# Made by Saul Paiva (https://github.com/saulpaiva/)

from decimal import Decimal

def has_more_than_two_decimal_places(value): # verifica se o valor tem no máximo 2 casas decimais
    decimal_value = Decimal(str(value))
    decimal_places = abs(decimal_value.as_tuple().exponent)
    if decimal_places > 2:
        return True
    return False

# # Test the function
# values = [3.14, 2.0, 5.678, 10.123456, 10]
# for value in values:
#     if has_more_than_two_decimal_places(value):
#         print(f"{value} has more than two decimal places")
#     else:
#         print(f"{value} does not have more than two decimal places")


menu = """
Selecione uma das opções:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

t = 0 # variável temporária
saldo = 0.00
limite = 500
extrato = "----- EXTRATO -----\n\n"
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        # print("Depósito")
        t = float(input("Digite um valor para depositar: "))
        if (t < 0):
            print("Valor inválido, por favor selecione novamente a operação desejada.")
        elif (has_more_than_two_decimal_places(t)):
            print("Valor inválido, por favor selecione novamente a operação desejada.")
        else:
            saldo += t
            print(f"\nSeu novo saldo é R$ {saldo}")
            extrato += "[hora] Depósito de R$ " + str(t) + "\n" + "Novo saldo da conta: R$" + str(saldo) + "\n\n"

    elif opcao == "s":
        # print("Saque")
        if (numero_saques == LIMITE_SAQUES):
            print("Limite de saques diário excedido!")
            continue

        t = float(input("Digite um valor para sacar: "))

        if (t < 0):
            print("Valor inválido, por favor selecione novamente a operação desejada.")

        elif (has_more_than_two_decimal_places(t)):
            print("Valor inválido, por favor selecione novamente a operação desejada.")
        
        elif (t > saldo):
            print("\nSaldo insuficiente, por favor selecione novamente a operação desejada.")

        else:
            saldo -= t
            print(f"\nSeu novo saldo é R$ {saldo}")

            extrato += "[hora] Saque de R$ " + str(t) + "\n" + "Novo saldo da conta: R$" + str(saldo) + "\n\n"

            numero_saques += 1

    elif opcao == "e":

        print("\n" + extrato + "-------------------")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
