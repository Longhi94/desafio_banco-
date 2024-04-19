menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair   

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
             print("Operção falhou! Vaor informado é inválido")

    elif opcao == "s":
        valor = float(input("Informe valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo o suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print("Operção falhou! Vaor informado é inválido")


    elif opcao == "e":
        print("\n===========EXRATO===========")
        print("Não foram realizadas moviemntações." if not extrato else extrato) # Verifica se o estrato esta vazio, ele vai exibir o valorq euesta dentro da variavel extrato.d
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================")
    elif opcao == "q":
        break

    else:
        print("Opreação inválida, por favor selecione novamente a operação desejada.")