from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controllers import guide_controller
from my_project.auth.domain import Guide

guide_bp = Blueprint('guides', __name__, url_prefix='/guides')


@guide_bp.get('')
def get_all_guides() -> Response:
    return make_response(jsonify(guide_controller.find_all()), HTTPStatus.OK)

@guide_bp.post('')
def create_guide() -> Response:
    content = request.get_json()
    guide = Guide.create_from_dto(content)
    guide_controller.create(guide)
    return make_response(jsonify(guide.put_into_dto()), HTTPStatus.CREATED)

@guide_bp.put('/<int:id>')
def update_guide(guide_id: str) -> Response:
    content = request.get_json()
    guide = Guide.create_from_dto(content)
    guide_controller.update(guide_id, guide)
    return make_response("guide updated", HTTPStatus.OK)

@guide_bp.patch('/<int:id>')
def patch_guide(guide_id: id) -> Response:
    content = request.get_json()
    guide_controller.patch(guide_id, content)
    return make_response("guide updated", HTTPStatus.OK)

@guide_bp.delete('/<int:id>')
def delete_guide(guide_id: int) -> Response:
    guide_controller.delete(guide_id)
    return make_response("guide deleted", HTTPStatus.OK)
