from __future__ import annotations
from typing import Dict, Any

from my_project import db

class Hotel(db.Model):
    __tablename__ = "hotels"

    id_hotel = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(20), nullable=False)
    hotel = db.Column(db.String(45), unique=True, nullable=False)
    price_for_night = db.Column(db.Integer, nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id_hotel": self.id_hotel,
            "city": self.city,
            "hotel": self.hotel,
            "price_for_night": self.price_for_night
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Hotel':
        return Hotel(
            id_hotel=dto_dict.get("id_hotel", 0),
            city=dto_dict.get("city", ""),
            hotel=dto_dict.get("hotel", ""),
            price_for_night=dto_dict.get("price_for_night", 0)
        )
