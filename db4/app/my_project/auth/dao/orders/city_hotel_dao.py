from typing import List

from sqlalchemy import text

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import CityHotel


class CityHotelDao(GeneralDAO):

    _domain_type = CityHotel

    def find_by_city(self, city: str) -> List[object]:
        return self._session.query(CityHotel).filter(CityHotel.city == city).order_by(CityHotel.city).all()

    def insert_route_stops_association(self, p_id_hotel, p_city_name):
            
        query = text("CALL InsertRouteStopsAssociation(:id_hotel, :city)")

        self._session.execute(query, {"id_hotel": p_id_hotel, "city": p_city_name})

        self._session.commit()
