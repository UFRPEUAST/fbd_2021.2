from datetime import datetime


class Grade:
    def __init__(self, codigo, status, total_horas, curso, id=None, data=None):
        self.id = id
        self.codigo = codigo
        self.status = status
        self.total_horas = total_horas
        self.curso = curso
        if data:
            self.data = data
        else:
            self.data = datetime.now().date()

    def __str__(self):
        return f'Código: {self.codigo} STATUS: {self.status} CURSO: {self.curso}'

    def get_data_dict(self):
        return {
            'id': self.id,
            'codigo': self.codigo,
            'status': self.status,
            'total_horas': self.total_horas,
            'curso': self.curso,

        }