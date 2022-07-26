from database.connect import ConnectDataBase
from modulos.curso.curso import Curso


class CursoDao:
    _TABLE_NAME = 'CURSO'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(nome, sigla)' \
                   ' values(%s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'
    _SELECT_BY_SIGLA = "SELECT * FROM {} WHERE SIGLA ILIKE '{}'"

    # update

    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    def salvar(self, curso):
        if curso.id is None:
            cur = self.database.cursor()
            cur.execute(self._INSERT_INTO, (curso.nome, curso.sigla))
            id = cur.fetchone()[0]
            self.database.commit()
            cur.close()
            curso.id = id
            return curso
        else:
            raise Exception('Não é possível salvar')

    def get_all(self):
        cursos = []
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_ALL)
        all_cursos = cursor.fetchall()
        coluns_name = [desc[0] for desc in cursor.description]
        for curso_query in all_cursos:
            data = dict(zip(coluns_name, curso_query))
            curso = Curso(**data)
            cursos.append(curso)
        cursor.close()
        return cursos

    def get_por_id(self, id):
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_BY_ID.format(self._TABLE_NAME, id))
        coluns_name = [desc[0] for desc in cursor.description]
        curso = cursor.fetchone()
        if not curso:
            return None
        data = dict(zip(coluns_name, curso))
        curso = Curso(**data)
        cursor.close()
        return curso


    def is_por_sigla(self, sigla):
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_BY_SIGLA.format(self._TABLE_NAME, sigla))
        curso = cursor.fetchone()
        if not curso:
            return False
        return True
