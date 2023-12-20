from typing import List

from my_project.auth.dao import schedule_dao
from my_project.auth.service.general_service import GeneralService

class ScheduleService(GeneralService):

    _dao = schedule_dao
    