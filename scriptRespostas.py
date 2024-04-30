from faker import Faker
import random
import mysql.connector

fake = Faker(locale='pt_BR')

def gerar_valores_aleatorios():
    Empresa_id = random.randint(1, 6)
    Perguntas_id = random.randint(1, 4)
    Formulario_id = random.randint(1, 3)
    return Empresa_id, Perguntas_id, Formulario_id

conn_mysql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rootroot',
    database='integrador'
)

cursor = conn_mysql.cursor()

contador_linhas = 0
contador_commits = 0

while True:
    resposta = fake.text(max_nb_chars=45)
    url_arquivo = fake.file_path(depth=2)
    Empresa_id, Perguntas_id, Formulario_id = gerar_valores_aleatorios()

    cursor.execute("INSERT INTO respostas (resposta, url_arquivo, Empresa_id, Perguntas_id, Formulario_id) VALUES (%s, %s, %s, %s, %s)", (resposta, url_arquivo, Empresa_id, Perguntas_id, Formulario_id))
    contador_linhas += 1

    if contador_linhas % 15 == 0:
        conn_mysql.commit()
        contador_commits += 1
        print(f"Commit {contador_commits} realizado. Linhas inseridas até agora: {contador_linhas}")

cursor.close()
conn_mysql.close()
