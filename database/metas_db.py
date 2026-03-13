from database.connection import conectar

def criar_meta(usuario_id, descricao, valor_meta):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO metas (usuario_id, descricao, valor_meta)
        VALUES (?, ?, ?)
        """, (usuario_id, descricao, valor_meta))


def listar_metas(usuario_id):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id, descricao, valor_meta, valor_atual
        FROM metas
        WHERE usuario_id = ?
        """, (usuario_id,))

        return cursor.fetchall()


def atualizar_metas(meta_id, valor):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE metas
        SET valor_atual = valor_atual + ?
        WHERE id = ?
        """, (valor, meta_id))

def progresso_metas(usuario_id):
    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT descricao, valor_meta, valor_atual
            FROM metas
            WHERE usuario_id = ?        
        """, (usuario_id,))

        metas = cursor.fetchall()
        resultado = []

        for descricao, meta, atual in metas:
            if meta == 0:
                progresso = 0
            else:
                progresso = (atual / meta) * 100
            
            resultado.append((descricao, progresso))
        return resultado