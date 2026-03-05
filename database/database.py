import sqlite3

def conectar():
    return sqlite3.connect('smartwallet.db')

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS usuarios (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL UNIQUE,
                   senha TEXT NOT NULL
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
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
                     )
                     """)
    
    cursor.execute("""
                     CREATE TABLE IF NOT EXISTS receitas(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     usuario_id INTEGER,
                     descricao TEXT NOT NULL,
                     valor REAL NOT NULL,
                     data TEXT NOT NULL,
                     FOREIGN KEY (usuario_id) REFERENCES usuarios(id))
                     
                     """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT NOT NULL UNIQUE)""")

    conn.commit()
    conn.close()

def criar_usuario(nome, email, senha):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
                          "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                          (nome, email, senha)
                          )
        conn.commit()
        conn.close()

def buscar_usuario(email):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT id, nome, email, senha FROM usuarios WHERE email = ?", (email,))
        
        usuario = cursor.fetchone()
        conn.close()
        return usuario

def criar_gasto(usuario_id, descricao, valor, categoria_id, data):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
        "INSERT INTO gastos (usuario_id, descricao, valor, categoria_id, data) VALUES (?, ?, ?, ?, ?)",
        (usuario_id, descricao, valor, categoria_id, data)
    )
        conn.commit()
        conn.close()

def listar_gastos(usuario_id):
        conn = conectar()
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
        gastos = cursor.fetchall()
        conn.close()
        return gastos

def remover_gastos(gasto_id):
       conn = conectar()
       cursor = conn.cursor()

       cursor.execute("DELETE FROM gastos WHERE id = ?", 
                      (gasto_id,))
       conn.commit()
       conn.close()

def editar_gasto(gasto_id, descricao, valor, data):
       conn = conectar()
       cursor = conn.cursor()

       cursor.execute("UPDATE gastos SET descricao = ?, valor = ?, data = ? WHERE id = ?",
                      (descricao, valor, data, gasto_id))
       conn.commit()
       conn.close()

def criar_receitas(usuario_id, descricao, valor, data):
       conn = conectar()
       cursor = conn.cursor()

       cursor.execute("INSERT INTO receitas (usuario_id, descricao, valor, data) VALUES(?, ?, ?, ?)",
                      (usuario_id, descricao, valor, data))
       conn.commit()
       conn.close()

def listar_receitas(usuario_id):
       conn = conectar()
       cursor = conn.cursor()

       cursor.execute("SELECT id, descricao, valor, data FROM receitas WHERE usuario_id = ?",
                      (usuario_id,))
       receitas = cursor.fetchall()
       conn.close()
       return receitas

def calcular_total_receitas(usuario_id):
       conn = conectar()
       cursor = conn.cursor()

       cursor.execute("SELECT valor FROM receitas WHERE usuario_id = ?",
                      (usuario_id,))
       total = cursor.fetchone()[0]
       conn.close()
       if total is None:
              return 0
       return total 

def calcular_receitas_mes(usuario_id, mes, ano):
       conn = conectar()
       cursor = conn.cursor()

       cursor.execute("SELECT SUM(valor) FROM receitas WHERE usuario_id = ? " \
                      "AND substr(data, 4, 2) = ? " \
                      "AND substr(data, 7, 4) = ?",
                      (usuario_id, mes, ano))
       total = cursor.fetchone()[0]

       conn.close()
       if total is None:
              return 0
       return total

def calcular_gastos_mes(usuario_id, mes, ano):
       conn = conectar()
       cursor = conn.cursor()
       
       cursor.execute("SELECT SUM(valor) FROM gastos WHERE usuario_id = ? AND substr(data, 4, 2) = ? AND substr(data, 7, 4) = ?"""
                      , (usuario_id, mes, ano))
       
       total = cursor.fetchone()[0]
       conn.close()

       if total is None:
        return 0
       return total

def gastos_descricao(usuario_id, mes, ano):
     conn = conectar()
     cursor = conn. cursor()

     cursor.execute("SELECT descricao, SUM(valor) " \
                    "FROM gastos " \
                    "WHERE usuario_id = ? " \
                    "AND substr(data, 4, 2) = ? " \
                    "AND substr(data, 7, 4) = ? " \
                    "GROUP BY descricao",
                    (usuario_id, mes, ano))
     dados = cursor.fetchall()
     conn.close()
     return dados

def gastos_categoria(usuario_id):
        conn = conectar()
        cursor = conn. cursor()

        cursor.execute("""
        SELECT categorias.nome, SUM(gastos.valor)
        FROM gastos
        JOIN categorias
        ON gastos.categoria_id = categorias.id
        WHERE gastos.usuario_id = ?
        GROUP BY categorias.nome
    """, (usuario_id,))
        
        dados = cursor.fetchall()
        conn.close()
        return dados

def criar_categoria(nome):
       conn = conectar()
       cursor = conn.cursor()

       cursor.execute("INSERT OR IGNORE INTO categorias (nome) VALUES(?)",
                      (nome,))
       conn.commit()
       conn.close()

def listar_categorias():
       conn = conectar()
       cursor = conn.cursor()

       cursor.execute("SELECT id, nome FROM categorias")

       categorias = cursor.fetchall()
       conn.close()     
       return categorias

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