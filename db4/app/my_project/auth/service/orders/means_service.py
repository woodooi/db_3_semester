from typing import List

from my_project.auth.dao import mean_dao
from my_project.auth.service.general_service import GeneralService


class MeanService(GeneralService):

    _dao = mean_dao

    def get_mean_by_name(self, name: str) -> List[object]:
        return self._dao.find_by_name(name)
