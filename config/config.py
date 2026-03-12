import os

# Abaixo, o diretório base do projeto.
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Abaixo, o banco de dados.
DB_PATH = os.path.join(BASE_DIR, "smartwallet.db")

# Abaixo, pastas de relatórios.
RELATORIOS_DIR = os.path.join(BASE_DIR, "relatorios")
PDF_DIR = os.path.join(RELATORIOS_DIR, "pdf")
CSV_DIR = os.path.join(RELATORIOS_DIR, "csv")
GRAFICOS_DIR = os.path.join(RELATORIOS_DIR, "graficos")

# Abaixo, logs do sistema.
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# Abaixo, a versão do sistema.
APP_VERSION = "2.0"