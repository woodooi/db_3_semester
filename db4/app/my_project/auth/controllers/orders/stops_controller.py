from my_project.auth.service import stop_service
from my_project.auth.controllers.general_controller import GeneralController


class StopController(GeneralController):

    _service = stop_service

    