from typing import List

from my_project.auth.dao import subroute_dao
from my_project.auth.service.general_service import GeneralService


class SubRouteService(GeneralService):

    _dao = subroute_dao

    def get_subroute_by_route(self, route_name: str) -> List[object]:
        return self._dao.find_by_route(route_name)
