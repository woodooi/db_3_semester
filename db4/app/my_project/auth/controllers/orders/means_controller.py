from my_project.auth.service import mean_service
from my_project.auth.controllers.general_controller import GeneralController


class MeanController(GeneralController):

    _service = mean_service
