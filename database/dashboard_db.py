from database.connection import conectar

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
