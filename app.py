from flask import Flask
from modulos.curso.controller import app_empresa
from modulos.semestre.controller import app_semestre

app = Flask(__name__)
app.register_blueprint(app_empresa)
app.register_blueprint(app_semestre)

app.run()