from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request
from ....db import db
from sqlalchemy import text
from my_project.auth.dao import city_hotel_dao

city_hotel_bp = Blueprint('city-hotel', __name__, url_prefix='/city-hotel')

@city_hotel_bp.route('/insert', methods=['POST'])
def insert_route_stops_association():
    try:
        data = request.get_json()
        id_hotel = data.get('id_hotel')
        city = data.get('city')

        city_hotel_dao.insert_route_stops_association(id_hotel, city)

        return jsonify({'message': 'Success'}), HTTPStatus.OK

    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), HTTPStatus.INTERNAL_SERVER_ERROR
