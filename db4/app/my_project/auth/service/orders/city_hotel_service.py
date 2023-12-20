from typing import List

from my_project.auth.dao import city_hotel_dao
from my_project.auth.service.general_service import GeneralService


class CityHotelService(GeneralService):

    _dao = city_hotel_dao

    def get_cities_and_hotels(self, city: str) -> List[object]:
        return self._dao.find_by_city(city)
