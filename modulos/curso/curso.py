

class Curso:
    def __init__(self, nome, sigla, id=None, status=True):
        self.id = id
        self.nome = nome
        self.sigla = sigla
        self.status = status

    def __str__(self):
        return f'Nome: {self.nome} SIGLA: {self.sigla}'



