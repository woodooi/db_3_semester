from __future__ import annotations
from typing import Dict, Any

from my_project import db

class Guide(db.Model):
    __tablename__ = "guides"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)


    
    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "phone_number": self.phone_number
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Guide':
        return Guide(
            id=dto_dict.get("id", 0),
            name=dto_dict.get("name", ""),
            surname=dto_dict.get("surname", ""),
            age=dto_dict.get("age", 0),
            phone_number=dto_dict.get("phone_number", "")
        )
