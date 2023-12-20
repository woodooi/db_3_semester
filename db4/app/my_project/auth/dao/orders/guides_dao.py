from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Guide

class GuideDAO(GeneralDAO):

    _domain_type = Guide
