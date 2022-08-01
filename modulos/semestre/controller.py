from flask import make_response, jsonify, request, Blueprint

from modulos.semestre.dao import SemestreDao
from modulos.semestre.semestre import Semestre

app_semestre = Blueprint('app_semestre', __name__)
dao = SemestreDao()


@app_semestre.route('/semestre/', methods=['GET'])
def get_semestres():
    semestres = dao.get_all()
    data = [seemstre.get_data_dict() for seemstre in semestres]
    return make_response(jsonify(data))


@app_semestre.route('/semestre/add/', methods=['POST'])
def add_curso():
    data = request.form.to_dict(flat=True)
    semestre = dao.get_por_descricao(data.get('descricao'))
    if semestre:
        return make_response('Já existe um semestre com essa descrição', 400)
    data['status'] = True if data['status'] in [True, 1, 'TRUE', 'true', 'True'] else False
    semestre = Semestre(**data)
    semestre = dao.salvar(semestre)
    return make_response({
        'id': semestre.id
    })