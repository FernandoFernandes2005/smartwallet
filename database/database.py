import sqlite3
from config.config import DB_PATH

def conectar():
    return sqlite3.connect(DB_PATH)


# ========================
# CRIAÇÃO DE TABELAS
# ========================

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


# ========================
# USUÁRIOS
# ========================

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


# ========================
# GASTOS
# ========================

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


# ========================
# RECEITAS
# ========================

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


def calcular_gastos_mes(usuario_id, mes, ano):

    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT SUM(valor)
        FROM gastos
        WHERE usuario_id = ?
        AND substr(data,4,2) = ?
        AND substr(data,7,4) = ?
        """, (usuario_id, mes, ano))

        total = cursor.fetchone()[0]

        return total if total else 0


# ========================
# RELATÓRIOS
# ========================

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


# ========================
# CATEGORIAS
# ========================

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


# ========================
# METAS
# ========================

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

def saldo_mes(usuario_id):
    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT substr(data, 4, 2) AS mes,
                   substr(data, 7, 4) AS ano,
                   SUM(valor)
            FROM receitas
            WHERE usuario_id = ?
            GROUP BY ano, mes
            ORDER BY ano, mes              
        """, (usuario_id,))
        receitas = cursor.fetchall()

        cursor.execute("""
            SELECT substr(data, 4, 2) AS mes,
                   substr(data, 7, 4) AS ano,
                   SUM(valor)
            FROM gastos
            WHERE usuario_id = ?
            GROUP BY ano, mes
            ORDER BY ano, mes
        """, (usuario_id,))
        gastos = cursor.fetchall()

        receitas_dict = {f"{m}/{a}": v for m,a,v in receitas}
        gastos_dict = {f"{m}/{a}": v for m,a,v in gastos}

        meses = sorted(set(receitas_dict.keys()) | set(gastos_dict.keys()))
        saldos = []

        for mes in meses:
            receita = receitas_dict.get(mes, 0)
            gasto = gastos_dict.get(mes, 0)
            saldos.append(receita - gasto)
        return meses, saldos
    
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
    
def resumo_financeiro(usuario_id):
    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT substr(data, 4 ,2) AS mes,
                   substr(data, 7, 4) AS ano,
                   SUM(valor)
            FROM receitas
            WHERE usuario_id = ?
            GROUP BY ano, mes                
            """,(usuario_id,))
        receitas = cursor.fetchall()

        cursor.execute("""
        SELECT substr(data,4,2) AS mes,
               substr(data,7,4) AS ano,
               SUM(valor)
        FROM gastos
        WHERE usuario_id = ?
        GROUP BY ano, mes
        """, (usuario_id,))
        gastos = cursor.fetchall()

        receitas_dict = {f"{m}/{a}": v for m,a,v in receitas}
        gastos_dict = {f"{m}/{a}": v for m,a,v in gastos}

        meses = sorted(set(receitas_dict.keys()) | set(gastos_dict.keys()))

        resultado = []

        for mes in meses:

            receita = receitas_dict.get(mes,0)
            gasto = gastos_dict.get(mes,0)

            saldo = receita - gasto

            resultado.append((mes, receita, gasto, saldo))

        return resultado

        

        

        