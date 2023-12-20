from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controllers import route_stop_controller
from my_project.auth.domain import CityHotel
from sqlalchemy import text
from ....db import db

route_stop_bp = Blueprint('route-stops', __name__, url_prefix='/route-stops')


@route_stop_bp.get('/<string:route_name>')
def get_cities_by_route(route_name: str) -> Response:
    return make_response(jsonify(route_stop_controller.find_stops_by_route(route_name)), HTTPStatus.OK)

@route_stop_bp.get('')
def get_all_route_stops() -> Response:
    return make_response(jsonify(route_stop_controller.find_all()), HTTPStatus.OK)

@route_stop_bp.post('')
def create_route_stop() -> Response:
    content = request.get_json()
    route_stop = CityHotel.create_from_dto(content)
    route_stop_controller.create(route_stop)
    return make_response(jsonify(route_stop.put_into_dto()), HTTPStatus.CREATED)

@route_stop_bp.put('/<string:route_name>/<string:city_name>')
def update_route_stop(route_name: str, city_name: str) -> Response:
    content = request.get_json()
    route_stop = CityHotel.create_from_dto(content)
    route_stop_controller.update(route_name, city_name, route_stop)
    return make_response("Route stop updated", HTTPStatus.OK)

@route_stop_bp.patch('/<string:route_name>/<string:city_name>')
def patch_route_stop(route_name: str, city_name: str) -> Response:
    content = request.get_json()
    route_stop_controller.patch(route_name, city_name, content)
    return make_response("Route stop updated", HTTPStatus.OK)

@route_stop_bp.delete('/<string:route_name>/<string:city_name>')
def delete_route_stop(route_name: str, city_name: str) -> Response:
    route_stop_controller.delete(route_name, city_name)
    return make_response("Route stop deleted", HTTPStatus.OK)

@route_stop_bp.route('/create-tables', methods=['POST'])
def create_dynamic_tables():
    try:
        db.session.execute(text('CALL DynamicTableCreationForRoutes()'))
        return jsonify({'message': 'Success'}), HTTPStatus.OK
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), HTTPStatus.INTERNAL_SERVER_ERROR
    

