from models import Usuario
from services import adicionar_gasto, calcular_total
from datetime import datetime
import hashlib
from database import criar_tabelas, criar_usuario, buscar_usuario
from database import criar_gasto, listar_gastos, editar_gasto, remover_gastos

def menu(usuario):
    while True:
        print('\n1. Adicionar gasto')
        print('2. Ver total de gastos')
        print('3. Remover gasto')
        print('4. Editar gasto')
        print('5. Relatório Mensal')
        print('6. Resumo Mensal Automático')
        print('7. Sair')

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            descricao = input('Digite a descrição do gasto: ')

            try:
                valor = float(input('Digite o valor do gasto: '))
            except ValueError:
                print('Valor inválido. Por favor, digite um número.')
                continue

            data_input = input('Digite a data do gasto (dd/mm/aaaa) ou pressione Enter para usar a data atual: ')
            if not data_input:
                data = datetime.now().strftime('%d/%m/%Y')
            else:               
                try:
                    data = datetime.strptime(data_input, '%d/%m/%Y')
                    data = data_input
                except ValueError:
                    print('Data inválida. Por favor, use o formato dd/mm/aaaa.')
                    continue

            criar_gasto(usuario[0], descricao, valor, data)
            print('Gasto adicionado com sucesso!')

        elif escolha == '2':
            gastos = listar_gastos(usuario[0])

            if not gastos:
                print('Nenhum gasto registrado.')
                continue
            
            print('\n === Seus Gastos ===')
            for gasto in gastos:
               print(f'{gasto[0]} - {gasto[1]}')
               print(f'     R${gasto[2]:.2f}\n')
               print(f'     Data: {gasto[3]}\n')
            
            total = calcular_total(usuario[0])
            print(f'Total de gastos: R${total:.2f}')
        
        elif escolha == '3':
            gastos = listar_gastos(usuario[0])
            if not gastos:
                print('Nenhum gasto registrado para remover.')
                continue

            print('\nSelecione o número do gasto que deseja remover: ')

            for gasto in gastos:
                print(f'{gasto[0]} - {gasto[1]} (R${gasto[2]:.2f})')

            try:
                gasto_id = int(input('\nDigite o ID do gasto que deseja remover: '))
                remover_gastos(gasto_id)
                print('Gasto removido com sucesso!')

            except ValueError:
                print('Entrada inválida. Por favor, digite um número.')

        elif escolha == '4':
           gastos =  listar_gastos(usuario[0])
           if not gastos:
                print('Nenhum gasto registrado para editar.')
                continue
           
           print('\nSelecione o ID do gasto que deseja editar:\n')

           for gasto in gastos:
                print(f'{gasto[0]} - {gasto[1]} (R${gasto[2]:.2f})')

           try:
                gasto_id = int(input('\nDigite o ID do gasto que deseja editar: '))

                nova_descricao = input('Digite a nova descrição do gasto (pressione Enter para manter): ')
                novo_valor_input = input('Digite o novo valor do gasto (pressione Enter para manter): ')
                nova_data_input = input('Digite a nova data do gasto (dd/mm/aaaa) (ou pressione Enter para manter): ')

                for gasto in gastos:
                    if gasto[0] == gasto_id:
                       descricao = nova_descricao if nova_descricao else gasto[1]

                       if novo_valor_input:
                          try:
                                valor = float(novo_valor_input)
                          except ValueError:
                            print('Valor inválido. Mantendo valor anterior!.')
                            valor = gasto[2]
                       else:
                            valor = gasto[2]
                       if nova_data_input:
                          try:
                              data = datetime.strptime(nova_data_input, '%d/%m/%Y')
                              data = nova_data_input
                          except ValueError:
                                    print('Data inválida. Mantendo data anterior!.')
                                    data = gasto[3]
                       else:
                            data = gasto[3]
                            
                       editar_gasto(gasto_id, descricao, valor, data)
                       print('Gasto editado com sucesso!')
                       break
                    else:
                        print('ID do gasto não encontrado.')
           except ValueError:
                    print('Entrada inválida. Por favor, digite um número.')

        elif escolha == '5':
            gastos = listar_gastos(usuario[0])

            if not gastos:
                    print('Nenhum gasto registrado para gerar relatório.')
                    continue

            mes = input('Digite o mês para o relatório (MM): ')
            ano = input('Digite o ano para o relatório (AAAA): ')

            gastos_filtrados = []

            for gasto in gastos:
                try:
                    data_obj = datetime.strptime(gasto[3], '%d/%m/%Y')
                except ValueError:
                    continue

                if data_obj.month == int(mes) and data_obj.year == int(ano):
                    gastos_filtrados.append(gasto)

            if not gastos_filtrados:
                print(f'Nenhum gasto encontrado para {mes}/{ano}.')
                continue

            print(f'\n=== Relatório de Gastos para {mes}/{ano} ===')

            total = 0

            for gasto in gastos_filtrados:
                print(f'{gasto[1]} - R${gasto[2]:.2f} (Data: {gasto[3]})')
                total += gasto[2]

            print(f'\nTotal de gastos: R${total:.2f}')

        elif escolha == '6':
            gastos = listar_gastos(usuario[0])

            if not gastos:
                    print('Nenhum gasto registrado para gerar resumo.')
                    continue
            resumo_mensal = {}

            for gasto in gastos:
                try:
                    data_obj = datetime.strptime(gasto[3], '%d/%m/%Y')
                except ValueError:
                    continue

                chave = f"{data_obj.month:02d}/{data_obj.year}"

                if chave not in resumo_mensal:
                    resumo_mensal[chave] = 0

                resumo_mensal[chave] += gasto[2]

            print('\n=== Resumo Mensal de Gastos ===')
            for mes in sorted(resumo_mensal):
                print(f'{mes}: R${resumo_mensal[mes]:.2f}')

        elif escolha == '7':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')



def realizar_login():
    print("\n=== Login ===")

    while True:
        email_login = input("Digite seu email: ")
        senha_login = input("Digite sua senha: ")

        usuario = buscar_usuario(email_login)

        if usuario:
            senha_hash = hash_senha(senha_login)

            if usuario[3] == senha_hash:
                print(f"Bem-vindo, {usuario[1]}!")
                return usuario

        print("Email ou senha incorretos. Tente novamente.")

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()
                          
def main():
  criar_tabelas()

  print("=== Bem-vindo ao SmartWallet ===")

  while True:
        print("\n1 - Login")
        print("2 - Cadastrar")
        print("3 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            usuario_logado = realizar_login()
            menu(usuario_logado)
            
        elif escolha == "2":
            print("\n=== Cadastro ===")
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            senha_hash = hash_senha(senha)

            try:
                criar_usuario(nome, email, senha_hash)
                print("Usuário cadastrado com sucesso!")
            except:
                print('Esse email já está cadastrado. Tente novamente.')
        elif escolha == "3":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida.")
if __name__ == "__main__":
    main()

