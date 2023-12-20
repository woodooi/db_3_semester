from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class CityHotel(db.Model):
    __tablename__ = "city_hotel"

    city = db.Column(db.String(20), db.ForeignKey('stops.city'), primary_key=True, nullable=False)
    id_hotel = db.Column(db.Integer, db.ForeignKey('hotels.id_hotel'), primary_key=True, nullable=False)

    stop = db.relationship('Stop', backref=db.backref('city_hotel', lazy=True))
    hotel = db.relationship('Hotel', backref=db.backref('city_hotel', lazy=True))

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "city": self.city,
            "id_hotel": self.id_hotel
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'CityHotel':
        return CityHotel(
            city=dto_dict.get("city", ""),
            id_hotel=dto_dict.get("id_hotel", 0)
        )
