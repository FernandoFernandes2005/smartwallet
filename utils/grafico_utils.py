import os
import matplotlib.pyplot as plt
from config.config import GRAFICOS_DIR

def gerar_grafico_categorias(dados, mes, ano):
    if not dados:
        print("Nenhum dado pra gerar gráfico.")
        return
    
    categorias = []
    valores = []

    for categoria, valor in dados:
        categorias.append(categoria)
        valores.append(valor)

    plt.figure(figsize=(8,6))

    plt.pie(
        valores,
        labels=categorias,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title(f"Gastos por Categoria - {mes}/{ano}")
    os.makedirs(GRAFICOS_DIR, exist_ok=True)

    nome_arquivo = os.path.join(
        GRAFICOS_DIR,
        f"grafico_{mes}_{ano}.png"
    )
    
    plt.savefig(nome_arquivo)
    #plt.show()
    plt.close()
    print(f"\nGráfico salvo em: {nome_arquivo}")

def gerar_grafico_evo(meses, saldos):
    if not meses:
        print("Nenhum dado para gerar gráfico!")
        return
    
    plt.figure(figsize=(8,5))
    plt.plot(meses, saldos, marker='o')

    plt.title("Evolução Financeira")
    plt.xlabel("Mês")
    plt.ylabel("Saldo (R$)")
    plt.grid(True)

    os.makedirs(GRAFICOS_DIR, exist_ok=True)

    nome_arquivo = os.path.join(
        GRAFICOS_DIR,
        "evolução_financeira.png"
    )

    plt.savefig(nome_arquivo)
    plt.show()
    plt.close()
    print(f"\nGráfico de evolução salvo em: {nome_arquivo}")