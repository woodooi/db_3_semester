from my_project.auth.service import excursion_service
from my_project.auth.controllers.general_controller import GeneralController


class ExcursionController(GeneralController):

    _service = excursion_service
