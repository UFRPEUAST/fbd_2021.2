from datetime import datetime


class Grade:
    REQUIRED_VALUES = ['codigo', 'titulo', 'carga_horaria', 'id_curso']

    def __init__(self, codigo, titulo, carga_horaria, status, id_curso, id=None, data=None, duracao=0):
        self.id = id
        self.codigo = codigo
        self.titulo = titulo
        self.carga_horaria = carga_horaria
        self.status = status
        self.duracao = duracao
        self.id_curso = id_curso
        if data:
            self.data = data
        else:
            self.data = datetime.now().date()

    def __str__(self):
        return f'Código: {self.titulo} STATUS: {self.status} CURSO: {self.id_curso}'

    def get_data_dict(self):
        return {
            'id': self.id,
            'codigo': self.codigo,
            'titulo': self.titulo,
            'status': self.status,
            'Duracao': self.duracao,
            'total_horas': self.carga_horaria,
            'curso': self.id_curso,

        }