from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class Schedule(db.Model):
    __tablename__ = "schedule"

    trip_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_exc = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    guide_id = db.Column(db.Integer, nullable=False)

    sched_to_excursion = db.relationship('Excursion', foreign_keys=[id_exc], backref=db.backref('schedule', lazy=True))
    sched_to_guide = db.relationship('Guide', foreign_keys=[guide_id], backref=db.backref('schedule', lazy=True))

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "trip_id": self.trip_id,
            "id_exc": self.id_exc,
            "date": self.date,
            "guide_id": self.guide_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Schedule':
        return Schedule(
            trip_id=dto_dict.get("trip_id", 0),
            id_exc=dto_dict.get("id_exc", 0),
            date=dto_dict.get("date", ""),
            guide_id=dto_dict.get("guide_id", 0)
        )
