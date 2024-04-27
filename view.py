import sqlite3 as lite

#Criando conexão
con = lite.connect('dados.db')

# Funções de inserção

# Inserindo categoria
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria(nome) VALUES (?)" # interrogaçaõ pois posso receber qualquer valor
        cur.execute(query,i) 

def inserir_receita(i):
    with con:
        cur =con.cursor()
        query = "INSERT INTO (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)


def inserir_gastos(i):
    with con:
        cur =con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em,valor) VALUES (?,?,?)"
        cur.execute(query,i)

def deletar_receitas(i):
    with con:
        cur= con.cursor()
        query = "DELETE FROM * Receitas WHERE id=?"
        cur.execute(query,i)

def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM * GGastos WHERE id=?"
        cur.execute(query,i)

# Funções para ver dados 
def ver_categoria():
    lista_items = []
    with con:
        cur = con.cursor()
        cur.execute("SLECT * FROM Categoria")
        linha = cur.fetchall #  Fetchal pega todos os valores passados ..
        for l in linha :
            lista_items.append(l) 

    return lista_items()

def ver_receitas():
    lista_items = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_items.append(l)

    return lista_items

def ver_gastos():
    lista_items = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        linha = cur.fetchall()
        for l in linha:
            lista_items.append(l)

    return lista_items