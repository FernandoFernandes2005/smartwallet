import csv
import os
from datetime import datetime
from database import listar_gastos
from config.config import CSV_DIR

def exportar_gastos_csv(usuario_id, mes, ano):
    os.makedirs(CSV_DIR, exist_ok=True)

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
    
    nome_arquivo = os.path.join(
            CSV_DIR,
            f"relatorio_{mes}_{ano}.csv"
    )
    with open(nome_arquivo, "w", newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([
            'Descrição',
            'Categoria',
            'Valor',
            'Data'
        ])

        for gasto in gastos_filtrados:
            writer.writerow([
                gasto[1],
                gasto[3],
                f'R${gasto[2]:.2f}',
                gasto[4]
            ])
    
    print(f"\nRelatório exportado com sucesso!")
    print("Arquivo salvo em:", nome_arquivo)