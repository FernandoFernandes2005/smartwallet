from models.models import Gasto
from database.database import listar_gastos

def adicionar_gasto(usuario, descricao, valor, data):
    gasto = Gasto(descricao, valor, data)
    usuario.gastos.append(gasto)

def calcular_total(usuario_id):
    gastos = listar_gastos(usuario_id)
    total = 0
    print('\nGastos:')
    for gasto in gastos:
        total += gasto[2]
    return total