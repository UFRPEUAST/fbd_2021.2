from database.connect import ConnectDataBase
from modulos.curso.curso import Curso
from modulos.semestre.semestre import Semestre


class SemestreDao:
    _TABLE_NAME = 'SEMESTRE'
    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(descricao, status)' \
                   ' values(%s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_DESCRICAO = "SELECT * FROM {} WHERE descricao ilike '{}'"

    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    def salvar(self, semestre):
        if semestre.id is None:
            cur = self.database.cursor()
            cur.execute(self._INSERT_INTO, (semestre.descricao, semestre.status))
            id = cur.fetchone()[0]
            self.database.commit()
            cur.close()
            semestre.id = id
            return semestre
        else:
            raise Exception('Não é possível salvar')

    def get_all(self):
        try:
            semestres = []
            cursor = self.database.cursor()
            cursor.execute(self._SELECT_ALL)
            all_semestres = cursor.fetchall()
            columns_name = [desc[0] for desc in cursor.description]
            for semestre_query in all_semestres:
                data = dict(zip(columns_name, semestre_query))
                curso = Curso(**data)
                semestres.append(curso)
        except Exception as e:
            print(e)
        cursor.close()
        return semestres

    def get_por_descricao(self, descricao):
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_BY_DESCRICAO.format(self._TABLE_NAME, descricao))
        columns_name = [desc[0] for desc in cursor.description]
        semestre = cursor.fetchone()
        if not semestre:
            return None
        data = dict(zip(columns_name, semestre))
        semestre = Semestre(**data)
        cursor.close()
        return semestre