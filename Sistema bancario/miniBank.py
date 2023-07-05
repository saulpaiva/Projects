# Sistema bancário simples, com funcionalidades de depósito, saque e extrato
# Made by Saul Paiva (https://github.com/saulpaiva/)


import datetime
from decimal import Decimal

timestamp = datetime.datetime.now().strftime("[%d-%m-%Y] - %H:%M:%S") # Registra a data e a hora das operações bancárias

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

t = 0.00 # variável temporária
saldo = 0.00
limite = 500
extrato = "----- EXTRATO -----\n\n"
numero_saques = 0
numero_depositos = 0
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
            saldo_formatado = f"{saldo:.2f}" # formata o saldo em :.2f (monetário)
            t_formatado = f"{t:.2f}" # formata t em :.2f (monetário)

            print(f"\nSeu novo saldo é R$ {saldo_formatado}")
            extrato += f"\033[93m{timestamp}\033[0m \nDepósito de R$ " + str(t_formatado) + "\n" + "Novo saldo: R$ " + str(saldo_formatado) + "\n\n"

            numero_depositos += 1

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
            saldo_formatado = f"{saldo:.2f}" # formata o saldo em :.2f (monetário)
            t_formatado = f"{t:.2f}" # formata t em :.2f (monetário)

            print(f"\nSeu novo saldo é R$ {saldo_formatado}")

            extrato += f"\033[93m{timestamp}\033[0m \nSaque de R$ " + str(t_formatado) + "\n" + "Novo saldo: R$ " + str(saldo_formatado) + "\n\n"

            numero_saques += 1

    elif opcao == "e":

        if (numero_depositos + numero_saques) == 0 :
            print("\n" + extrato + f"\033[93m{timestamp}\033[0m \nSem movimentações\n\n" + "-------------------")

        else :
            print("\n" + extrato + "-------------------")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
