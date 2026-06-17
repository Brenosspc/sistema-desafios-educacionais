from database.database import conn, cursor

class SQLiteProvider:

    def listar_alunos(self):

        cursor.execute(
            "SELECT * FROM alunos"
        )

        return cursor.fetchall()

    def criar_aluno(self, nome):

        cursor.execute(
            "INSERT INTO alunos(nome) VALUES(?)",
            (nome,)
        )

        conn.commit()

    def listar_desafios(self):

        cursor.execute(
        "SELECT * FROM desafios"
    )

        return cursor.fetchall()

def criar_desafio(self, titulo, pontos):

    cursor.execute(
        "INSERT INTO desafios(titulo,pontos) VALUES(?,?)",
        (titulo, pontos)
    )

    conn.commit()