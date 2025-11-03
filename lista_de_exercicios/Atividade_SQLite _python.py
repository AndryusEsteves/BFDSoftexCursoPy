# Importe o módulo sqlite3 e faça a conexão com o banco de dados escola_v2.db


# Use Left Join com as tabelas Aluno e Turma e imprima todos os dados da tabela.
# Usando a query da questão 4, adicione um filtro para pegar apenas os alunos da turma 2 e imprima na tela.


import sqlite3  # Importa o módulo para trabalhar com banco de dados SQLite

# Conecta ao banco de dados (ou cria se não existir)
conexao = sqlite3.connect("escola_v2.db")
cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL

# 1️ Seleciona todos os registros da tabela alunos
print("Todos os alunos:")
cursor.execute("SELECT * FROM alunos")
alunos = cursor.fetchall()  # Retorna todos os resultados da consulta
for aluno in alunos:
    print(aluno)

# 2️ Calcula a média entre nota1 e nota2, ordena em ordem decrescente e mostra os 10 maiores
print("\nTop 10 alunos por média:")
cursor.execute("""
    SELECT nome, (nota1 + nota2)/2 AS media
    FROM alunos
    ORDER BY media DESC
    LIMIT 10
""")
top_alunos = cursor.fetchall()
for nome, media in top_alunos:
    print(f"{nome} - Média: {media:.2f}")

# 3️ Faz um LEFT JOIN entre as tabelas alunos e turma
print("\nAlunos com informações da turma (LEFT JOIN):")
cursor.execute("""
    SELECT alunos.*, turma.nome_turma
    FROM alunos
    LEFT JOIN turma ON alunos.id_turma = turma.id
""")
dados_join = cursor.fetchall()
for dado in dados_join:
    print(dado)

# 4️ Mesmo LEFT JOIN, mas filtrando apenas alunos da turma 2
print("\nAlunos da turma 2:")
cursor.execute("""
    SELECT alunos.*, turma.nome_turma
    FROM alunos
    LEFT JOIN turma ON alunos.id_turma = turma.id
    WHERE turma.id = 2
""")
turma2 = cursor.fetchall()
for dado in turma2:
    print(dado)

# Fecha a conexão com o banco de dados
conexao.close()
