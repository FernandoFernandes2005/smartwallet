from database.connection import conectar

def criar_tabelas():
    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS gastos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            categoria_id INTEGER,
            data TEXT NOT NULL,
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
            FOREIGN KEY(categoria_id) REFERENCES categorias(id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS receitas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            data TEXT NOT NULL,
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS metas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            descricao TEXT NOT NULL,
            valor_meta REAL NOT NULL,
            valor_atual REAL DEFAULT 0,
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
        )
        """)