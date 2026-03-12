import os
from config.config import(
    RELATORIOS_DIR,
    PDF_DIR,
    CSV_DIR,
    GRAFICOS_DIR,
    LOGS_DIR
)

def inicializar_pastas():
    pastas = [
        RELATORIOS_DIR,
        PDF_DIR,
        CSV_DIR,
        GRAFICOS_DIR,
        LOGS_DIR
    ]

    for pasta in pastas:
        os.makedirs(pasta, exist_ok=True)