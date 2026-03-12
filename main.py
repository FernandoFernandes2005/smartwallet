from database.database import criar_tabelas, criar_usuario, buscar_usuario, categorias_padrao
from menus.menu_principal import menu
from utils.auth_utils import hash_senha
from utils.input_utils import input_int
from utils.logger_utils import logger
from utils.setup_utils import inicializar_pastas

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

                logger.info(f"Login realizado pelo usuário: {usuario[1]}")
                return usuario

        print("Email ou senha incorretos. Tente novamente.")
                      
def main():
  inicializar_pastas()
  criar_tabelas()
  categorias_padrao()

  print("=== Bem-vindo ao SmartWallet ===")

  while True:
        print("\n1 - Login")
        print("2 - Cadastrar")
        print("0 - Sair")

        escolha = input_int("Escolha uma opção: ")

        if escolha == 1:
            usuario_logado = realizar_login()
            menu(usuario_logado)
            
        elif escolha == 2:
            print("\n=== Cadastro ===")
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            senha_hash = hash_senha(senha)

            try:
                criar_usuario(nome, email, senha_hash)
                logger.info(f"Novo usuário cadastrado: {email}")
                print("Usuário cadastrado com sucesso!")
            except:
                print('Esse email já está cadastrado. Tente novamente.')
        elif escolha == 0:
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()