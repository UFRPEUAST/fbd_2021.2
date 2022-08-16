from datetime import datetime


class Disciplina:
    def __init__(self, codigo, nome, total_horas, grade, id=None):
        self.id = id
        self.codigo = codigo
        self.total_horas = total_horas
        self.nome = nome
        self.grade = grade



    # def __str__(self):
    #     return f'Código: {self.codigo} STATUS: {self.status} CURSO: {self.curso}'
    #
    # def get_data_dict(self):
    #     return {
    #         'id': self.id,
    #         'codigo': self.codigo,
    #         'status': self.status,
    #         'total_horas': self.total_horas,
    #         'curso': self.curso,
    #
    #     }