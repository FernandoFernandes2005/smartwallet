from datetime import datetime
from database.database import listar_gastos, gastos_categoria
from menus.exportar import exportar_gastos_csv


def menu_relatorios(usuario):

    while True:

        print("\n=== Relatórios ===")
        print("1. Relatório mensal")
        print("2. Resumo mensal automático")
        print("3. Gastos por Categorias")
        print("4. Exportar relatório CSV")
        print("0. Voltar")

        escolha = input("Escolha: ")

        if escolha == "1":

            mes = input('Digite o mês (MM): ')
            ano = input('Digite o ano (AAAA): ')

            gastos = listar_gastos(usuario[0])

            gastos_filtrados = []

            for gasto in gastos:

                try:
                    data_obj = datetime.strptime(gasto[4], '%d/%m/%Y')
                except ValueError:
                    continue

                if data_obj.month == int(mes) and data_obj.year == int(ano):
                    gastos_filtrados.append(gasto)

            if not gastos_filtrados:
                print("Nenhum gasto encontrado.")
                continue

            total = 0

            print(f"\n=== Gastos de {mes}/{ano} ===")
            for gasto in gastos_filtrados:

                print(f'\n{gasto[1]} - R${gasto[2]:.2f} ({gasto[4]})')
                total += gasto[2]

            print('\n===Relatório Mensal===')
            print(f'\nTotal: R${total:.2f}')

        elif escolha == "2":

            gastos = listar_gastos(usuario[0])

            resumo = {}

            for gasto in gastos:

                try:
                    data_obj = datetime.strptime(gasto[4], '%d/%m/%Y')
                except ValueError:
                    continue

                chave = f"{data_obj.month:02d}/{data_obj.year}"

                if chave not in resumo:
                    resumo[chave] = 0

                resumo[chave] += gasto[2]

            print("\n=== Resumo Mês a Mês ===")

            for mes in sorted(resumo):
                print(f'{mes}: R${resumo[mes]:.2f}')

        elif escolha == "3":
            dados = gastos_categoria(usuario[0])

            if not dados:
                print('Nenhum gasto registrado para este período.')
                continue

            print('\n=== Gastos por Categoria ===')
            total = 0

            for categoria, valor in dados:
                print(f'{categoria}: R${valor:.2f}')
                total += valor
            print(f'\nTotal de gastos: R${total:.2f}')

        elif escolha == "4":

            mes = input('Digite o mês (MM): ')
            ano = input('Digite o ano (AAAA): ')
            exportar_gastos_csv(usuario[0], mes, ano)

        elif escolha == "0":
            break
        else:
            print("Opção inválida.")