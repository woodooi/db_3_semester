from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Stop


class StopDao(GeneralDAO):

    _domain_type = Stop

    def find_by_city(self, city: str) -> List[object]:
        return self._session.query(Stop).filter(Stop.city == city).order_by(Stop.city).all()
