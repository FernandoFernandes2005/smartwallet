from database.gastos_db import listar_gastos
from database.metas_db import progresso_metas
from database.receitas_db import calcular_receitas_mes
from database.dashboard_db import calcular_gastos_mes
from database.relatorios_db import gastos_categoria, gastos_descricao, categorias_mes
from datetime import datetime
from utils import gerar_pdf, pedir_mes_ano, input_int, exportar_gastos_csv

def menu_relatorios(usuario):

    while True:

        print("\n=== Relatórios ===")
        print("1. Detalhamento Mensal de Gastos")
        print("2. Gastos por Categorias")
        print("3. Exportar relatório CSV")
        print("4. Exportar relatório PDF")
        print("0. Voltar")

        escolha = input_int("Escolha: ")

        if escolha == 1:

            mes, ano = pedir_mes_ano()

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

            print('\n=== Gasto Mensal ===')
            print(f'\nTotal: R${total:.2f}')

    
        elif escolha == 2:

            mes, ano = pedir_mes_ano()
            dados = categorias_mes(usuario[0], mes, ano)

            if not dados:
                print('Nenhum gasto registrado para este mês.')
                continue

            print('\n=== Gastos por Categoria ===')
            total = 0

            for categoria, valor in dados:
                print(f'{categoria}: R${valor:.2f}')
                total += valor
            print(f'\nTotal de gastos: R${total:.2f}')

        elif escolha == 3:

            mes, ano = pedir_mes_ano()
            exportar_gastos_csv(usuario[0], mes, ano)

        elif escolha == 4:
            mes, ano = pedir_mes_ano()

            receitas = calcular_receitas_mes(usuario[0], mes, ano)
            gastos = calcular_gastos_mes(usuario[0], mes, ano)

            saldo = receitas - gastos
            categorias = categorias_mes(usuario[0], mes, ano)
            metas = progresso_metas(usuario[0])

            gerar_pdf(
                usuario[0],
                mes,
                ano,
                receitas,
                gastos,
                saldo,
                categorias,
                metas
            )

        elif escolha == 0:
            break
        else:
            print("Opção inválida.")