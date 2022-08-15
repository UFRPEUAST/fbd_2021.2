from flask import Flask
from modulos.curso.controller import app_empresa
from modulos.semestre.controller import app_semestre
from modulos.grade_curricular.controller import app_grade

app = Flask(__name__)
app.register_blueprint(app_empresa)
app.register_blueprint(app_semestre)
app.register_blueprint(app_grade)

app.run()