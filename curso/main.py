import sqlite3
#criar um banco de dados e conexäo
con = sqlite3.connect("cinema.db")
# criar um objeto cursor
cur = con.cursor()
cur.execute("CREATE TABLE filme(titulo,ano,duracao)")

#res = cur.execute("SELECT titulo FROM filme")
#print(res.fetchall())
# cur.execute("""
#     INSERT INTO filme VALUES
#     ('O senhor dos aneis: A sociedade do Anel', 2001, 165),
#     ('Conan O barbaro', 1985, 237)


# """)

dados_filmes = [("a casa bela",2000,124),
("o homem que desafiol o cao",2003,231),
("ilhas das cobras" ,2011,145),("leoa duorada",1982,432)]
cur.executemany("INSERT INTO filme (titulo,ano,duracao) VALUES(?,?,?)",dados_filmes)
con.commit()
con.close()