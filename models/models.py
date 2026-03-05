class Gasto:
    def __init__(self, descricao, valor, data):
        self.descricao = descricao
        self.valor = valor
        self.data = data

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.gastos = []

    def adicionar_gasto(self, gasto):
        self.gastos.append(gasto)