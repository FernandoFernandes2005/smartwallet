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
                   email TEXT NOT NULL,
                   senha TEXT NOT NULL
                   )
                   """)

    cursor.execute("""
                     CREATE TABLE IF NOT EXISTS gastos(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     usuario_id INTEGER,
                     descricao TEXT NOT NULL,
                     valor REAL NOT NULL,
                     data TEXT NOT NULL,
                     FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                     )
                     """)
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

def criar_gasto(usuario_id, descricao, valor, data):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO gastos (usuario_id, descricao, valor, data) VALUES(?, ?, ?, ?)",
                          (usuario_id, descricao, valor, data))
        conn.commit()
        conn.close()

def listar_gastos(usuario_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute ("SELECT id, descricao, valor, data FROM gastos WHERE usuario_id = ?",
                          (usuario_id,))
        
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
                         