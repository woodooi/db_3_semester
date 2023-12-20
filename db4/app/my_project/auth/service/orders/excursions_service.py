from typing import List

from my_project.auth.dao import excursion_dao
from my_project.auth.service.general_service import GeneralService

class ExcursionService(GeneralService):

    _dao = excursion_dao
    