from database import listar_gastos

def calcular_total(usuario_id):
    gastos = listar_gastos(usuario_id)
    total = sum(gasto[2] for gasto in gastos)
    return total