from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controllers import schedule_controller
from my_project.auth.domain import Schedule

schedule_bp = Blueprint('schedules', __name__, url_prefix='/schedules')


@schedule_bp.get('')
def get_all_schedules() -> Response:
    return make_response(jsonify(schedule_controller.find_all()), HTTPStatus.OK)

@schedule_bp.post('')
def create_schedule() -> Response:
    content = request.get_json()
    schedule = Schedule.create_from_dto(content)
    schedule_controller.create(schedule)
    return make_response(jsonify(schedule.put_into_dto()), HTTPStatus.CREATED)

@schedule_bp.put('/<int:id>')
def update_schedule(schedule_id: str) -> Response:
    content = request.get_json()
    schedule = Schedule.create_from_dto(content)
    schedule_controller.update(schedule_id, schedule)
    return make_response("schedule updated", HTTPStatus.OK)

@schedule_bp.patch('/<int:id>')
def patch_schedule(schedule_id: id) -> Response:
    content = request.get_json()
    schedule_controller.patch(schedule_id, content)
    return make_response("schedule updated", HTTPStatus.OK)

@schedule_bp.delete('/<int:id>')
def delete_schedule(schedule_id: int) -> Response:
    schedule_controller.delete(schedule_id)
    return make_response("schedule deleted", HTTPStatus.OK)
