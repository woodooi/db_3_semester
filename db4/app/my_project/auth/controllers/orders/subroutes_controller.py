from my_project.auth.service import subroute_service
from my_project.auth.controllers.general_controller import GeneralController


class SubRouteController(GeneralController):

    _service = subroute_service
