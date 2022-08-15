import psycopg2
class ConnectDataBase:
    def __init__(self):
        self._connect = psycopg2.connect(
            host="localhost",
            database="fbd_2021_2_acad",
            user="postgres",
            password="postgres"
        )
    def get_instance(self):
        return self._connect
#
# Dupla: Fulano e Sicrano
# 1- Descrição.
#     Desenvolveimento de um sistema para mapeamento de tomabmento escolar. O sistema vai registrar todos os bens de uma escola e salvar sua localização.
# Para o dados do bens, serão registraod, codigo.........
#
# 2 - Diagrama
# 3 - CREATEs
# 4 - Os endpoints
#
# 4.1:
#      endoint: /tombamento/bem/
#      method: GET
#      response: [
#          { id: '',
#            descrição:'' }
#            valor: ''
#      ]
# 4.2
# endoint: /tombamento/bem/add
# method: POT
# data: {
#     'drecricao'.....
# }