from http import HTTPStatus
from flask import Blueprint, jsonify, Response, json , request, make_response
from my_project.auth.controllers import hotel_controller
from my_project.auth.domain import Hotel
from my_project.auth.dao import hotel_dao

hotel_bp = Blueprint('hotels', __name__, url_prefix='/hotels')


@hotel_bp.get('')
def get_all_hotels() -> Response:
    return make_response(jsonify(hotel_controller.find_all()), HTTPStatus.OK)

@hotel_bp.post('')
def create_hotel() -> Response:
    content = request.get_json()
    hotel = Hotel.create_from_dto(content)
    hotel_controller.create(hotel)
    return make_response(jsonify(hotel.put_into_dto()), HTTPStatus.CREATED)

@hotel_bp.put('/<int:id>')
def update_hotel(hotel_id: str) -> Response:
    content = request.get_json()
    hotel = Hotel.create_from_dto(content)
    hotel_controller.update(hotel_id, hotel)
    return make_response("hotel updated", HTTPStatus.OK)

@hotel_bp.patch('/<int:id>')
def patch_hotel(hotel_id: id) -> Response:
    content = request.get_json()
    hotel_controller.patch(hotel_id, content)
    return make_response("hotel updated", HTTPStatus.OK)

@hotel_bp.delete('/<int:id>')
def delete_hotel(hotel_id: int) -> Response:
    hotel_controller.delete(hotel_id)
    return make_response("hotel deleted", HTTPStatus.OK)

@hotel_bp.route('/<string:filter>', methods=['GET'])
def get_price_information(filter: str):
    try:
        # Get the results from the stored procedure
        results = hotel_dao.get_price_value(filter)
        json_string = json.dumps(results, default=str)

        # Return the serialized results
        return {{'results': json_string}}, HTTPStatus.OK

    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), HTTPStatus.INTERNAL_SERVER_ERROR
    