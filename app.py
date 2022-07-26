from flask import Flask, make_response, jsonify, request

from modulos.curso.curso import Curso
from modulos.curso.dao import CursoDao

app = Flask(__name__)
dao_curso = CursoDao()



@app.route('/curso/', methods=['GET'])
def get_cursos():
    cursos = dao_curso.get_all()
    data = [{'id': curso.id} for curso in cursos]
    return make_response(jsonify(data))

@app.route('/curso/add/', methods=['POST'])
def add_curso():
    print(request.method)
    data = request.form.to_dict(flat=True)
    print('data', data)
    curso = dao_curso.is_por_sigla(data.get('sigla'))
    if curso:
        return make_response('Sigla do curso já existe', 400)
    curso = Curso(**data)
    curso = dao_curso.salvar(curso)
    return make_response({
        'id': curso.id
    })


app.run()
