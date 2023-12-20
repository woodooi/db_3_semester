from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class Excursion(db.Model):
    __tablename__ = "excursion"

    id_exc = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name_excursion = db.Column(db.String(100), unique=True, nullable=False)
    route = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    time_in_hours = db.Column(db.Integer, nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id_exc": self.id_exc,
            "name_excursion": self.name_excursion,
            "route": self.route,
            "price": self.price,
            "description": self.description,
            "time_in_hours": self.time_in_hours
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Excursion':
        return Excursion(
            id_exc=dto_dict.get("id_exc", 0),
            name_excursion=dto_dict.get("name_excursion", ""),
            route=dto_dict.get("route", ""),
            price=dto_dict.get("price", 0),
            description=dto_dict.get("description", ""),
            time_in_hours=dto_dict.get("time_in_hours", 0)
        )
