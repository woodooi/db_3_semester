from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class Mean(db.Model):
    __tablename__ = "route_stops"

    route_name = db.Column(db.String(45), db.ForeignKey('routes.start_end'), primary_key=True, nullable=False)
    city_name = db.Column(db.String(20), db.ForeignKey('stops.city'), primary_key=True, nullable=False)

    route_stop = db.relationship('Route', backref=db.backref('route_stops', lazy=True))
    stop_route = db.relationship('Stop', backref=db.backref('route_stops', lazy=True))

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "route_name": self.route_name,
            "city_name": self.city_name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Mean':
        return Mean(
            route_name=dto_dict.get("route_name", ""),
            city_name=dto_dict.get("city_name", "")
        )
