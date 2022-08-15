from flask import Blueprint, jsonify, make_response, request

from modulos.grade_curricular.dao import GradeDao
from modulos.grade_curricular.grade import Grade

app_grade = Blueprint('app_grade', __name__)
app_name = 'grade'
dao_grade = GradeDao()


@app_grade.route(f'/{app_name}/', methods=['GET'])
def get_grades():
    grades = dao_grade.get_all()
    data = [grade.get_data_dict() for grade in grades]
    return make_response(jsonify(data))


@app_grade.route(f'/{app_name}/add/', methods=['POST'])
def add_grade():
    # 1 - Só deve criar uma grade se existir o curso.
    # 2 - Não pode existir duas grades com o mesmo códido do mesmo curso.
    data = request.form.to_dict(flat=True)
    erros = []
    for key in Grade.REQUIRED_VALUES:
        if key not in data.keys():
            erros.append({
                'coluna': key,
                'message': 'Este campo é obrigatório'
            })
    if erros:
        return make_response({
            'erros': erros
        }, 400)

    grade = dao_grade.is_por_id_curso(data.get('id_curso'))
    in_curso = dao_grade.is_por_id_curso_in_curso(data.get('id_curso'))
    # if grade:
    #     return make_response('Já existe uma grade com esse ID do curso', 400)
    if not in_curso:
        return make_response('Esse curso  não existe', 400)
    data['status'] = True if data.get('status', None) in [True, 1, 'TRUE', 'true', 'True'] else False
    grade = Grade(**data)
    grade = dao_grade.salvar(grade)
    return make_response({
        'id': grade.id
    })


@app_grade.route(f'/{app_name}/id/', methods=['GET'])
def get_grade_id():
    # 3 - Buscar por codigo (id)
    data = request.form.to_dict(flat=True)
    grade = dao_grade.get_por_id(data.get('id'))
    data = [grade.get_data_dict()]
    return make_response(jsonify(data))


@app_grade.route(f'/{app_name}/id_curso/', methods=['GET'])
def get_grade_id_curso():
    # 4 - Buscar por curso (id_curso)
    data = request.form.to_dict(flat=True)
    grade = dao_grade.get_id_curso(data.get('id_curso'))
    data = [grade.get_data_dict()]
    return make_response(jsonify(data))