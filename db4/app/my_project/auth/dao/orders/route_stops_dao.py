from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import CityHotel
from my_project.auth.domain import Stop


class RouteStopDao(GeneralDAO):

    _domain_type = CityHotel

    def find_all_stops_for_route(self, route_name: str) -> List[Stop]:
        route_stops = CityHotel.query.filter_by(route_name=route_name).all()
        stops = [route_stop.stop for route_stop in route_stops]
        return stops
