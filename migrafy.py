#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import json
#from bson import json_util


class Maquina:
   def __init__(self, idMaquina, descricao, modelo, renda, capacidade, morada, stock):
      self.idMaquina = idMaquina
      self.descricao = descricao
      self.modelo = modelo
      self.renda = renda
      self.capacidade = capacidade
      self.morada = morada
      self.stock = stock


class Morada:

   def __init__(self, Cod_Postal, Freguesia, Rua, Porta, Pais, Cidade, Distrito):
      self.Cod_Postal = Cod_Postal
      self.Freguesia = Freguesia
      self.Rua = Rua
      self.Porta = Porta
      self.Pais = Pais
      self.Cidade = Cidade
      self.Distrito = Distrito

class Venda:

    def __init__(self, Data, PrecoV, PrecoA, Produto, Maquina):
        self.Data = Data
        self.PrecoV = PrecoV
        self.PrecoA = PrecoA
        self.Produto = Produto
        self.Maquina = Maquina
        
class Utilizador:

    def __init__(self, Email, Password, Saldo, Nome, Profissao, Genero, Data_Nascimento, Venda):
      self.Email = Email
      self.Password = Password
      self.Saldo = Saldo
      self.Nome = Nome
      self.Profissao = Profissao
      self.Genero = Genero
      self.Data_Nascimento = Data_Nascimento
      self.Venda = Venda
      
class Produto:

    def __init__(self, Nome, PrecoV, PrecoA, Validade):
      self.Nome = Nome
      self.PrecoV = PrecoV
      self.PrecoA = PrecoA
      self.Validade = Validade

class Stock:

    def __init__(self, Produto, Quantidade):
      self.Produto = Produto
      self.Quantidade = Quantidade


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

def extracaoMoradaId(db, idMorada):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM Morada WHERE id = " + str(idMorada)

    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    row = cursor.fetchone()

    codPostal = row[1]
    freguesia = row[2]
    rua = row[3]
    porta = row[4]
    pais = row[5]
    cidade = row[6]
    distrito = row[7]

    # Get morada
    morada = Morada(codPostal, freguesia, rua, porta, pais, cidade, distrito)
    
    return morada


def extracaoStockIdMaquina(db, idMaquina):
    lStock = []

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM Remessa WHERE Maquina = " + str(idMaquina) + " and Quantidade > 0"

    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        validade = str(row[1])
        quantidade = str(row[2])
        idProduto = str(row[4])

        # Create Produto object
        produto = extracaoProdutoIdSemValidade(db, idProduto)
        produto.validade = validade

        # Create stock object
        stock = Stock(produto, quantidade)

        lStock.append(stock)
        
    return lStock

def extracaoProdutoIdSemValidade(db, idProduto):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM Produto WHERE id = " + str(idProduto)

    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    row = cursor.fetchone()

    nome = row[1]
    precoV = str(row[2])
    precoA = str(row[3])
    
    # Get morada
    produto = Produto(nome, precoV, precoA, "")
    
    return produto

def extracaoMaquinas(db):
    lMaquinas = []

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM Maquina"

    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        # Get Atributes
        idMaquina = row[0]
        descricao = row[1]
        modelo = row[2]
        renda = str(row[3])
        capacidade = str(row[4])
        idMorada = str(row[5])

        # Get morada
        morada = extracaoMoradaId(db, idMorada)
        # Get stock
        stock = extracaoStockIdMaquina(db, idMaquina)
        maquina = Maquina(idMaquina, descricao, modelo, renda, capacidade, morada, stock)

        # Now print fetched result
        lMaquinas.append(maquina)

    return lMaquinas


# Open database connection
db = MySQLdb.connect("localhost","root","password","mydb")

# Funcao que extrai as maquinas da db
lMaquinas = extracaoMaquinas(db)
print (json.dumps(lMaquinas, cls=MyEncoder, indent=4, ensure_ascii=False, encoding='latin-1').encode('utf-8'))

# disconnect from server
db.close()
