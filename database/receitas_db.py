from database.connection import conectar


def criar_receitas(usuario_id, descricao, valor, data):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO receitas (usuario_id, descricao, valor, data)
        VALUES (?, ?, ?, ?)
        """, (usuario_id, descricao, valor, data))


def listar_receitas(usuario_id):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id, descricao, valor, data
        FROM receitas
        WHERE usuario_id = ?
        """, (usuario_id,))

        return cursor.fetchall()


def calcular_receitas_mes(usuario_id, mes, ano):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT SUM(valor)
        FROM receitas
        WHERE usuario_id = ?
        AND substr(data,4,2) = ?
        AND substr(data,7,4) = ?
        """, (usuario_id, mes, ano))

        total = cursor.fetchone()[0]

        return total if total else 0