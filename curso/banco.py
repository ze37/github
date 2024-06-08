#criar o banco de dados e as tabelas
import sqlite3 as con
# criar tabelas
sql_clientes = '''
    CREATE TABLE IF NOT EXISTS Cliente (
    ID_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    RG VARCHAR (12) NOT NULL,
    Name_Cliente VARCHAR(30) NOT NULL,
    Sobrenome_Cliente VARCHAR (40) NOT NULL,
    Telefone VARCHAR(12),
    Rua VARCHAR(40),
    Numero VARCHAR(5),
    Bairro VARCHAR (25)
    );
'''
sql_produtos= '''
    CREATE TABLE IF NOT EXISTS Produto (
    ID_Produto INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome_Produto VARCHAR (30) NOT NULL,
    Tipo_Produto VARCHAR (25) NOT NULL,    
    Preco DECIMAL(10,2) NOT NULL,
    Qtde_Estoque SMALLINT NOT NULL
    );
'''
sql_vendas = '''
    CREATE TABLE IF NOT EXISTS Venda (
    ID_Transacao INTEGER PRIMARY KEY AUTOINCREMENT,
    Nota_fiscal SMALLINT NOT NULL,
    ID_Cliente INTEGER NOT NULL,
    Data_Compra DATETIME,
    ID_Produto INTEGER NOT NULL,
    Quantidade SMALLINT NOT NULL,
    FOREING KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente),
    FOREING KEY (ID_Produto) REFERENCES Produto(ID_Produto)
    );
'''
try:
    conexao = con.connect('floricultura.db')
    cursor = conexao.cursor()

    cursor.execute(sql_clientes)
    cursor.execute(sql_produtos)
    cursor.execute(sql_vendas)

    conexao.commit()
except con.DatabaseError as erro:
    print("Erro no banco de dados", erro)
finally:
    if conexao:
        conexao.close()



















