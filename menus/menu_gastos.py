from datetime import datetime
from database.database import criar_gasto, listar_gastos, editar_gasto, remover_gastos, listar_categorias
from services.services import calcular_total


def menu_gastos(usuario):

    while True:

        print("\n=== Gestão de Gastos ===")
        print("1. Adicionar gasto")
        print("2. Ver gastos")
        print("3. Remover gasto")
        print("4. Editar gasto")
        print("0. Voltar")

        escolha = input("Escolha: ")

        if escolha == "1":

            descricao = input('Digite a descrição do gasto: ')

            try:
                valor = float(input('Digite o valor do gasto: '))
            except ValueError:
                print('Valor inválido.')
                continue

            categoria = listar_categorias()
            print("\nCategorias disponíveis:")
            for cat in categoria:
                print(f'{cat[0]} - {cat[1]}')
            categoria_id = int(input('Digite o ID da categoria: '))

            data_input = input('Digite a data (dd/mm/aaaa) ou Enter: ')

            if not data_input:
                data = datetime.now().strftime('%d/%m/%Y')
            else:
                try:
                    datetime.strptime(data_input, '%d/%m/%Y')
                    data = data_input
                except ValueError:
                    print('Data inválida.')
                    continue

            criar_gasto(usuario[0], descricao, valor, categoria_id, data)
            print('Gasto adicionado com sucesso!')
            
        elif escolha == "2":

            gastos = listar_gastos(usuario[0])

            if not gastos:
                print('Nenhum gasto registrado.')
                continue

            print('\n=== Seus Gastos ===')

            for gasto in gastos:
                print(f'{gasto[0]} - {gasto[1]}')
                print(f'Categoria: {gasto[3]}')
                print(f'R${gasto[2]:.2f}')
                print(f'Data: {gasto[4]}\n')

            total = calcular_total(usuario[0])
            print(f'Total de gastos: R${total:.2f}')

        elif escolha == "3":

            gastos = listar_gastos(usuario[0])

            if not gastos:
                print('Nenhum gasto registrado.')
                continue

            for gasto in gastos:
                print(f'{gasto[0]} - {gasto[1]} (R${gasto[2]:.2f})')

            try:
                gasto_id = int(input('Digite o ID do gasto: '))
                remover_gastos(gasto_id)
                print('Gasto removido com sucesso!')
            except ValueError:
                print('Entrada inválida.')

        elif escolha == "4":

            gastos = listar_gastos(usuario[0])

            if not gastos:
                print('Nenhum gasto registrado.')
                continue

            for gasto in gastos:
                print(f'{gasto[0]} - {gasto[1]} (R${gasto[2]:.2f})')

            try:

                gasto_id = int(input('Digite o ID do gasto: '))

                nova_descricao = input('Nova descrição (Enter mantém): ')
                novo_valor_input = input('Novo valor (Enter mantém): ')
                nova_data_input = input('Nova data (Enter mantém): ')

                for gasto in gastos:

                    if gasto[0] == gasto_id:

                        descricao = nova_descricao if nova_descricao else gasto[1]

                        if novo_valor_input:
                            valor = float(novo_valor_input)
                        else:
                            valor = gasto[2]

                        if nova_data_input:
                            data = nova_data_input
                        else:
                            data = gasto[4]

                        editar_gasto(gasto_id, descricao, valor, data)
                        print("Gasto editado com sucesso!")
                        break

            except ValueError:
                print("Entrada inválida.")

        elif escolha == "0":
            break
        else:
            print("Opção inválida.")