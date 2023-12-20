from typing import List

from my_project.auth.dao import route_dao
from my_project.auth.service.general_service import GeneralService

class RouteService(GeneralService):

    _dao = route_dao

    def get_route_by_name(self, str) -> object:

        return self._dao.find_by_name(str)
    
    def find_subroutes_by_name(self, str) -> List[object]:

        return self._dao.find_subroutes_by_name(str)
