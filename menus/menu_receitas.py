from datetime import datetime
from database.database import criar_receitas, listar_receitas



def menu_receitas(usuario):

    while True:

        print("\n=== Gestão de Receitas ===")
        print("1. Adicionar receita")
        print("2. Ver receitas")
        print("0. Voltar")

        escolha = input("Escolha: ")

        if escolha == "1":

            descricao = input('Digite a descrição da receita: ')

            try:
                valor = float(input('Digite o valor da receita: '))
            except ValueError:
                print('Valor inválido.')
                continue

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

            criar_receitas(usuario[0], descricao, valor, data)
            print('Receita adicionada!')

        elif escolha == "2":

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

        elif escolha == "0":
            break
        else:
            print("Opção inválida.")