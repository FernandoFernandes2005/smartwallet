from database.database import criar_receitas, listar_receitas
from utils.input_utils import input_float, input_int
from utils.date_utils import validar_data, data_hoje
from utils.logger_utils import logger

def menu_receitas(usuario):

    while True:

        print("\n=== Gestão de Receitas ===")
        print("1. Adicionar receita")
        print("2. Ver receitas")
        print("0. Voltar")

        escolha = input_int("Escolha: ")

        if escolha == 1:

            descricao = input('Digite a descrição da receita: ')

            
            valor = input_float('Digite o valor da receita: ')
            

            data_input = input('Digite a data (dd/mm/aaaa) ou Enter: ')

            if not data_input:
                data = data_hoje()
            else:
                if validar_data(data_input):
                    data = data_input
                else:
                    print("Data Inválida, tente novamente!")
                    continue

            criar_receitas(usuario[0], descricao, valor, data)
            logger.info(f"Receita criada | usuario_nome={usuario[1]} | descricao={descricao} | valor = {valor}")
            print('Receita adicionada!')

        elif escolha == 2:

            receitas = listar_receitas(usuario[0])

            if not receitas:
                print('Nenhuma receita registrada.')
                continue

            total = 0

            print("\n=== Suas Receitas ===")

            for receita in receitas:

                print(f'{receita[1]} - R${receita[2]:.2f}')
                print(f'Data: {receita[3]}\n')

                total += receita[2]

            print(f'Total de receitas: R${total:.2f}')

        elif escolha == 0:
            break
        else:
            print("Opção inválida.")