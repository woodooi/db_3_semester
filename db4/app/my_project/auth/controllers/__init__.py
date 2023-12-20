
from .orders.routes_controller import RouteController
from .orders.stops_controller import StopController
from .orders.hotels_controller import HotelController
from .orders.means_controller import MeanController
from .orders.route_stops_controller import RouteStopController
from .orders.city_hotel_controller import CityHotelController
from .orders.subroutes_controller import SubRouteController
from .orders.excursions_controller import ExcursionController
from .orders.guides_controller import GuideController
from .orders.schedule_controller import ScheduleController


route_controller = RouteController()
stop_controller = StopController()
hotel_controller = HotelController()
mean_controller = MeanController()
route_stop_controller = RouteStopController()
city_hotel_controller = CityHotelController()
subroute_controller = SubRouteController()
excursion_controller = ExcursionController()
guide_controller = GuideController()
schedule_controller = ScheduleController()
