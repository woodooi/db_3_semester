from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controllers import excursion_controller
from my_project.auth.domain import Excursion

excursion_bp = Blueprint('excursions', __name__, url_prefix='/excursions')


@excursion_bp.get('')
def get_all_excursions() -> Response:
    return make_response(jsonify(excursion_controller.find_all()), HTTPStatus.OK)

@excursion_bp.post('')
def create_excursion() -> Response:
    content = request.get_json()
    excursion = Excursion.create_from_dto(content)
    excursion_controller.create(excursion)
    return make_response(jsonify(excursion.put_into_dto()), HTTPStatus.CREATED)

@excursion_bp.put('/<int:id>')
def update_excursion(excursion_id: str) -> Response:
    content = request.get_json()
    excursion = Excursion.create_from_dto(content)
    excursion_controller.update(excursion_id, excursion)
    return make_response("excursion updated", HTTPStatus.OK)

@excursion_bp.patch('/<int:id>')
def patch_excursion(excursion_id: id) -> Response:
    content = request.get_json()
    excursion_controller.patch(excursion_id, content)
    return make_response("excursion updated", HTTPStatus.OK)

@excursion_bp.delete('/<int:id>')
def delete_excursion(excursion_id: int) -> Response:
    excursion_controller.delete(excursion_id)
    return make_response("excursion deleted", HTTPStatus.OK)
