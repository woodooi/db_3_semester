from my_project.auth.service import city_hotel_service
from my_project.auth.controllers.general_controller import GeneralController


class CityHotelController(GeneralController):

    _service = city_hotel_service
