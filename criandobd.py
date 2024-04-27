import sqlite3 as lite

con = lite.connect('dados.db')

#criando minha tabela categoria.

with con:
    cur =con.cursor()
    cur.execute('CREATE Table Categoria(id Interger PRIMARY KEY AUTO_NCREMENT, nome TEXT)')

with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Receitas(id INTERGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)')


with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Gastos(id INTERGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)')