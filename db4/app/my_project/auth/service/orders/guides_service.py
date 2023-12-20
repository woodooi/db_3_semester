from typing import List

from my_project.auth.dao import guide_dao
from my_project.auth.service.general_service import GeneralService

class GuideService(GeneralService):

    _dao = guide_dao
    