import mysql.connector

try:
    # Conectar ao MySQL
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        database="gerenciamento"
    )

    # Criar a tabela Categoria
    with con:
        cur = con.cursor()
        cur.execute('CREATE TABLE Categoria(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))')

    # Criar a tabela Receitas
    with con:
        cur = con.cursor()
        cur.execute('CREATE TABLE Receitas(id INT AUTO_INCREMENT PRIMARY KEY, categoria VARCHAR(255), adicionado_em DATE, valor DECIMAL)')

    # Criar a tabela Gastos
    with con:
        cur = con.cursor()
        cur.execute('CREATE TABLE Gastos(id INT AUTO_INCREMENT PRIMARY KEY, categoria VARCHAR(255), retirado_em DATE, valor DECIMAL)')

    print("Tabelas criadas com sucesso!")

except mysql.connector.Error as e:
    print(f"Erro ao criar tabelas: {e}")

finally:
    # Fechar a conexão
    if 'con' in locals() and con.is_connected():
        con.close()
