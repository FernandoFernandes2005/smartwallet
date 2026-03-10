from database.database import calcular_receitas_mes, calcular_gastos_mes, gastos_descricao

def menu_dashboard(usuario):

    while True:

        print("\n=== Financeiro ===")
        print("1. Resumo financeiro")
        print("2. Dashboard financeiro")
        print("0. Voltar")

        escolha = input("Escolha: ")

        if escolha == "1":

            mes = input('Digite o mês (MM): ')
            ano = input('Digite o ano (AAAA): ')

            total_receitas = calcular_receitas_mes(usuario[0], mes, ano)
            total_gastos = calcular_gastos_mes(usuario[0], mes, ano)

            saldo = total_receitas - total_gastos

            print(f"\n=== Resumo Financeiro - {mes}/{ano} ===")
            print(f"\nReceitas: R${total_receitas:.2f}")
            print(f"Gastos: R${total_gastos:.2f}")
            print(f"Saldo: R${saldo:.2f}")

        elif escolha == "2":

            mes = input('Digite o mês (MM): ')
            ano = input('Digite o ano (AAAA): ')

            total_receitas = calcular_receitas_mes(usuario[0], mes, ano)
            total_gastos = calcular_gastos_mes(usuario[0], mes, ano)

            saldo = total_receitas - total_gastos

            print(f"\n=== Dashboard Financeiro - {mes}/{ano} ===")
            print(f"\nReceitas: R${total_receitas:.2f}")
            print(f"Gastos: R${total_gastos:.2f}")
            print(f"Saldo: R${saldo:.2f}")

            dados = gastos_descricao(usuario[0], mes, ano)

            if not dados:
                print("Nenhum gasto registrado.")
                continue

            print("\nDistribuição dos gastos:")

            for desc, valor in dados:

                porcentagem = (valor / total_gastos) * 100 if total_gastos else 0
                barras = "=" * int(porcentagem / 5)

                print(f"{desc:<15} {barras} {porcentagem:.1f}%")

        elif escolha == "0":
            break
        else:
            print("Opção inválida.")