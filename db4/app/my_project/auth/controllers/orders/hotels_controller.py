from my_project.auth.service import hotel_service
from my_project.auth.controllers.general_controller import GeneralController


class HotelController(GeneralController):

    _service = hotel_service
