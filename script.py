from faker import Faker
import random
import mysql.connector

fake = Faker()

# Valores aleatórios para setor_id, porte_id e eixo_id
def gerar_valores_aleatorios():
    setor_id = random.randint(1, 6)
    porte_id = random.randint(1, 4)
    eixo_id = random.randint(1, 3)  
    return setor_id, porte_id, eixo_id


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
    # Gerar dados fictícios
    titulo = fake.sentence(nb_words=3) 
    descricao = fake.text(max_nb_chars=200)  
    setor_id, porte_id, eixo_id = gerar_valores_aleatorios()

    cursor.execute("INSERT INTO perguntas (titulo, descricao, setor_id, porte_id, eixo_id) VALUES (%s, %s, %s, %s, %s)", (titulo, descricao, setor_id, porte_id, eixo_id))
    contador_linhas += 1

    # Fazer commit a cada 15 linhas inseridas
    if contador_linhas % 15 == 0:
        conn_mysql.commit()
        contador_commits += 1
        print(f"Commit {contador_commits} realizado. Linhas inseridas até agora: {contador_linhas}")


cursor.close()
conn_mysql.close()
