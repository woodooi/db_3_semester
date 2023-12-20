from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controllers import route_stop_controller
from my_project.auth.domain import CityHotel

mean_bp = Blueprint('means', __name__, url_prefix='/means')


@mean_bp.get('')
def get_all_means() -> Response:
    return make_response(jsonify(route_stop_controller.find_all()), HTTPStatus.OK)

@mean_bp.post('')
def create_mean() -> Response:
    content = request.get_json()
    mean = CityHotel.create_from_dto(content)
    route_stop_controller.create(mean)
    return make_response(jsonify(mean.put_into_dto()), HTTPStatus.CREATED)

@mean_bp.put('/<int:id>')
def update_mean(mean_id: str) -> Response:
    content = request.get_json()
    mean = CityHotel.create_from_dto(content)
    route_stop_controller.update(mean_id, mean)
    return make_response("Mean updated", HTTPStatus.OK)

@mean_bp.patch('/<int:id>')
def patch_mean(mean_id: id) -> Response:
    content = request.get_json()
    route_stop_controller.patch(mean_id, content)
    return make_response("Mean updated", HTTPStatus.OK)

@mean_bp.delete('/<string:mean>')
def delete_mean(mean_id: int) -> Response:
    route_stop_controller.delete(mean_id)
    return make_response("Mean deleted", HTTPStatus.OK)
