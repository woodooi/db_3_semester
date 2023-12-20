from typing import List, Dict

from http import HTTPStatus
from flask import abort

from my_project.auth.service import route_service
from my_project.auth.controllers.general_controller import GeneralController


class RouteController(GeneralController):

    _service = route_service

    def find_by_name(self, key: str) -> object:
        obj = self._service.get_route_by_name(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        return obj.put_into_dto() 
    
    def find_subroutes_by_name(self, key: str) -> List[object]:
        return list(map(lambda x: x.put_into_dto(), self._service.find_subroutes_by_name(key)))
