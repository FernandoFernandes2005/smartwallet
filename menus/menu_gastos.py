from database.database import criar_gasto, listar_gastos, editar_gasto, remover_gastos, listar_categorias
from services.services import calcular_total
from utils.input_utils import input_float, input_int
from utils.date_utils import validar_data, data_hoje
from utils.logger_utils import logger

def menu_gastos(usuario):

    while True:

        print("\n=== Gestão de Gastos ===")
        print("1. Adicionar gasto")
        print("2. Ver gastos")
        print("3. Remover gasto")
        print("4. Editar gasto")
        print("0. Voltar")

        escolha = input_int("Escolha: ")

        if escolha == 1:

            descricao = input('Digite a descrição do gasto: ')

           
            valor = input_float('Digite o valor do gasto: ')
           

            categoria = listar_categorias()
            print("\nCategorias disponíveis:")
            for cat in categoria:
                print(f'{cat[0]} - {cat[1]}')
            categoria_id = input_int('Digite o ID da categoria: ')

            data_input = input('Digite a data (dd/mm/aaaa) ou Enter: ')

            if not data_input:
                data = data_hoje()
            else:
                if validar_data(data_input):
                    data = data_input
                else:
                    print("Data Inválida, tente novamente!")
                    continue

            criar_gasto(usuario[0], descricao, valor, categoria_id, data)
            logger.info(f"Gasto criado | usuario_nome={usuario[1]} | descricao={descricao} | valor={valor}")
            print('Gasto adicionado com sucesso!')
            
        elif escolha == 2:

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

        elif escolha == 3:

            gastos = listar_gastos(usuario[0])

            if not gastos:
                print('Nenhum gasto registrado.')
                continue

            for gasto in gastos:
                print(f'{gasto[0]} - {gasto[1]} (R${gasto[2]:.2f})')

            gasto_id = input_int('Digite o ID do gasto: ')
            remover_gastos(gasto_id)
            logger.info(f"Gasto removido | usuario_nome={usuario[1]} | gasto_id={gasto_id}")
            print('Gasto removido com sucesso!')
          

        elif escolha == 4:

            gastos = listar_gastos(usuario[0])

            if not gastos:
                print('Nenhum gasto registrado.')
                continue

            for gasto in gastos:
                print(f'{gasto[0]} - {gasto[1]} (R${gasto[2]:.2f})')

            

            gasto_id = input_int('Digite o ID do gasto: ')

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
                        logger.info(f"Gasto editado | usuario_nome={usuario[1]} | gasto_id{gasto_id}")
                        print("Gasto editado com sucesso!")
                        break

        elif escolha == 0:
            break
        else:
            print("Opção inválida.")