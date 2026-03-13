from database.connection import conectar

def criar_usuario(nome, email, senha):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
            (nome, email, senha)
        )


def buscar_usuario(email):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, nome, email, senha FROM usuarios WHERE email = ?",
            (email,)
        )

        return cursor.fetchone()