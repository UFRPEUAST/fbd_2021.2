from flask import Flask, make_response, jsonify, request, Blueprint

from modulos.curso.curso import Curso
from modulos.curso.dao import CursoDao

app_empresa = Blueprint('example_blueprint', __name__)
dao_curso = CursoDao()


@app_empresa.route('/curso/', methods=['GET'])
def get_cursos():
    cursos = dao_curso.get_all()
    data = [curso.get_data_dict() for curso in cursos]
    return make_response(jsonify(data))


@app_empresa.route('/curso/add/', methods=['POST'])
def add_curso():
    data = request.form.to_dict(flat=True)
    curso = dao_curso.is_por_sigla(data.get('sigla'))
    if curso:
        return make_response('Sigla do curso já existe', 400)
    data['status'] = True if data['status'] in [True, 1, 'TRUE', 'true', 'True'] else False
    curso = Curso(**data)
    curso = dao_curso.salvar(curso)
    return make_response({
        'id': curso.id
    })