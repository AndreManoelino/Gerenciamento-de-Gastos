import mysql.connector

try:
    # Conectando ao banco de dados MySQL
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        database='gerenciamento'
    )

    # Verificando se a conexão foi feita com sucesso
    if con.is_connected():
        print("Conexão com o banco de dados estabelecida com sucesso!")

    # Criando tabela Categoria
    with con.cursor() as cur:
        cur.execute('''
            CREATE TABLE Categoria (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255)
            )
        ''')

    # Criando tabela Receitas
    with con.cursor() as cur:
        cur.execute('''
            CREATE TABLE Receitas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                categoria VARCHAR(255),
                adicionado_em DATE,
                valor DECIMAL(10, 2)
            )
        ''')

    # Criando tabela Gastos
    with con.cursor() as cur:
        cur.execute('''
            CREATE TABLE Gastos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                categoria VARCHAR(255),
                retirado_em DATE,
                valor DECIMAL(10, 2)
            )
        ''')

    print("Tabelas criadas com sucesso!")

except mysql.connector.Error as e:
    print(f"Erro ao criar tabelas: {e}")

finally:
    if 'con' in locals() and con.is_connected():
        con.close()
