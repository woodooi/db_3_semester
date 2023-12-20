from typing import List

from my_project.auth.dao import stop_dao
from my_project.auth.service.general_service import GeneralService


class StopService(GeneralService):

    _dao = stop_dao

    def get_stop_by_city(self, city: str) -> List[object]:
        return self._dao.find_by_city(city)
