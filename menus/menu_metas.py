from database.database import criar_meta, listar_metas, atualizar_metas
from utils.input_utils import input_float, input_int
from utils.logger_utils import logger

def menu_metas(usuario):
    while True:
        print("\n==== Metas Financeiras ===")
        print("1. Criar Meta")
        print("2. Ver Metas")
        print("3. Atualizar Progresso")
        print("0. Voltar")

        escolha = input_int("Escolha: ")

        if escolha == 1:
            descricao = input("Descrição da meta: ")
            valor_meta = input_float("Valor da meta: ")

            criar_meta(usuario[0], descricao, valor_meta)
            logger.info(f"Meta criada | usuario_nome={usuario[1]} | descricao={descricao} | valor_meta={valor_meta}")
            print("Meta criada com sucesso!")

        elif escolha == 2:
            metas = listar_metas(usuario[0])

            if not metas:
                print("Nenhuma meta cadastrada!")
                continue

            print("\n=== Suas Metas ===")

            for meta in metas:
                progresso = (meta[3] / meta[2]) *100 if meta[2] else 0

                print(f"\nID: {meta[0]}")
                print(f"Meta: {meta[1]}")
                print(f"Objetivo: R${meta[2]:.2f}")
                print(f"Atual: R${meta[3]:.2f}")
                print(f"Progresso: {progresso:.1f}%")

        elif escolha == 3:
            metas = listar_metas(usuario[0])

            if not metas:
                print("Nenhuma meta cadastrada!")
                continue
            
            for meta in metas:
                print(f"{meta[0]} - {meta[1]} (R${meta[3]:.2f}/{meta[2]:.2f})")

            meta_id = input_int("Digite o ID da meta: ")
            valor = input_float("Valor a adicionar: ")

            atualizar_metas(meta_id, valor)
            logger.info(f"Meta atualizada | usuario_nome={usuario[1]} | meta_id={meta_id} | valor_adicionado={valor}")
            print("Progresso Atualizado!")

        elif escolha == 0:
            break

        else:
            print("Opção inválida!")