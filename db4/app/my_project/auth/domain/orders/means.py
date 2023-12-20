from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class CityHotel(db.Model):
    __tablename__ = "means"

    id_mean = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    num_of_seats = db.Column(db.Integer, nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id_mean,
            "name": self.name,
            "num_of_seats": self.num_of_seats
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'CityHotel':
        return CityHotel(
            id_mean =dto_dict.get("id"),
            name=dto_dict.get("name", ""),
            num_of_seats=dto_dict.get("num_of_seats", 0)
        )
