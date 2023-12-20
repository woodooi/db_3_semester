from my_project.auth.service import guides_service
from my_project.auth.controllers.general_controller import GeneralController


class GuideController(GeneralController):

    _service = guides_service
    