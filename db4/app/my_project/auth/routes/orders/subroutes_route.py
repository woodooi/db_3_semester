from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controllers import subroute_controller
from my_project.auth.domain import Subroute

subroute_bp = Blueprint('subroutes', __name__, url_prefix='/subroutes')


@subroute_bp.get('')
def get_all_subroutes() -> Response:
    return make_response(jsonify(subroute_controller.find_all()), HTTPStatus.OK)

@subroute_bp.post('')
def create_subroute() -> Response:
    content = request.get_json()
    subroute = Subroute.create_from_dto(content)
    subroute_controller.create(subroute)
    return make_response(jsonify(subroute.put_into_dto()), HTTPStatus.CREATED)

@subroute_bp.put('/<int:id>')
def update_subroute(subroute_id: str) -> Response:
    content = request.get_json()
    subroute = Subroute.create_from_dto(content)
    subroute_controller.update(subroute_id, subroute)
    return make_response("subroute updated", HTTPStatus.OK)

@subroute_bp.patch('/<int:id>')
def patch_subroute(subroute_id: id) -> Response:
    content = request.get_json()
    subroute_controller.patch(subroute_id, content)
    return make_response("subroute updated", HTTPStatus.OK)

@subroute_bp.delete('/<int:id>')
def delete_subroute(subroute_id: int) -> Response:
    subroute_controller.delete(subroute_id)
    return make_response("subroute deleted", HTTPStatus.OK)
