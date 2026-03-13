from database.connection import conectar


def criar_gasto(usuario_id, descricao, valor, categoria_id, data):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO gastos (usuario_id, descricao, valor, categoria_id, data)
        VALUES (?, ?, ?, ?, ?)
        """, (usuario_id, descricao, valor, categoria_id, data))


def listar_gastos(usuario_id):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT gastos.id,
               gastos.descricao,
               gastos.valor,
               categorias.nome,
               gastos.data
        FROM gastos
        JOIN categorias
        ON gastos.categoria_id = categorias.id
        WHERE gastos.usuario_id = ?
        """, (usuario_id,))

        return cursor.fetchall()


def remover_gastos(gasto_id):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM gastos WHERE id = ?",
            (gasto_id,)
        )


def editar_gasto(gasto_id, descricao, valor, data):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE gastos
        SET descricao = ?, valor = ?, data = ?
        WHERE id = ?
        """, (descricao, valor, data, gasto_id))