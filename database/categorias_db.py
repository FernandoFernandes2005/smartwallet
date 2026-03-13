from database.connection import conectar

def criar_categoria(nome):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT OR IGNORE INTO categorias (nome) VALUES (?)",
            (nome,)
        )


def listar_categorias():

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, nome FROM categorias"
        )

        return cursor.fetchall()


def categorias_padrao():

    categorias = [
        "Alimentação",
        "Transporte",
        "Moradia",
        "Lazer",
        "Saúde",
        "Educação",
        "Outros"
    ]

    for categoria in categorias:
        criar_categoria(categoria)
