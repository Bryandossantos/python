import sqlite3

conexao = sqlite3.connect('aulasegunda.db')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'nome TEXT, '
                'idade INT'
                ')')

cursor.execute('INSERT INTO clientes (nome, idade) VALUES ("Suele", 25)')
conexao.commit()

cursor.execute('SELECT id, nome, idade FROM clientes')

for linha in cursor.fetchall():
    print(linha)


cursor.close()
conexao.close()
