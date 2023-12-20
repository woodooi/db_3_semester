from .orders.city_hotel_dao import CityHotelDao
from .orders.routes_dao import RouteDao
from .orders.route_stops_dao import RouteStopDao
from .orders.subroutes_dao import SubRouteDao
from .orders.hotels_dao import HotelDao
from .orders.stops_dao import StopDao
from .orders.means_dao import MeanDao
from .orders.guides_dao import GuideDAO
from .orders.excursions_dao import ExcursionDAO
from .orders.schedule_dao import ScheduleDAO

city_hotel_dao = CityHotelDao()
route_dao = RouteDao()
route_stop_dao = RouteStopDao()
subroute_dao = SubRouteDao()
hotel_dao = HotelDao()
stop_dao = StopDao()
mean_dao = MeanDao()
excursion_dao = ExcursionDAO()
schedule_dao = ScheduleDAO()
guide_dao = GuideDAO()
