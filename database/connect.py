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
