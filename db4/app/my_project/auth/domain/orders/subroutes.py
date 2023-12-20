from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Subroute(db.Model):
    __tablename__ = "subroutes"

    id_subroute = db.Column(db.Integer, primary_key=True, nullable=False)
    route_name = db.Column(db.String(45), db.ForeignKey('routes.start_end'), nullable=False)
    start = db.Column(db.String(20), db.ForeignKey('stops.city'), nullable=False)
    end = db.Column(db.String(20), db.ForeignKey('stops.city'), nullable=False)
    transport_mean = db.Column(db.String(20), db.ForeignKey('means.name'), nullable=False)

    route = db.relationship('Route', foreign_keys=[route_name], backref=db.backref('subroutes', lazy=True))
    start_stop = db.relationship('Stop', foreign_keys=[start], backref=db.backref('start_subroutes', lazy=True))
    end_stop = db.relationship('Stop', foreign_keys=[end], backref=db.backref('end_subroutes', lazy=True))
    mean = db.relationship('Mean', foreign_keys=[transport_mean], backref=db.backref('subroutes', lazy=True))

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id_subroute": self.id_subroute,
            "route_name": self.route_name,
            "start": self.start,
            "end": self.end,
            "transport_mean": self.transport_mean
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Subroute':
        return Subroute(
            id_subroute=dto_dict.get("id_subroute", 0),
            route_name=dto_dict.get("route_name", ""),
            start=dto_dict.get("start", ""),
            end=dto_dict.get("end", ""),
            transport_mean=dto_dict.get("transport_mean", "")
        )
