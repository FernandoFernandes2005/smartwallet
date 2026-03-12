from datetime import datetime

def validar_data(data_input):
    try:
        datetime.strptime(data_input, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def data_hoje():
    return datetime.now().strftime("%d/%m/%Y")