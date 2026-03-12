from menus.menu_gastos import menu_gastos
from menus.menu_receitas import menu_receitas
from menus.menu_relatorios import menu_relatorios
from menus.menu_dashboard import menu_dashboard
from utils.input_utils import input_int

def menu(usuario):
    while True:

        print("\n===SmartWallet===")
        print("1. Gestão de Gastos")
        print("2. Gestão de Receitas")
        print("3. Relatórios")
        print("4. Dashboard Financeiro")
       
        print("0. Sair")

        escolha = input_int("Escolha uma opção: ")

        if escolha == 1:
            menu_gastos(usuario)
        
        elif escolha == 2:
            menu_receitas(usuario)

        elif escolha == 3:
            menu_relatorios(usuario)
        
        elif escolha == 4:
            menu_dashboard(usuario)
            
        elif escolha == 0:
            print("Saindo do sistema...")
            break
        else:
            print("Opção Inválida!")