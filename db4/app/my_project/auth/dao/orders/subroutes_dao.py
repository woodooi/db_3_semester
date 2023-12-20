from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Subroute


class SubRouteDao(GeneralDAO):

    _domain_type = Subroute

    def find_by_route(self, route_name: str) -> List[object]:
        return self._session.query(Subroute).filter(Subroute.route_name == route_name).order_by(Subroute.route_name).all()

    def find_by_start(self, start: str) -> List[object]:
        return self._session.query(Subroute).filter(Subroute.start == start).order_by(Subroute.start).all()

    def find_by_end(self, end: str) -> List[object]:
        return self._session.query(Subroute).filter(Subroute.end == end).order_by(Subroute.end).all()

    def find_by_transport_mean(self, transport_mean: str) -> List[object]:
        return self._session.query(Subroute).filter(Subroute.transport_mean == transport_mean).order_by(Subroute.transport_mean).all()
