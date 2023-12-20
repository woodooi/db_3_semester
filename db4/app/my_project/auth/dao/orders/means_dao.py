from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import CityHotel


class MeanDao(GeneralDAO):

    _domain_type = CityHotel

    def find_by_name(self, name: str) -> List[object]:
        return self._session.query(CityHotel).filter(CityHotel.name == name).order_by(CityHotel.name).all()
