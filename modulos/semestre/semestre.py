class Semestre:
    def __init__(self, descricao, status, id=None):
        self.id = id
        self.descricao = descricao
        self.status = status

    def __str__(self):
        return f'Nome: {self.descricao} STATUS: {self.status}'

    def get_data_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'status': self.status
        }