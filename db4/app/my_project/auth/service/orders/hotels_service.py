from typing import List

from my_project.auth.dao import hotel_dao
from my_project.auth.service.general_service import GeneralService


class HotelService(GeneralService):

    _dao = hotel_dao

    def get_hotel_by_city(self, city: str) -> List[object]:
        return self._dao.find_by_city(city)
