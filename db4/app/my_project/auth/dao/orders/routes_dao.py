from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Route
import sqlalchemy


class RouteDao(GeneralDAO):

    _domain_type = Route

    def find_by_name(self, str: str) -> List[object]:

        obj = self._session.query(Route).filter_by(start_end=str).first()
        return obj
    
    def find_subroutes_by_name(self, name: str) -> List[object]:
        route = self._session.query(Route).filter_by(start_end=name).first()

        if route:
            subroutes = route.subroutes
            return subroutes
        else:
            return []
