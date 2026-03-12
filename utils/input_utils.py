def input_float(mensagem):
    while True:
       valor = input(mensagem)
       try:
           valor = float(valor)
           return valor
       except ValueError:
           print("Valor inválido. Digite uma opção válida!")
    


def pedir_mes_ano():
    mes = input("Digite o mês (MM): ")
    ano = input("Digite o ano (AAAA): ")

    return mes, ano

def input_int(mensagem):
    while True:
        valor = input(mensagem)
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print("Digite um número válido!")