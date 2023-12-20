from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class Stop(db.Model):
    __tablename__ = "stops"

    id_stop = db.Column(db.Integer, primary_key=True, nullable=False)
    city = db.Column(db.String(20), unique=True, nullable=False)
    postal_code = db.Column(db.String(10), nullable=False)

    routes = db.relationship('RouteStop', backref=db.backref('stop'), lazy=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id_stop,
            "city": self.city,
            "postal_code": self.postal_code
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Stop':
        return Stop(
            id_stop=dto_dict.get("id_stop", 0),
            city=dto_dict.get("city", ""),
            postal_code=dto_dict.get("postal_code", "")
        )
