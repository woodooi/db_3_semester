from my_project.auth.service import schedule_service
from my_project.auth.controllers.general_controller import GeneralController


class ScheduleController(GeneralController):

    _service = schedule_service
