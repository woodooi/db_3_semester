from __future__ import annotations
from typing import Dict, Any

from flask import jsonify

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Route(db.Model, IDto):
    __tablename__ = "routes"

    id_route = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_end: str = db.Column(db.String(45), unique=True, nullable=False)
    distance = db.Column(db.Integer, nullable=False)

    stops = db.relationship('RouteStop', backref=db.backref('route'), lazy=True)

    def call_stored_procedure():
        with db.engine.connect() as connection:
            result = connection.execute("CALL DynamicTableCreationForRoutes();")

            return jsonify({"status": "success", "message": "Stored procedure called successfully"})

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id_route": self.id_route,
            "start_end": self.start_end,
            "distance": self.distance
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Route:
        return Route(
            id_route=dto_dict.get("id_route", 0),
            start_end=dto_dict.get("start_end", ""),
            distance=dto_dict.get("distance", 0)
        )
