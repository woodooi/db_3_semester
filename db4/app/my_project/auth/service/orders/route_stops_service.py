from typing import List

from my_project.auth.dao import route_stop_dao
from my_project.auth.service.general_service import GeneralService


class RouteStopService(GeneralService):

    _dao = route_stop_dao
    
    def get_cities_by_route(self, route_name: str) -> List[object]:
        return self._dao.find_all_stops_for_route(route_name)
