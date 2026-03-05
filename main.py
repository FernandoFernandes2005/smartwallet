from models.models import Usuario
from services.services import adicionar_gasto, calcular_total
from datetime import datetime
from database.database import criar_tabelas, criar_usuario, buscar_usuario, criar_gasto, listar_gastos, editar_gasto, gastos_descricao, gastos_categoria
from database.database import remover_gastos,criar_receitas, listar_receitas, calcular_total_receitas, calcular_receitas_mes, calcular_gastos_mes
from database.database import categorias_padrao, listar_categorias 
import hashlib
import csv

def menu(usuario):

    while True:

        print("\n=== SmartWallet ===")
        print("1. Gestão de Gastos")
        print("2. Gestão de Receitas")
        print("3. Relatórios")
        print("4. Dashboard Financeiro")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_gastos(usuario)

        elif escolha == "2":
            menu_receitas(usuario)

        elif escolha == "3":
            menu_relatorios(usuario)

        elif escolha == "4":
            menu_dashboard(usuario)

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

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
  categorias_padrao()

  print("=== Bem-vindo ao SmartWallet ===")

  while True:
        print("\n1 - Login")
        print("2 - Cadastrar")
        print("0 - Sair")

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
        elif escolha == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida.")

def exportar_gastos_csv(usuario_id, mes, ano):

    gastos = listar_gastos(usuario_id)
    gastos_filtrados = []

    for gasto in gastos:
        try:
            data_obj = datetime.strptime(gasto[4], '%d/%m/%Y')
        except ValueError:
            continue

        if data_obj.month == int(mes) and data_obj.year == int(ano):
            gastos_filtrados.append(gasto)

    if not gastos_filtrados:
        print("Nenhum gasto encontrado neste período.")
        return
    
    nome_arquivo = f'relatorio_{mes}_{ano}.csv'

    with open(nome_arquivo, "w", newline='', encoding='utf-8') as arquivo:
       writer = csv.writer(arquivo)
       writer.writerow(['Descrição', 'Categoria', 'Valor', 'Data'])


       for gasto in gastos_filtrados:
           writer.writerow([
                gasto[1],  # Descrição
                gasto[3],  # Categoria
                f'R${gasto[2]:.2f}',  # Valor formatado
                gasto[4]   # Data
           ])
    print(f"\nRelatório exportado com sucesso: {nome_arquivo}")



if __name__ == "__main__":
    main()