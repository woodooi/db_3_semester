from .orders.routes_service import RouteService
from .orders.stops_service import StopService
from .orders.hotels_service import HotelService
from .orders.means_service import MeanService
from .orders.route_stops_service import RouteStopService
from .orders.city_hotel_service import CityHotelService
from .orders.subroutes_service import SubRouteService
from .orders.guides_service import GuideService
from .orders.schedule_service import ScheduleService
from .orders.excursions_service import ExcursionService

route_service = RouteService()
stop_service = StopService()
hotel_service = HotelService()
mean_service = MeanService()
route_stop_service = RouteStopService()
city_hotel_service = CityHotelService()
subroute_service = SubRouteService()
excursion_service = ExcursionService()
guides_service = GuideService()
schedule_service = ScheduleService()
