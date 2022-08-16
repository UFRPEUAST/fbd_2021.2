from datetime import datetime


class Aluno:
    def __init__(self, nome, cpf, id=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf


class CursoAluno:
    def __init__(self, id_aluno, id_curso, id=None):
        self.id = id
        self.id_aluno = id_aluno
        self.id_curso = id_curso