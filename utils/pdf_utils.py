import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from config.config import PDF_DIR, GRAFICOS_DIR
from utils.grafico_utils import gerar_grafico_categorias

def gerar_pdf(usuario_id, mes, ano, receitas, gastos, saldo, categorias, metas):

    os.makedirs(PDF_DIR, exist_ok=True)

    nome_arquivo = os.path.join(
        PDF_DIR,
        f"relatorio_{mes}_{ano}.pdf"
    )

    c = canvas.Canvas(nome_arquivo, pagesize=letter)

    y = 750

    # TÍTULO
    c.setFont("Helvetica-Bold", 18)
    c.drawString(180, y, "SMARTWALLET")
    y -= 25

    c.setFont("Helvetica-Bold", 14)
    c.drawString(160, y, "Relatório Financeiro")
    y -= 40

    # MÊS
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Mês: {mes}/{ano}")
    y -= 40

    # RESUMO
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Resumo Financeiro")
    y -= 20

    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Receitas: R${receitas:.2f}")
    y -= 20

    c.drawString(50, y, f"Gastos: R${gastos:.2f}")
    y -= 20

    c.drawString(50, y, f"Saldo: R${saldo:.2f}")
    y -= 40

    # CATEGORIAS
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Gastos por Categoria")
    y -= 20

    c.setFont("Helvetica", 11)

    for categoria, valor in categorias:
        c.drawString(50, y, f"{categoria}: R${valor:.2f}")
        y -= 18

    y -= 20

    # METAS
    if metas:

        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "Progresso das Metas")
        y -= 20

        c.setFont("Helvetica", 11)

        for descricao, progresso in metas:
            c.drawString(50, y, f"{descricao} - {progresso:.1f}%")
            y -= 18

    y -= 30

    # GRÁFICO
    gerar_grafico_categorias(categorias, mes, ano) #Gera o gráfico automaticamente

    caminho_grafico = os.path.join(
        GRAFICOS_DIR,
        f"grafico_{mes}_{ano}.png"
    )

    if os.path.exists(caminho_grafico):

        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "Distribuição dos Gastos")
        y -= 20

        imagem = ImageReader(caminho_grafico)

        c.drawImage(
            imagem,
            100,
            y - 200,
            width=400,
            height=200
        )

    c.save()

    print("\nRelatório PDF gerado com sucesso!")
    print("Arquivo salvo em:", nome_arquivo)