from typing import List, Dict

from http import HTTPStatus
from flask import abort

from my_project.auth.service import route_stop_service
from my_project.auth.controllers.general_controller import GeneralController


class RouteStopController(GeneralController):

    _service = route_stop_service

    def find_stops_by_route(self, key: str) -> List[object]:
        return list(map(lambda x: x.put_into_dto(), self._service.get_cities_by_route(key)))
    
