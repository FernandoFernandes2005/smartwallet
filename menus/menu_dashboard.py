from database.database import calcular_receitas_mes, calcular_gastos_mes, gastos_descricao, categorias_mes, saldo_mes, progresso_metas, resumo_financeiro
from utils.input_utils import pedir_mes_ano
from utils.grafico_utils import gerar_grafico_categorias, gerar_grafico_evo
from utils.input_utils import input_int
from menus.menu_metas import menu_metas

def menu_dashboard(usuario):

    while True:

        print("\n=== Financeiro ===")
        print("1. Resumo financeiro")
        print("2. Dashboard financeiro")
        print("3. Evolução financeira")
        print("4. Metas financeiras")
        print("0. Voltar")

        escolha = input_int("Escolha: ")

        if escolha == 1:

            dados = resumo_financeiro(usuario[0])

            if not dados:
                print("Nenhum histórico financeiro encontrado.")
                continue
            
            print(f"\n=== Histórico Financeiro ===")
            for mes, receita, gasto, saldo in dados:
                print(mes)
                print(f"\nReceitas: R${receita:.2f}")
                print(f"Gastos: R${gasto:.2f}")
                print(f"Saldo: R${saldo:.2f}")
                print()

        elif escolha == 2:

            mes, ano = pedir_mes_ano()

            total_receitas = calcular_receitas_mes(usuario[0], mes, ano)
            total_gastos = calcular_gastos_mes(usuario[0], mes, ano)

            saldo = total_receitas - total_gastos

            print(f"\n=== Dashboard Financeiro - {mes}/{ano} ===")
            print(f"\nReceitas: R${total_receitas:.2f}")
            print(f"Gastos: R${total_gastos:.2f}")
            print(f"Saldo: R${saldo:.2f}")

            dados = gastos_descricao(usuario[0], mes, ano)
            dados_categoria = categorias_mes(usuario[0], mes, ano)
        
            if not dados:
                print("Nenhum gasto registrado.")
                continue

            print("\nDistribuição dos gastos:")

            for desc, valor in dados:

                porcentagem = (valor / total_gastos) * 100 if total_gastos else 0
                barras = "=" * int(porcentagem / 5)

                print(f"{desc:<15} {barras} {porcentagem:.1f}%")
            
            
            metas = progresso_metas(usuario[0])

            if metas:
                print("\n=== Progresso das Metas ===")
                for descricao, progresso in metas:
                    barras = "█" * int(progresso / 5)
                    restante = "░" * (20 - int(progresso / 5))

                    print(f"{descricao}")
                    print(f"{barras}{restante} {progresso:.1f}%\n")

            if dados_categoria:
                gerar_grafico_categorias(dados_categoria, mes, ano)

        elif escolha == 3:
            meses, saldos = saldo_mes(usuario[0])
            gerar_grafico_evo(meses, saldos)

        elif escolha == 4:
            menu_metas(usuario)

        elif escolha == 0:
            break
        else:
            print("Opção inválida.")