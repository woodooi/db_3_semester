from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controllers import route_controller
from my_project.auth.domain import Route

route_bp = Blueprint('routes', __name__, url_prefix='/routes')

@route_bp.get('/<string:route_name>')
def get_route_by_name(route_name:  str) -> Response:

    return make_response(jsonify(route_controller.find_by_name(route_name)))

@route_bp.get('')
def get_all_routes() -> Response:

    return make_response(jsonify(route_controller.find_all()), HTTPStatus.OK)


@route_bp.get('/subroutes/<string:route_name>')
def get_all_subroutes(route_name: str) -> Response:

    return make_response(jsonify(route_controller.find_subroutes_by_name(route_name)), HTTPStatus.OK)


@route_bp.get('/<int:route_id>')
def get_route(route_id: int) -> Response:

    return make_response(jsonify(route_controller.find_by_id(route_id)), HTTPStatus.OK)

@route_bp.put('/<int:route_id>')
def update_route(route_id: int) -> Response:

    content = request.get_json()
    route = Route.create_from_dto(content)
    route_controller.update(route_id, route)
    return make_response("Route updated", HTTPStatus.OK)


@route_bp.patch('/<int:route_id>')
def patch_route(route_id: int) -> Response:

    content = request.get_json()
    route_controller.patch(route_id, content)
    return make_response("Route updated", HTTPStatus.OK)


@route_bp.delete('/<int:route_id>')
def delete_route(route_id: int) -> Response:

    route_controller.delete(route_id)
    return make_response("Route deleted", HTTPStatus.OK)

