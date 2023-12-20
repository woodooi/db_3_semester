from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controllers import stop_controller
from my_project.auth.domain import Stop

stop_bp = Blueprint('stops', __name__, url_prefix='/stops')


@stop_bp.get('')
def get_all_schedules() -> Response:
    return make_response(jsonify(stop_controller.find_all()), HTTPStatus.OK)

@stop_bp.post('')
def create_stop() -> Response:
    content = request.get_json()
    stop = Stop.create_from_dto(content)
    stop_controller.create(stop)
    return make_response(jsonify(stop.put_into_dto()), HTTPStatus.CREATED)

@stop_bp.put('/<int:id>')
def update_stop(stop_id: str) -> Response:
    content = request.get_json()
    stop = Stop.create_from_dto(content)
    stop_controller.update(stop_id, stop)
    return make_response("stop updated", HTTPStatus.OK)

@stop_bp.patch('/<int:id>')
def patch_stop(stop_id: id) -> Response:
    content = request.get_json()
    stop_controller.patch(stop_id, content)
    return make_response("stop updated", HTTPStatus.OK)

@stop_bp.delete('/<int:id>')
def delete_stop(stop_id: int) -> Response:
    stop_controller.delete(stop_id)
    return make_response("stop deleted", HTTPStatus.OK)
