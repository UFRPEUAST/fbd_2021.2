from database.connect import ConnectDataBase
from modulos.grade_curricular.grade import Grade


class GradeDao:
    _TABLE_NAME = 'GRADE'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(titulo, carga_horaria, status, duracao, id_curso, codigo)' \
                   ' values(%s, %s, %s, %s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'
    _SELECT_BY_ID_CURSO = "SELECT * FROM {} WHERE ID_CURSO = '{}'"
    _SELECT_BY_ID_CURSO_IN_CURSO = "SELECT * FROM {} WHERE ID = '{}'"

    # update

    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    def salvar(self, grade):
        if grade.id is None:
            cur = self.database.cursor()
            cur.execute(self._INSERT_INTO, (grade.titulo, grade.carga_horaria, grade.status, grade.duracao, grade.id_curso, grade.codigo))
            id = cur.fetchone()[0]
            self.database.commit()
            cur.close()
            grade.id = id
            return grade
        else:
            raise Exception('Não é possível salvar')

    def get_all(self):
        grades = []
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_ALL)
        all_grade = cursor.fetchall()
        coluns_name = [desc[0] for desc in cursor.description]
        for grade_query in all_grade:
            data = dict(zip(coluns_name, grade_query))
            grade = Grade(**data)
            grades.append(grade)
        cursor.close()
        return grades

    def get_por_id(self, id):
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_BY_ID.format(self._TABLE_NAME, id))
        coluns_name = [desc[0] for desc in cursor.description]
        grade = cursor.fetchone()
        if not grade:
            return None
        data = dict(zip(coluns_name, grade))
        grade = Grade(**data)
        cursor.close()
        return grade


    def is_por_id_curso(self, id_curso):
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_BY_ID_CURSO.format(self._TABLE_NAME, id_curso))
        grade = cursor.fetchone()
        if not grade:
            return False
        return True

    def is_por_id_curso_in_curso(self, id_curso):
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_BY_ID_CURSO_IN_CURSO.format('CURSO', id_curso))
        grade = cursor.fetchone()
        if not grade:
            return False
        return True

    def get_id_curso(self, id_curso):
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_BY_ID_CURSO.format(self._TABLE_NAME, id_curso))
        coluns_name = [desc[0] for desc in cursor.description]
        grade = cursor.fetchone()
        if not grade:
            return None
        data = dict(zip(coluns_name, grade))
        grade = Grade(**data)
        cursor.close()
        return grade