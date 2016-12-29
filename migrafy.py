#!/usr/bin/python

import MySQLdb
import json
#from bson import json_util


class Maquina:
   'Comentario'
   
   count = 0

   def __init__(self, descricao, modelo, renda, capacidade, morada, stock):
      self.id = Maquina.count
      Maquina.count = Maquina.count + 1
      self.descricao = descricao
      self.modelo = modelo
      self.renda = renda
      self.capacidade = capacidade
      self.morada = morada
      self.stock = stock


class Morada:
   'Comentario'

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
   

produto1 = Produto("Lanche", "0.8", "0.5", "2016-12-01")
produto2 = Produto("Croissant", "0.5", "0.3", "2016-12-30")   
stock = [Stock(produto1, "20"), Stock(produto2, "49")]
morada1 = Morada("4710-057", "Campus de Gualtar", "Campus de Guatar", "", "Portugal", "Braga", "Braga")
maquina1 = Maquina("CP1 no segundo Piso", "A", "200", "300", morada1, stock)
venda = [Venda("2016-11-28 00:00:00", "0.80", "0.50", produto1, maquina1)]
utilizador = Utilizador("andreiabarros@gmail.com", "4321", "10.00", "Andreia Barros", "Estudante", "F", "1995-10-01", [venda])

print "-------------------------------------------"
print json.dumps(maquina1, cls=MyEncoder, indent=4)

print "\n-------------------------------------------"

print json.dumps(utilizador, cls=MyEncoder, indent=4)




# # Open database connection
# db = MySQLdb.connect("localhost","root","password","mydb" )

# # prepare a cursor object using cursor() method
# cursor = db.cursor()

# # Prepare SQL query to INSERT a record into the database.
# sql = "SELECT * FROM Maquina"

# # Execute the SQL command
# cursor.execute(sql)
# # Fetch all the rows in a list of lists.
# results = cursor.fetchall()
# for row in results:
# 	fname = row[0]
# 	lname = row[1]
# 	age = row[2]
# 	sex = row[3]
# 	income = row[4]
# 	# Now print fetched result
# 	print "fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
# 			(fname, lname, age, sex, income )


# # disconnect from server
# db.close()
