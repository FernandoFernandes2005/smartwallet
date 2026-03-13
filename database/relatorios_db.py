from database.connection import conectar

def gastos_descricao(usuario_id, mes, ano):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT descricao, SUM(valor)
        FROM gastos
        WHERE usuario_id = ?
        AND substr(data,4,2) = ?
        AND substr(data,7,4) = ?
        GROUP BY descricao
        """, (usuario_id, mes, ano))

        return cursor.fetchall()
    
def gastos_categoria(usuario_id):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT categorias.nome, SUM(gastos.valor)
        FROM gastos
        JOIN categorias
        ON gastos.categoria_id = categorias.id
        WHERE gastos.usuario_id = ?
        GROUP BY categorias.nome
        """, (usuario_id,))

        return cursor.fetchall()
    
def categorias_mes(usuario_id, mes, ano):
    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT categorias.nome, SUM(gastos.valor)
            FROM gastos
            JOIN categorias
            ON gastos.categoria_id = categorias.id
            WHERE gastos.usuario_id = ?
            AND substr(gastos.data, 4, 2) = ?        
            AND substr(gastos.data, 7, 4) = ?
            GROUP BY categorias.nome         
        """, (usuario_id, mes, ano))
    
        return cursor.fetchall()
    