import random
import string
import csv

def gerar_cpf_aleatorio():
    return ''.join(random.choices(string.digits, k=11))

def gerar_senha_aleatoria():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

dados = [{'CPF': gerar_cpf_aleatorio(), 'Senha': gerar_senha_aleatoria()} for _ in range(100)]

with open('./data/usuarios.csv', 'w', newline='') as arquivo:
    campos = ['CPF', 'Senha']
    writer = csv.DictWriter(arquivo, fieldnames=campos)
    writer.writeheader()
    writer.writerows(dados)